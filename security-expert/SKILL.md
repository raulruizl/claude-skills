---
name: security-expert
description: Use when assessing security posture, threat modeling, reviewing code for vulnerabilities, conducting authorized penetration testing, hardening AWS or on-prem Kubernetes/Docker infrastructure, evaluating data security, reviewing AI/LLM systems for security risks, or ensuring compliance with SOC2/HIPAA/GDPR/PCI/NIST/CIS frameworks.
---

# Security Expert

## Overview

Security is not a checklist — it is a mindset applied at every layer: code, infrastructure, data, network, and AI. Think like an attacker to defend like an architect. Always operate within authorized scope. Document every finding with severity, evidence, and remediation.

## CRITICAL: Authorization First (Pentesting)

**Before ANY offensive security action:**
- [ ] Written authorization from system owner confirmed?
- [ ] Scope defined (IPs, domains, accounts, services in/out of scope)?
- [ ] Rules of engagement agreed (time window, methods, escalation path)?
- [ ] Emergency stop contact identified?

**Never proceed without explicit written authorization. No exceptions.**

---

## Security Principles

### 1. Assume Breach
Design as if attackers are already inside. Lateral movement controls, blast radius limits, detection over prevention alone.

### 2. Defense in Depth
Multiple independent security layers. No single control failure = full compromise.

### 3. Least Privilege
Every identity (human, service, role) gets minimum permissions needed. No wildcards. No permanent admin access.

### 4. Shift Left
Security in design, code review, CI/CD — not just at deployment. Catch vulnerabilities before they ship.

### 5. Zero Trust
Never trust, always verify. No implicit trust from network location. mTLS between services. Identity-based access everywhere.

### 6. Security by Design, Not Obscurity
Architecture withstands public scrutiny. Secrets are secrets; algorithms are not.

### 7. Risk-Based Prioritization
Not all vulnerabilities are equal. Prioritize by: exploitability × impact × exposure. Fix Critical/High first.

### 8. Secure the Data, Not Just the Perimeter
Classify data. Encrypt at rest and in transit. Data is the target — protect it directly.

### 9. Document Everything
Every finding: severity, evidence, CVSS score, reproduction steps, remediation. Security work without documentation never happened.

---

## Mandatory Outputs

Every security assessment MUST produce:

**1. Threat Model**
```
Asset: [what are we protecting?]
Threat actors: [who attacks this and why?]
Attack vectors: [how would they get in?]
Controls in place: [what's already there?]
Residual risk: [what's still exposed?]
```

**2. Findings Report (per vulnerability)**
```
ID: VULN-NNN
Title: [short name]
Severity: Critical | High | Medium | Low | Informational
CVSS Score: [0.0–10.0]
Component: [file/service/resource affected]
Description: [what is the vulnerability?]
Evidence: [exact proof — command output, screenshot, code line]
Impact: [what can attacker achieve?]
Remediation: [specific fix with code/config example]
References: [CVE, CWE, OWASP link]
```

**3. Risk Matrix**
| Severity | Count | Top Finding |
|----------|-------|-------------|
| Critical | N | ... |
| High | N | ... |
| Medium | N | ... |
| Low | N | ... |

---

## Penetration Testing Methodology

### Phase 1: Reconnaissance (Passive)
```bash
# DNS enumeration
dig ANY target.com
subfinder -d target.com
amass enum -d target.com

# Certificate transparency
curl "https://crt.sh/?q=%.target.com&output=json"

# Technology fingerprinting
whatweb target.com
wappalyzer (browser)

# OSINT
theHarvester -d target.com -b all
shodan search hostname:target.com
```

### Phase 2: Scanning (Active — requires authorization)
```bash
# Port + service scan
nmap -sV -sC -O -p- --min-rate 5000 target.com

# Web vulnerability scan
nikto -h https://target.com
nuclei -u https://target.com -t cves/ -t exposures/

# SSL/TLS assessment
testssl.sh https://target.com
sslyze --regular target.com

# Directory/endpoint discovery
ffuf -w /usr/share/wordlists/dirb/big.txt -u https://target.com/FUZZ
gobuster dir -u https://target.com -w wordlist.txt
```

### Phase 3: Exploitation (Authorized Only)
```bash
# Web app
sqlmap -u "https://target.com/item?id=1" --dbs
burpsuite (manual testing, intercept, repeat)

# AWS misconfiguration exploitation
prowler -g extras    # all extras checks
pacu                 # AWS exploitation framework

# K8s
kubectl auth can-i --list --as=system:anonymous
kube-hunter --remote target-ip

# Password attacks
hydra -L users.txt -P passwords.txt ssh://target.com
```

### Phase 4: Post-Exploitation
- Document exactly what was accessed
- Do NOT exfiltrate real data — prove access only
- Screenshot / log evidence
- Stop when scope boundary reached

### Phase 5: Reporting
- Every finding with reproduction steps
- Remediation per finding
- Executive summary (non-technical)
- Risk prioritization matrix

---

## Code Vulnerability Review

### OWASP Top 10 (2021) — Check Every Review
| # | Vulnerability | Look For |
|---|---------------|----------|
| A01 | Broken Access Control | Missing authz checks, IDOR, path traversal |
| A02 | Cryptographic Failures | Weak ciphers, plaintext secrets, MD5/SHA1 |
| A03 | Injection | SQL, NoSQL, OS command, LDAP, XPath injection |
| A04 | Insecure Design | No threat model, missing security controls by design |
| A05 | Security Misconfiguration | Default creds, open S3, verbose errors, CORS wildcard |
| A06 | Vulnerable Components | Outdated deps with known CVEs |
| A07 | Auth & Session Failures | Weak passwords, no MFA, session fixation |
| A08 | Software Integrity Failures | No code signing, untrusted CI/CD pipeline |
| A09 | Logging & Monitoring Failures | No audit log, no alerts on suspicious activity |
| A10 | SSRF | User-controlled URLs fetched server-side |

### Code Review Checklist
```
Authentication:
- [ ] Passwords hashed with bcrypt/argon2 (not MD5/SHA1)?
- [ ] MFA enforced for privileged accounts?
- [ ] JWT validated (signature, expiry, algorithm)?
- [ ] No hardcoded credentials in code or config?

Authorization:
- [ ] Every endpoint checks permissions (not just authentication)?
- [ ] Direct object references validated against user ownership?
- [ ] Privilege escalation paths blocked?

Input Validation:
- [ ] All user input validated, sanitized, and parameterized?
- [ ] File uploads restricted by type, size, content?
- [ ] XML/JSON parsers protected against XXE?

Cryptography:
- [ ] TLS 1.2+ only (no SSLv3, TLS 1.0/1.1)?
- [ ] Secrets in vault (not env vars, not code)?
- [ ] Encryption uses AES-256-GCM or ChaCha20?

Logging:
- [ ] Auth events logged (success + failure)?
- [ ] No PII/secrets in logs?
- [ ] Logs tamper-proof (separate account / immutable storage)?
```

### Common Injection Patterns to Flag

**SQL Injection:**
```python
# VULNERABLE
query = f"SELECT * FROM users WHERE id = {user_id}"

# SAFE
query = "SELECT * FROM users WHERE id = %s"
cursor.execute(query, (user_id,))
```

**Command Injection:**
```python
# VULNERABLE
os.system(f"convert {filename} output.pdf")

# SAFE
subprocess.run(["convert", filename, "output.pdf"], shell=False)
```

**SSRF:**
```python
# VULNERABLE
requests.get(user_provided_url)

# SAFE — validate against allowlist
ALLOWED = ["api.internal.com", "partner.com"]
parsed = urlparse(user_provided_url)
if parsed.hostname not in ALLOWED:
    raise ValueError("Blocked")
```

---

## AWS Security

### IAM Hardening
```bash
# Audit root account usage
aws iam get-account-summary
aws iam generate-credential-report && aws iam get-credential-report

# Find overly permissive policies
aws iam list-policies --scope Local
# Look for: Action: "*", Resource: "*"

# Find unused roles/users
aws iam get-last-accessed-services --arn <role-arn>
```

### AWS Security Checklist
```
Identity:
- [ ] Root account has no access keys
- [ ] Root account has MFA
- [ ] No inline policies (use managed)
- [ ] SCPs applied at org level to deny dangerous actions
- [ ] IAM Access Analyzer enabled

Network:
- [ ] No 0.0.0.0/0 ingress on sensitive ports (22, 3389, 5432)
- [ ] VPC Flow Logs enabled
- [ ] Security groups follow least-privilege
- [ ] Private subnets for all data workloads

Data:
- [ ] S3 Block Public Access enabled account-wide
- [ ] S3 buckets encrypted (SSE-KMS)
- [ ] No public S3 buckets (unless intentional CDN)
- [ ] RDS encrypted at rest + in transit
- [ ] Lake Formation controls on Glue Catalog

Detection:
- [ ] GuardDuty enabled (all regions)
- [ ] Security Hub enabled + CIS benchmark
- [ ] CloudTrail enabled (all regions, S3 + CloudWatch)
- [ ] Config Rules for compliance drift
- [ ] Macie for PII detection in S3
```

### Common AWS Misconfigs (High Value Targets)
| Misconfiguration | Check |
|-----------------|-------|
| Public S3 bucket | `aws s3api get-bucket-acl --bucket <name>` |
| EC2 metadata SSRF (IMDSv1) | Check if IMDSv2 enforced: `aws ec2 describe-instances` |
| Wildcard IAM policy | `iam:*` or `s3:*` with `Resource: "*"` |
| Exposed secrets in Lambda env | `aws lambda get-function-configuration` |
| Open security group | Port 0-65535 from 0.0.0.0/0 |
| Unencrypted snapshot | `aws ec2 describe-snapshots` |

---

## Kubernetes / Container Security

### K8s Hardening Checklist
```
Cluster:
- [ ] RBAC enabled (no --authorization-mode=AlwaysAllow)
- [ ] Anonymous auth disabled on API server
- [ ] Audit logging enabled
- [ ] Network policies enforced (default deny all)
- [ ] Pod Security Standards enforced (restricted profile)

Workloads:
- [ ] No privileged containers
- [ ] No hostNetwork / hostPID / hostIPC
- [ ] Read-only root filesystem
- [ ] Non-root user (runAsNonRoot: true)
- [ ] Resource limits set (CPU + memory)
- [ ] Secrets from vault (not K8s Secrets in plain YAML)

Images:
- [ ] No latest tag (pin to digest)
- [ ] Base images scanned (Trivy, Snyk)
- [ ] No secrets baked into image layers
- [ ] Images from trusted registry only
```

### K8s Scanning Tools
```bash
# Cluster security scan
kube-bench                          # CIS benchmark
kube-hunter --remote <ip>           # pentest K8s
kubectl-who-can list pods           # RBAC audit

# Image scanning
trivy image nginx:latest
grype my-app:1.0.0

# Runtime security
falco                               # runtime threat detection
```

---

## Data Security

### Data Classification
| Level | Examples | Controls |
|-------|----------|---------|
| Public | Marketing content | Basic integrity |
| Internal | Business reports | Access logging |
| Confidential | Customer PII, financials | Encryption + RBAC + audit |
| Restricted | Health data, credentials | Encryption + MFA + DLP + audit |

### Data Pipeline Security
- [ ] Encrypt data in transit between all pipeline stages (TLS)
- [ ] Encrypt at rest (S3 SSE-KMS, RDS encryption)
- [ ] Column-level encryption for PII/PHI in data warehouse
- [ ] Data masking / tokenization before non-prod environments
- [ ] Lake Formation row/column filters for fine-grained access
- [ ] Audit log all data access (CloudTrail data events on S3)
- [ ] DLP policy: scan outbound data for PII leakage

---

## AI / LLM Security

### Threat Model for AI Systems
| Threat | Attack | Mitigation |
|--------|--------|-----------|
| Prompt injection | Malicious input hijacks agent behavior | Input sanitization, system prompt hardening, output validation |
| Data poisoning | Attacker corrupts training/RAG data | Source validation, data signing, anomaly detection on embeddings |
| Model inversion | Extract training data from model | Differential privacy, output filtering, rate limiting |
| Insecure tool use | Agent calls destructive tools without check | Tool allowlist, human-in-the-loop for destructive actions |
| Jailbreak | Bypass safety controls | Red-teaming, robust system prompts, content filters |
| Sensitive data in RAG | PII retrieved and exposed | Data classification before ingestion, access-controlled vector store |
| Embedding inversion | Reconstruct text from embeddings | Don't expose raw embeddings externally |

### AI Security Checklist
```
- [ ] Prompt injection tested (indirect + direct)
- [ ] RAG data classified — no PII without access control
- [ ] Vector store access requires authentication
- [ ] Agent tool use has explicit allowlist (no wildcard tool access)
- [ ] Destructive actions require confirmation or human-in-the-loop
- [ ] LLM outputs validated before acting on them (never trust blindly)
- [ ] API keys for LLM services in vault, rotated regularly
- [ ] Model access logged and audited
- [ ] Red-team the system before production
```

---

## DevSecOps — Shift-Left Pipeline

```
Code commit
    ↓
Pre-commit hooks: secret scanning (gitleaks, detect-secrets)
    ↓
CI: SAST (Semgrep, Bandit, Checkov for IaC)
    ↓
CI: Dependency scan (Snyk, OWASP Dependency-Check, Trivy)
    ↓
CI: Container image scan (Trivy, Grype)
    ↓
CD: DAST on staging (OWASP ZAP, Nuclei)
    ↓
CD: IaC scan before apply (Checkov, tfsec)
    ↓
Production: Runtime monitoring (Falco, GuardDuty, WAF)
```

### Tools Reference
| Category | Tool | Use |
|----------|------|-----|
| Secret scanning | Gitleaks, detect-secrets | Pre-commit + CI |
| SAST | Semgrep, Bandit (Python), CodeQL | CI |
| IaC scanning | Checkov, tfsec, KICS | CI before terraform apply |
| Dependency CVE | Snyk, OWASP Dep-Check, Trivy | CI |
| Container scan | Trivy, Grype, Anchore | CI + registry |
| DAST | OWASP ZAP, Nuclei, Burp Suite | Staging |
| K8s security | kube-bench, kube-hunter, Falco | Cluster audit + runtime |
| AWS audit | Prowler, ScoutSuite, AWS Security Hub | Account review |
| Pentest | Nmap, Metasploit, SQLMap, FFUF | Authorized testing only |
| Secrets mgmt | AWS Secrets Manager, HashiCorp Vault | Production |

---

## Compliance Framework Quick Reference

| Framework | Applies to | Key Controls |
|-----------|-----------|--------------|
| SOC2 | SaaS, cloud services | CC6–CC9: logical access, change mgmt, risk |
| HIPAA | Healthcare data (PHI) | Encryption, audit logs, BAA, breach notification |
| GDPR | EU personal data | Consent, right to erasure, DPA, breach 72h notify |
| PCI-DSS | Card data (CHD) | Network segmentation, encryption, vulnerability mgmt |
| NIST CSF | US federal / voluntary | Identify, Protect, Detect, Respond, Recover |
| CIS Benchmarks | Cloud + OS hardening | Scored config baselines for AWS, K8s, Linux |

---

## Common Security Mistakes

| Mistake | Correct Approach |
|---------|-----------------|
| IAM wildcard permissions | Scope to specific actions + resources |
| Secrets in .env files committed | Vault + gitleaks pre-commit hook |
| No MFA on privileged accounts | Enforce MFA via SCP / IAM condition |
| Public S3 buckets for data | Block public access, use pre-signed URLs |
| IMDSv1 on EC2 (SSRF risk) | Enforce IMDSv2 (hop limit = 1) |
| Privileged K8s containers | Pod Security Standards: restricted |
| Testing without authorization | Always get written scope before scanning |
| PII in RAG without access control | Classify + gate access to vector store |
| Treating pentesting as one-time | Continuous: automate DAST + dependency scans |
| No incident response plan | Define runbook before breach, not during |
