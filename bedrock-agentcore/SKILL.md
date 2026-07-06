---
name: bedrock-agentcore
description: Use when building, deploying, or debugging an Amazon Bedrock AgentCore Runtime agent (Strands SDK, container-based deploy to ECR, IAM execution role, CLI-driven runtime creation). Covers the full loop from agent.py scaffold to a real invoke against a deployed runtime.
---

# Bedrock AgentCore Runtime — build & deploy

## Overview

AgentCore Runtime hosts an agent as a container that AWS pulls from ECR and runs behind an
`InvokeAgentRuntime` API. There are two deployment artifact types
(`containerConfiguration` vs `codeConfiguration`); **container is the proven path** — it's
what every working example uses. Don't reach for `codeConfiguration` (zip-from-S3) without
testing it first; it's undocumented enough that its dependency-installation behavior is
unverified as of this writing.

No native Terraform resource exists for the agent runtime itself (checked: `hashicorp/aws`
provider v5.100.0 has no `bedrockagentcore`/`agent_runtime` resource). Terraform manages the
ECR repo + IAM role; the runtime itself is created via `aws bedrock-agentcore-control
create-agent-runtime` CLI, and its ARN is fed back in as a variable for anything that needs to
invoke it (e.g. a proxy Lambda). This is not a workaround — it's the standard pattern until
AWS ships the resource.

## Stack

- **Agent code**: Python, `strands-agents` (the Agent/tool framework) +
  `bedrock-agentcore` (the `BedrockAgentCoreApp` runtime wrapper).
- **Model**: `strands.models.BedrockModel`, pointed at a Bedrock inference profile ID (not a
  bare foundation-model ID for cross-region/on-demand models — check
  `aws bedrock list-inference-profiles --region <region>` for what's actually enabled in the
  account before hardcoding a model ID).
- **Container**: `python:3.12-slim`, arm64 (AgentCore requires arm64), built with
  `docker buildx --platform linux/arm64`, pushed to ECR.
- **Runtime**: created once via CLI, `networkMode: PUBLIC` for a no-VPC single-tenant setup.

## Minimal agent.py shape

```python
from bedrock_agentcore.runtime import BedrockAgentCoreApp
from strands import Agent
from strands.models import BedrockModel

from tools.my_tool import my_tool

SYSTEM_PROMPT = """..."""

app = BedrockAgentCoreApp()
_model = BedrockModel(model_id="eu.anthropic.claude-haiku-4-5-20251001-v1:0")
_agent = Agent(model=_model, tools=[my_tool], system_prompt=SYSTEM_PROMPT)

@app.entrypoint
def invoke_agent(payload: dict, context=None) -> dict:
    prompt = payload.get("prompt", "")
    result = _agent(prompt)
    return {"response": result.message["content"][0]["text"]}

if __name__ == "__main__":
    app.run()
```

Tools are plain functions decorated `@tool` from `strands`, with a docstring — the docstring
*is* the tool spec the model sees, so write it like an API doc (Args/Returns), not a comment.

## Dockerfile

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8080
CMD ["python", "agent.py"]
```

`requirements.txt` needs at minimum: `strands-agents`, `bedrock-agentcore`, `boto3`.

## Build & push (arm64 required)

```bash
aws ecr get-login-password --region <region> | \
  docker login --username AWS --password-stdin <account>.dkr.ecr.<region>.amazonaws.com

docker buildx build --platform linux/arm64 --provenance=false \
  --tag <account>.dkr.ecr.<region>.amazonaws.com/<repo>:<tag> --push .
```

`--provenance=false` matters — without it buildx attaches a provenance manifest that some
AgentCore validation paths reject.

## Terraform: ECR repo (works, use this)

```hcl
resource "aws_ecr_repository" "agent" {
  name                 = "<name>"
  image_tag_mutability = "IMMUTABLE"   # no exceptions — mutable tags = supply-chain risk
  image_scanning_configuration { scan_on_push = true }
  encryption_configuration { encryption_type = "AES256" }
}

resource "aws_ecr_lifecycle_policy" "agent" {
  repository = aws_ecr_repository.agent.name
  policy = jsonencode({
    rules = [{
      rulePriority = 1
      selection    = { tagStatus = "any", countType = "imageCountMoreThan", countNumber = 5 }
      action       = { type = "expire" }
    }]
  })
}
```

## Terraform: execution IAM role (verified working shape)

Trust policy — only `bedrock-agentcore.amazonaws.com` may assume it:

```hcl
resource "aws_iam_role" "agentcore" {
  name = "<name>-agentcore-runtime-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { Service = "bedrock-agentcore.amazonaws.com" }
      Action    = "sts:AssumeRole"
    }]
  })
}
```

Inline policy — confirmed working set of actions (verified against a live `READY` runtime):

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ECRPull",
      "Effect": "Allow",
      "Action": ["ecr:GetDownloadUrlForLayer", "ecr:BatchGetImage", "ecr:GetAuthorizationToken"],
      "Resource": "*"
    },
    {
      "Sid": "BedrockInvoke",
      "Effect": "Allow",
      "Action": ["bedrock:InvokeModel", "bedrock:InvokeModelWithResponseStream"],
      "Resource": "*"
    },
    {
      "Sid": "CloudWatchLogs",
      "Effect": "Allow",
      "Action": ["logs:CreateLogGroup", "logs:CreateLogStream", "logs:PutLogEvents"],
      "Resource": "*"
    }
  ]
}
```

Notes on tightening this (the observed example used `Resource: "*"` throughout — workable but
looser than this project's per-resource least-privilege bar):
- `ecr:GetAuthorizationToken` **cannot** be scoped to a resource — IAM requires `"*"` for it,
  full stop. `BatchGetImage`/`GetDownloadUrlForLayer` *can* be scoped to the specific repo ARN
  — do that.
- `bedrock:InvokeModel*` can be scoped to the specific inference-profile ARN
  (`arn:aws:bedrock:<region>:<account>:inference-profile/<profile-id>`) instead of `*` if you
  want to pin the agent to exactly one model.
- `logs:*` on `Resource: "*"` is hard to avoid because AgentCore auto-generates the log group
  name (contains the runtime ID, unknown before creation) — scoping to
  `arn:aws:logs:<region>:*:log-group:/aws/bedrock-agentcore/*` is a reasonable middle ground.
- Add whatever data-access actions the agent's tools actually need (e.g. `dynamodb:GetItem` on
  the specific table ARN) — nothing beyond that.

Then add per-tool permissions (DynamoDB, S3, etc.) scoped to the exact resource ARNs the
agent's tools touch — same least-privilege pattern as every other component.

## Create the runtime (CLI — no Terraform resource exists)

```bash
aws bedrock-agentcore-control create-agent-runtime \
  --agent-runtime-name <camelCaseName> \
  --agent-runtime-artifact '{"containerConfiguration":{"containerUri":"<account>.dkr.ecr.<region>.amazonaws.com/<repo>:<tag>"}}' \
  --role-arn arn:aws:iam::<account>:role/<name>-agentcore-runtime-role \
  --network-configuration '{"networkMode":"PUBLIC"}' \
  --region <region>
```

`--agent-runtime-name` must match `[a-zA-Z][a-zA-Z0-9_]{0,47}` — no hyphens.

To update after a new image push, re-run `create-agent-runtime` with the same name (it
versions) or use `update-agent-runtime` if you want to keep a stable runtime ID.

## Verify it's live

```bash
aws bedrock-agentcore-control list-agent-runtimes --region <region> \
  --query 'agentRuntimes[].{name:agentRuntimeName,arn:agentRuntimeArn,status:status}'

aws bedrock-agentcore-control get-agent-runtime --agent-runtime-id <id> --region <region>
```

Status should read `READY`. `get-agent-runtime` also echoes back the exact
`agentRuntimeArtifact`, `roleArn`, `networkConfiguration`, and `environmentVariables` it's
running with — useful for confirming a redeploy actually picked up the new image tag.

## Real invoke (data plane, different API than control plane)

Data-plane invocation goes through `bedrock-agentcore` (not `-control`):
`InvokeAgentRuntime`, given the runtime ARN and a JSON payload matching whatever
`payload.get(...)` keys `agent.py`'s entrypoint reads (e.g. `{"prompt": "..."}`).

## Downstream consumers

Anything invoking the runtime (a proxy Lambda, a WebSocket bridge) needs its own IAM
permission `bedrock-agentcore:InvokeAgentRuntime` scoped to the runtime ARN (and
`<arn>/*` — AgentCore issues sub-resource ARNs per invocation/session). Since the runtime ARN
only exists after the CLI step, wire it through Terraform as an input variable set after first
deploy, not as a resource reference.

## Common pitfalls

- Building the image for `amd64` (default on most dev machines) — AgentCore requires arm64,
  the runtime will fail to start with a platform mismatch.
- Forgetting `--provenance=false` on buildx — attaches metadata some AgentCore paths reject.
- Hardcoding a model ID without checking `list-inference-profiles` first — cross-region
  inference profile IDs (the `eu.`/`us.`/`global.` prefixed ones) are what's actually
  invocable, not always the bare foundation-model ID.
- Mutable ECR tags — always `IMMUTABLE` + `scan_on_push`, this is non-negotiable across every
  project that's used this pattern so far.
- Trying to find a Terraform-native way to create the runtime — there isn't one yet in AWS
  provider 5.x. Stop looking, use the CLI, store the ARN as a variable.
