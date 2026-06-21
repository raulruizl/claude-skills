---
name: data-governance
description: Use when designing data governance programs, assessing regulatory compliance (GDPR, CCPA/CPRA, HIPAA, SOX), preparing for audits (SOC2 Type II, ISO 27001, regulatory, internal), implementing data classification, building data catalogs, defining data policies, managing data lifecycle, or responding to data subject requests and breach incidents across EU and USA jurisdictions.
---

# Data Governance Expert

## Overview

Data governance is the system of decision rights and accountabilities for data-related processes. It ensures data is trustworthy, compliant, secure, and used responsibly. Think of it as: **the right people, making the right decisions, about the right data, at the right time.**

Governance without enforcement is decoration. Every policy must have an owner, a control, and an audit trail.

## Step 1: Understand Before Governing

Before designing any governance program:
- What data does the organization collect, process, and share?
- Which jurisdictions apply (EU, California, federal US, state laws)?
- What industry regulations apply (HIPAA, SOX, PCI, FedRAMP)?
- Who are data subjects? (EU residents, CA residents, patients, employees?)
- What third parties receive data (processors, sub-processors, vendors)?
- What systems hold what data? (inventory exists?)
- Has a ROPA (Record of Processing Activities) been created?
- What is the current breach response plan?

---

## Governance Roles (RACI)

| Role | Responsibility |
|------|---------------|
| **CDO / DPO** | Program ownership, regulatory liaison, DPA contact (GDPR requires DPO for certain orgs) |
| **Data Owner** | Business accountability for a data domain (e.g., HR owns employee data) |
| **Data Steward** | Day-to-day quality, classification, and policy enforcement for a domain |
| **Data Custodian** | Technical implementation (IT/engineering) — storage, access controls, backups |
| **Privacy Counsel** | Legal interpretation of regulations, contract review, breach notification decisions |
| **Internal Audit** | Independent assessment of controls, evidence review |

---

## 9 Governance Principles

### 1. Privacy by Design
Privacy controls built into systems from inception, not bolted on. Default: collect minimum, share minimum, retain minimum.

### 2. Data Minimization
Collect only what is necessary for the stated purpose. Document the purpose for every data element.

### 3. Data Quality as a First-Class Citizen
Governance without quality is meaningless. Accuracy, completeness, timeliness, consistency must be measured and owned.

### 4. Lineage is Evidence
Every data transformation must be traceable. Lineage is not optional — it is the proof auditors demand.

### 5. Classify Before You Process
Every dataset must be classified before use. Classification drives controls, retention, and access rights.

### 6. Consent and Lawful Basis are Non-Negotiable
Processing without documented lawful basis is a violation. No exceptions.

### 7. Retention is a Control, Not an Afterthought
Define retention periods before storing data. Keeping data longer than needed is a liability.

### 8. Audit Trails Are Immutable
Logs that can be modified are not evidence. Audit trails must be write-once, access-controlled, and time-stamped.

### 9. Governance is Continuous, Not a Project
Compliance is not a state — it is a practice. Policies must be reviewed, controls must be tested, risks must be reassessed.

---

## Mandatory Governance Artifacts

Every governed organization MUST maintain:

### 1. ROPA — Record of Processing Activities (GDPR Art. 30)
```
Processing activity: [name]
Controller/Processor: [who]
Purpose: [why processing]
Lawful basis: [consent / contract / legal obligation / vital interest / public task / legitimate interest]
Data categories: [what types]
Data subjects: [employees / customers / EU residents / etc.]
Recipients: [internal teams + third parties]
Third-country transfers: [if any, legal mechanism]
Retention period: [how long]
Security measures: [technical + organizational]
```

### 2. Data Classification Register
| Classification | Definition | Examples | Controls |
|---------------|------------|----------|---------|
| Public | Intended for public | Marketing, press releases | Integrity only |
| Internal | Business use, not public | Reports, internal docs | Access logging |
| Confidential | Sensitive business data | Customer PII, contracts | Encryption + RBAC + audit |
| Restricted | Regulated / high-risk | PHI, financial records, credentials | Encryption + MFA + DLP + audit + legal hold |

### 3. Data Retention Schedule
```
Data type | Retention period | Legal basis | Deletion method | Owner
Employee records | 7 years post-employment | Tax law / labor law | Secure wipe | HR
Customer PII | Duration of relationship + 3 years | Contract / legal | Anonymization or deletion | Legal
Financial records | 7 years | SOX / IRS | Secure archive | Finance
Health records | 6 years (HIPAA) / varies by state | HIPAA | Secure deletion | Compliance
Audit logs | 1–3 years | SOC2 / ISO 27001 | Immutable archive | IT Security
```

### 4. DPIA — Data Protection Impact Assessment (GDPR Art. 35)
Required when processing is likely to result in high risk:
- Large-scale processing of sensitive data
- Systematic monitoring of public areas
- New technologies (AI, biometrics, profiling)
```
Processing description:
Necessity and proportionality assessment:
Risks identified:
Mitigating measures:
DPO consultation outcome:
Residual risk accepted by: [Controller name + date]
```

### 5. Incident Response & Breach Notification Plan
```
Detection → 0h
Internal triage → <1h
Severity classification → <4h
Legal/DPO notification → <24h
Regulatory notification → GDPR: 72h | HIPAA: 60 days | CCPA: expedient
Subject notification → GDPR: without undue delay | HIPAA: 60 days | CCPA: expedient
Post-incident review → <30 days
```

---

## Compliance Quick Matrix

| Regulation | Who it applies to | Key obligation | Penalty |
|-----------|------------------|----------------|---------|
| GDPR | Any org processing EU resident data | Lawful basis, ROPA, DPO (if applicable), 72h breach notify | €20M or 4% global revenue |
| CCPA/CPRA | CA orgs > $25M revenue or 100K records | Opt-out of sale, deletion rights, privacy notice | $7,500/intentional violation |
| HIPAA | US healthcare entities + business associates | PHI safeguards, BAA, 60-day breach notify | Up to $1.9M/violation category/year |
| SOX | US public companies | Financial data integrity, internal controls, 7-yr retention | Criminal: up to 20 years prison |
| ISO 27001 | Any org (voluntary) | ISMS, 93 Annex A controls, certification audit | Certification loss |
| SOC2 Type II | SaaS / cloud services | Trust Service Criteria over audit period (6–12 mo) | Loss of customer trust + contracts |

**For detailed per-regulation requirements, see:**
- [compliance-reference.md](compliance-reference.md) — GDPR, CCPA, HIPAA, SOX deep dive
- [audit-playbook.md](audit-playbook.md) — SOC2, ISO 27001, regulatory, internal audit prep
- [contracts/dpa-template.md](contracts/dpa-template.md) — GDPR Art. 28 Data Processing Agreement
- [contracts/baa-template.md](contracts/baa-template.md) — HIPAA Business Associate Agreement
- [contracts/data-sharing-agreement.md](contracts/data-sharing-agreement.md) — Data Sharing Agreement (Controller-to-Controller)
- [contracts/nda-data-template.md](contracts/nda-data-template.md) — NDA for data and technical information

---

## Contract Writing

### Which Contract for Which Situation

| Situation | Contract Needed |
|-----------|----------------|
| Vendor processes personal data on your behalf | DPA (GDPR) |
| Vendor receives or creates PHI | BAA (HIPAA) |
| Two orgs share data as independent controllers | Data Sharing Agreement |
| Sharing confidential data/architecture in early discussions | NDA |
| Vendor in US processes EU personal data | DPA + SCCs (Module 2) |
| Subcontractor of a Business Associate receives PHI | BAA (BA → Subcontractor) |
| Research partner receives anonymized datasets | DSA (confirm truly anonymized first) |
| Joint venture — both parties control shared personal data | Joint Controller Agreement (JCA) |

### Contract Drafting Process
1. **Identify the relationship** — controller/processor, joint controllers, or pure sharing?
2. **Identify regulations** — GDPR? HIPAA? Both? State laws?
3. **Load the relevant template** — from contracts/ directory above
4. **Fill all [VARIABLES]** — none should remain blank before execution
5. **Confirm lawful basis** — document before signing, not after
6. **Legal review** — always have qualified counsel review before execution
7. **Execution** — both parties sign, retain executed copy
8. **Register** — add to vendor/processor registry with expiry date
9. **Renewal** — review annually; renegotiate if processing activities change

### Contract Registry (maintain this)
| Contract | Counterparty | Type | Signed Date | Expiry | Owner |
|----------|-------------|------|-------------|--------|-------|
| [Name] | [Vendor] | DPA/BAA/DSA/NDA | [Date] | [Date] | [Team] |

> **Important:** A contract without an expiry review is a compliance gap. All data contracts must be reviewed annually and updated when processing activities change.

---

## AWS Governance Stack

| Capability | AWS Service |
|-----------|-------------|
| Data catalog | AWS Glue Data Catalog |
| Fine-grained access | Lake Formation (row/column level) |
| PII detection | Amazon Macie |
| Compliance monitoring | AWS Config + Config Rules |
| Audit evidence | AWS Audit Manager |
| Immutable audit logs | CloudTrail + S3 Object Lock |
| Data residency control | AWS Organizations SCPs (deny non-approved regions) |
| Encryption key governance | AWS KMS + key policies |
| Data access auditing | S3 Access Logs + CloudTrail Data Events |
| Third-party access review | AWS IAM Access Analyzer |

---

## On-Prem / K8s Governance Stack

| Capability | Tool |
|-----------|------|
| Data catalog | Apache Atlas or DataHub |
| Policy enforcement | OPA / Gatekeeper (K8s) |
| PII scanning | Presidio (Microsoft OSS) or Faker + custom rules |
| Audit logging | Elasticsearch + immutable index policy |
| Data lineage | OpenLineage + Marquez |
| Access governance | Ranger (Hadoop) or Casbin (app-level) |
| Secrets | HashiCorp Vault |

---

## Data Subject Rights — Response Checklist

| Right | GDPR | CCPA | Response SLA | Process |
|-------|------|------|-------------|---------|
| Access / Know | Art. 15 | Yes | 30 days (GDPR) / 45 days (CCPA) | Identify all systems holding subject's data, compile report |
| Deletion / Erasure | Art. 17 | Yes | 30 days | Delete from all systems, notify processors, log action |
| Rectification | Art. 16 | No | 30 days | Update + propagate to downstream systems |
| Portability | Art. 20 | No | 30 days | Export in machine-readable format (JSON/CSV) |
| Opt-out of sale | No | Yes | 15 days | Suppress from data sharing with third parties |
| Restriction | Art. 18 | No | 30 days | Flag record, halt processing |
| Objection | Art. 21 | No | Immediately | Assess legitimate grounds, halt or justify |

---

## Common Governance Mistakes

| Mistake | Correct approach |
|---------|-----------------|
| No ROPA maintained | Mandatory under GDPR Art. 30, build before first audit |
| Consent used as lawful basis for everything | Match lawful basis to actual processing purpose |
| No data retention enforcement | Automate deletion with S3 lifecycle + DB TTL policies |
| Audit logs deletable by admins | Immutable storage (S3 Object Lock, WORM) |
| DPIA skipped for new AI system | AI + large-scale processing = DPIA mandatory |
| DPO role unfilled (required orgs) | Required: public authority, large-scale systematic monitoring, large-scale special category data |
| Breach response plan untested | Run tabletop exercise annually |
| Third-party processors without DPA/BAA | All processors must have signed agreement before data flows |
| Data classification done once | Review classification annually and on system change |
| Governance only in compliance team | Embed data stewards in every data-producing business unit |
