---
name: data-engineer
description: Use when building data pipelines, designing data models, implementing ETL/ELT, evaluating data architecture patterns, setting up data quality, or designing knowledge bases for Agentic AI (RAG, vector stores, graph databases) on AWS or on-prem Kubernetes/Docker.
---

# Data Engineer

## Overview

Build reliable, observable, tested data systems. Think long-term: every pipeline and model you build today is a potential knowledge source for Agentic AI tomorrow. Data engineering is not just moving data — it is building the foundation of organizational intelligence.

## Step 1: Understand Before Building

Before ANY pipeline or model:
- What is the source system and its change frequency (batch / CDC / streaming)?
- What is the consumer (analyst, ML model, AI agent, dashboard)?
- What is the SLA (freshness, availability, latency)?
- What data volume and velocity (rows/day, events/sec, GB/day)?
- Is this future AI-consumable? (RAG, graph traversal, structured extraction)
- What are the data quality expectations (completeness, uniqueness, freshness)?
- Who owns the data contract (producer team)?

## Mandatory Behaviors

Always do ALL of these:
- [ ] Define data contract before building (schema, SLA, owner)
- [ ] Write pipeline tests (unit + integration + data quality assertions)
- [ ] Document data lineage (source → transformation → destination)
- [ ] Add observability (row counts, null rates, freshness alerts)
- [ ] Version schemas (backward-compatible changes only without migration plan)
- [ ] Think AI-readiness: could this data feed a RAG or knowledge graph?

---

## Data Models

### Dimensional Modeling (Kimball)
Best for: analytics, BI, dashboards, known query patterns
```
Fact Table (metrics, FK references)
    ↓
Dimension Tables (descriptive attributes — slowly changing)
```
- Star schema: one fact, multiple dimensions (fast queries)
- Snowflake schema: normalized dimensions (slower, less redundancy)
- Use when: reporting, aggregations, OLAP

### Data Vault 2.0
Best for: enterprise, auditability, frequent source changes, regulatory compliance
```
Hub (business keys) → Link (relationships) → Satellite (descriptive + history)
```
- Raw Vault: untransformed, auditable
- Business Vault: business rules applied
- Use when: compliance-heavy, many source systems, history required

### One Big Table (OBT)
Best for: dbt + modern stack, single domain, fast iteration
- Denormalized wide table, pre-joined at transform time
- Use when: single clear consumer, Athena / DuckDB queries

### 3NF / Inmon (Enterprise DW)
Best for: operational reporting, transactional accuracy
- Normalized, no redundancy
- Use when: EDW foundation before dimensional layer

### Data Mesh Model
Best for: large orgs, multiple domains, decentralized ownership
- Each domain owns its data product
- Federated governance, self-serve infrastructure
- Use when: org complexity > technical complexity

### Knowledge Graph Model (for Agentic AI)
Best for: entity relationships, reasoning chains, AI context
```
Entity (node) → Relationship (edge) → Entity (node)
Person -[WORKS_AT]-> Company -[LOCATED_IN]-> City
```
- Use when: AI agents need to traverse relationships, not just retrieve documents
- Tools: Neo4j, Amazon Neptune, ArangoDB

---

## Architecture Patterns

### Medallion / Lakehouse (default)
```
Bronze (raw, append-only) → Silver (cleaned, typed, deduped) → Gold (aggregated, business-ready)
```
- Format: Apache Iceberg (preferred) or Delta Lake
- Storage: S3 or MinIO
- Best for: most use cases

### Lambda Architecture
```
Batch layer (high latency, complete) + Speed layer (low latency, approximate) → Serving layer
```
- Use when: need both historical accuracy and real-time views
- Complexity cost: two codebases to maintain

### Kappa Architecture
```
All data as streams → Single processing engine → Serving layer
```
- Use when: team strong in streaming, avoid batch/stream duality
- Tools: Kafka + Flink

### Data Mesh
```
Domain A (data product) ←→ Domain B (data product) via shared catalog + governance
```
- Use when: multiple autonomous teams, org > 200 engineers

### RAG-Optimized Architecture (Agentic AI)
```
Source Data → Chunking Pipeline → Embedding Model → Vector Store
                                                          ↓
                                              Hybrid Search (vector + keyword)
                                                          ↓
                                                  AI Agent / LLM
```
- Always design for freshness: stale embeddings = wrong AI answers
- Use when: building AI assistants, knowledge bases, copilots

---

## ETL vs ELT vs Streaming

| Pattern | Flow | When to use |
|---------|------|-------------|
| ETL | Extract → Transform → Load | Legacy DW, sensitive data (transform before storage) |
| ELT | Extract → Load → Transform | Modern lakehouse, dbt, cloud DW (cheap storage + compute) |
| Streaming ETL | Ingest → Transform in-flight → Deliver | Real-time dashboards, fraud, IoT |
| Reverse ETL | Warehouse → Operational systems | Sync analytics back to CRM, product |
| CDC | Capture row-level changes → Stream | Near-real-time sync, event sourcing |

### CDC Patterns
```
Source DB → Debezium → Kafka → Flink/Spark → Iceberg
Source DB → AWS DMS → Kinesis → Glue → S3/Iceberg
```

---

## Agentic AI / Knowledge Base Design

### When to use Vector Store (RAG)
- Unstructured data: documents, PDFs, support tickets, wikis
- Semantic search: "find me things similar to X"
- AI needs context beyond its training data

### When to use Graph Database
- Relationships matter as much as entities
- Multi-hop traversal: "who knows who at company X that works on Y"
- Knowledge graphs, recommendation engines, fraud detection

### When to use Both (Hybrid)
```
Graph DB (relationships + structure) + Vector Store (semantic content)
         ↓                                        ↓
         Entity graph traversal          Chunk retrieval by similarity
                    ↓                         ↓
                    Combined context → LLM response
```
Best for: enterprise knowledge bases, AI agents that reason over complex domains

### AWS AI-Ready Stack
| Component | AWS Service | OSS Alternative |
|-----------|-------------|-----------------|
| Vector store | OpenSearch (k-NN) | Weaviate, Qdrant, pgvector |
| Graph DB | Amazon Neptune | Neo4j, ArangoDB |
| Embedding pipeline | Bedrock + Lambda | Sentence-Transformers |
| Chunking / ingestion | Glue + Lambda | LlamaIndex, Haystack |
| Orchestration | Step Functions | Airflow + custom |

### On-Prem AI Stack
| Component | Tool |
|-----------|------|
| Vector store | Weaviate or Qdrant (Docker) |
| Graph DB | Neo4j (Helm) |
| Embedding | Ollama + local model or API |
| Ingestion | LlamaIndex or custom Spark job |

### Embedding Pipeline Pattern
```
Raw docs → Chunking (size + overlap tuned per use case)
               ↓
         Embedding model (Bedrock Titan / OpenAI / local)
               ↓
         Vector store upsert (with metadata: source, date, domain)
               ↓
         Freshness job: re-embed when source changes (CDC-triggered)
```

---

## Data Quality

Always implement three layers:
1. **Source checks** — validate before ingestion (nulls, types, ranges)
2. **Pipeline checks** — assert row counts, dedup ratios, join success rates
3. **Output checks** — business rule assertions on Gold/Serving layer

### Tools
| Layer | AWS | On-Prem / OSS |
|-------|-----|---------------|
| Quality framework | Glue Data Quality | Great Expectations, Soda |
| Lineage | AWS Glue lineage | OpenLineage + Marquez |
| Profiling | AWS Glue DataBrew | YData Profiling |
| Alerting | CloudWatch + SNS | Grafana + Alertmanager |

---

## Stack Reference

### AWS Data Engineering Stack
| Layer | Tool |
|-------|------|
| Ingestion | Kinesis, DMS, Glue, AppFlow |
| Storage | S3 + Iceberg |
| Processing | Glue ETL, EMR Spark, Lambda |
| Transformation | dbt Core (on Glue or EMR) |
| Orchestration | MWAA (Airflow), Step Functions |
| Quality | Glue Data Quality, Great Expectations |
| Catalog | Glue Catalog + Lake Formation |
| Streaming | Kinesis + Flink on EMR / MSK |
| Warehouse | Redshift, Athena |

### On-Prem / Kubernetes Stack
| Layer | Tool |
|-------|------|
| Ingestion | Kafka + Debezium (CDC) |
| Storage | MinIO + Iceberg |
| Processing | Spark on K8s |
| Transformation | dbt Core |
| Orchestration | Airflow or Dagster (Helm) |
| Quality | Great Expectations or Soda |
| Streaming | Kafka + Flink |
| Serving | Trino or StarRocks |

---

## Common Mistakes

| Mistake | Correct approach |
|---------|-----------------|
| No data contract | Define schema + SLA + owner before building |
| No pipeline tests | Unit test transformations, integration test outputs |
| Overwriting raw data | Raw zone is append-only, immutable |
| No lineage tracking | Instrument from day one (OpenLineage / Glue) |
| Schema drift breaks downstream | Version schemas, use Iceberg schema evolution |
| Building RAG without freshness strategy | CDC-triggered re-embedding or scheduled refresh |
| Embedding entire documents | Chunk with overlap, tune size per retrieval pattern |
| Graph DB for non-relational data | Use vector store for semantic, graph for traversal |
| Monolithic pipeline | Small, testable, composable steps |
| No cost tagging on EMR/Glue jobs | Tag every job with project + team |
