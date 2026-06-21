# Audit Playbook — SOC2 Type II, ISO 27001, Regulatory, Internal

## How to Use This Playbook
Load this file when preparing for or responding to an audit. Each section covers:
- What auditors actually look for
- Evidence to collect before they ask
- Common failure points
- Response scripts for difficult questions

---

## SOC2 Type II

### What it is
Third-party audit of controls over a defined period (typically 6–12 months). Based on AICPA Trust Service Criteria (TSC). Report types:
- **Type I**: Controls designed appropriately (point in time)
- **Type II**: Controls operating effectively over time — THIS is what customers demand

### Trust Service Criteria
| Category | Code | Core focus |
|----------|------|-----------|
| Security | CC | Access control, change management, risk, monitoring |
| Availability | A | Uptime, incident response, capacity |
| Processing Integrity | PI | Complete, valid, accurate processing |
| Confidentiality | C | Protection of confidential info |
| Privacy | P | GDPR/CCPA alignment, personal data handling |

Most organizations pursue **Security (CC) + Availability (A)** minimum. Add Privacy (P) if handling personal data.

### 12-Month Readiness Timeline

**Months 1–2: Gap Assessment**
- Map current controls to TSC criteria
- Identify gaps (missing policies, untested controls, no evidence)
- Prioritize remediation by audit risk

**Months 3–8: Control Operation Period**
- All controls must operate consistently for the audit period
- Evidence collection begins NOW — every access review, change ticket, incident
- Training records, vendor reviews, vulnerability scans — all timestamped

**Months 9–10: Readiness Assessment (mock audit)**
- Internal walkthrough with all control owners
- Collect sample evidence per auditor request format
- Fix any evidence gaps

**Months 11–12: Auditor Fieldwork**
- Provide auditor with requested samples
- PBC (Provided By Client) list — respond within agreed SLA
- Do not interpret evidence — provide exactly what was requested

### Evidence Required (Common CC Controls)
| Control | Evidence |
|---------|---------|
| CC6.1 Logical access | User access list, provisioning tickets, deprovisioning records |
| CC6.2 Authentication | MFA enforcement screenshots, password policy, config export |
| CC6.3 Access reviews | Quarterly access review sign-off + any remediation tickets |
| CC7.1 Vulnerability mgmt | Scan reports, remediation tickets with dates, SLAs met |
| CC7.2 Monitoring | SIEM/alerting config, alert samples, incident log |
| CC8.1 Change management | Change tickets, approval records, testing evidence, post-deploy validation |
| CC9.2 Vendor management | Vendor list, risk tiers, SOC2 reports collected from critical vendors |
| A1.1 Availability | SLA/SLO definitions, uptime monitoring, incident log |

### Common SOC2 Failures
- Evidence gaps mid-period (control operated, but no documentation)
- Access reviews not completed quarterly
- Terminated employee accounts not removed within SLA
- Patch SLA breached without documented exception
- Critical vendor has no SOC2 report and no compensating control
- Change deployed without approval ticket

---

## ISO 27001

### What it is
International standard for Information Security Management Systems (ISMS). Certification requires:
1. Define scope of ISMS
2. Risk assessment + treatment plan
3. Statement of Applicability (SoA) — which Annex A controls apply and why
4. Implement controls
5. Internal audit
6. Management review
7. Certification audit (Stage 1 doc review + Stage 2 on-site)

### Annex A Control Domains (ISO 27001:2022 — 93 controls)
| Domain | Controls | Key focus |
|--------|---------|-----------|
| Organizational (5.x) | 37 | Policies, roles, threat intelligence, information security in projects |
| People (6.x) | 8 | Screening, training, disciplinary process, remote working |
| Physical (7.x) | 14 | Physical security, clean desk, equipment maintenance |
| Technological (8.x) | 34 | Access control, malware, logging, encryption, SDLC, vulnerability mgmt |

### Statement of Applicability (SoA)
Document that lists all 93 controls with:
- Applicable: Yes/No
- If No: justification for exclusion
- Implementation status
- Reference to policy/procedure that implements it

This is the most scrutinized document in ISO 27001 audit.

### Evidence Required
| Area | Evidence |
|------|---------|
| Risk assessment | Risk register with likelihood × impact scoring, treatment decisions |
| SoA | Complete, signed, current |
| Asset inventory | All information assets classified |
| Access control | User access lists, review records |
| Incident log | All incidents (including near-misses) with response documented |
| Internal audit | Internal audit report, findings, corrective actions |
| Management review | Minutes of management review meeting |
| Supplier management | Critical supplier list, security assessments |
| Business continuity | BCP/DRP documented and tested |
| Training | Annual security awareness training records |

### Certification Audit Stages
**Stage 1 (Document Review):**
Auditor reviews ISMS documentation. Common findings: SoA incomplete, risk methodology not defined, scope too vague.

**Stage 2 (On-site/Remote Assessment):**
Auditor interviews staff, samples evidence, tests controls. Findings graded:
- **Major nonconformity**: Systematic failure, must be resolved before certification
- **Minor nonconformity**: Isolated gap, corrective action plan required
- **Observation**: Improvement opportunity, not blocking

### Common ISO 27001 Failures
- SoA excludes controls without justification
- Risk assessment not updated when new systems added
- Internal audit done by same team responsible for controls (not independent)
- Corrective actions from previous audit not closed
- Management review not documented (verbal reviews don't count)
- Supplier security not assessed for critical vendors

---

## GDPR Supervisory Authority Audit (EU DPA Audit)

### Triggers
- Data subject complaint
- Cross-border investigation
- Sector sweep
- Proactive audit (rare but increasing)

### What DPAs Examine
1. **ROPA** — complete? current? accessible within 72h?
2. **Lawful basis** — documented per processing activity? appropriate?
3. **Privacy notices** — transparent? in plain language? all required elements?
4. **Data subject request handling** — requests logged? responded within 30 days?
5. **Data transfers** — SCCs/adequacy? TIA for US transfers?
6. **Security measures** — appropriate to risk? tested? documented?
7. **Breach log** — all breaches logged? 72h notification met?
8. **DPO** — appointed where required? independent? sufficient resources?
9. **Processor contracts** — DPA signed with ALL processors?
10. **DPIA** — conducted for high-risk processing?

### Response Strategy
- Designate single point of contact for DPA communication
- Respond to all requests within statutory deadlines (varies by DPA)
- Never provide more than requested (scope creep creates liability)
- Legal counsel reviews all written responses to DPA
- Document every communication

### Evidence Package (Have Ready)
```
ROPA — latest version, signed by DPO
Privacy notice — all versions with effective dates
DSR log — all requests in past 2 years with response dates
Breach log — all incidents (notified + non-notified with justification)
DPA agreements — signed copies with all processors
Training records — staff handling personal data
DPIA reports — for any high-risk processing
Transfer documentation — SCCs, TIAs for non-EEA transfers
DPO appointment record and contact registration with supervisory authority
```

---

## HIPAA OCR Audit (US Office for Civil Rights)

### Triggers
- Breach report (> 500 affected)
- Patient complaint
- Desk audit (random selection from covered entities)
- Targeted investigation

### What OCR Audits
**Administrative safeguards:**
- Risk analysis completed and documented
- Risk management plan with timelines
- Workforce training records (annual minimum)
- Sanction policy applied consistently
- Access management procedures

**Physical safeguards:**
- Facility access controls
- Workstation policy and controls
- Device and media controls

**Technical safeguards:**
- Unique user IDs (no shared accounts)
- Automatic logoff
- Audit logs of ePHI access
- Transmission encryption

**Organizational requirements:**
- BAAs with all business associates
- Policies and procedures current and enforced

### OCR Response Protocol
1. Acknowledge receipt of audit notification within 10 days
2. Assign compliance officer as primary contact
3. Provide requested documentation within stated deadline (typically 10–14 days)
4. Legal counsel reviews all submissions
5. Do not volunteer information beyond the specific request

### Evidence Package
```
Risk analysis — most recent, signed
Risk management plan — current status of each action item
Training records — past 3 years, all workforce members
Sanction policy + any applied sanctions
Access control policy + user access logs
Audit logs showing ePHI access monitoring
BAAs — signed copies with all business associates
Incident log — all breaches + near-misses
Contingency plan — BCP/DRP tested
Policies and procedures — effective dates, review history
```

---

## Internal Audit

### Purpose
Independent, objective assurance that controls are operating effectively. Internal audit should report to Board/Audit Committee, not management.

### Audit Universe — Common Data Governance Scope
- Data classification compliance
- Access control effectiveness
- Data retention enforcement
- Third-party/vendor compliance
- Incident response capability
- Privacy program maturity
- Data quality controls

### Methodology
```
1. Planning
   - Define scope and objectives
   - Risk-based selection of audit areas
   - Stakeholder communication
   - Fieldwork schedule

2. Fieldwork
   - Request evidence (PBC list)
   - Interview control owners
   - Test controls (sampling + walkthrough)
   - Document findings with evidence

3. Reporting
   - Draft report to management for response
   - Management response: agree/disagree + remediation plan
   - Final report to Audit Committee

4. Follow-up
   - Track remediation of findings
   - Validate control fixes (re-test)
   - Report status to Audit Committee quarterly
```

### Finding Severity Ratings
| Rating | Definition | Response SLA |
|--------|-----------|-------------|
| Critical | Immediate risk of material loss, regulatory violation, or data breach | 30 days |
| High | Significant control gap, elevated risk | 60 days |
| Medium | Control weakness, limited risk | 90 days |
| Low | Improvement opportunity, minimal risk | 180 days |
| Observation | Advisory only, no control failure | No SLA |

### Audit Report Structure
```
Executive Summary (1 page — for Board)
  - Audit scope and period
  - Overall opinion (satisfactory / needs improvement / unsatisfactory)
  - Top 3 findings summary

Detailed Findings
  - Finding ID and title
  - Risk rating
  - Criteria (what should be true)
  - Condition (what we found)
  - Cause (why it happened)
  - Effect (impact if not fixed)
  - Recommendation (specific, actionable)
  - Management response + owner + due date

Appendix
  - Methodology
  - Scope limitations
  - Evidence index
```

---

## Pre-Audit Rapid Readiness Checklist

Run this 60 days before any audit:

```
Documentation:
- [ ] All policies reviewed and dated within 12 months
- [ ] ROPA current
- [ ] Risk register current
- [ ] Asset inventory current
- [ ] Evidence binder organized by control domain

Access:
- [ ] User access review completed in past quarter
- [ ] Terminated employee accounts verified removed
- [ ] Privileged access list reviewed
- [ ] MFA enforced for all admin accounts

Incidents:
- [ ] Incident log complete (no gaps)
- [ ] All breaches notified within regulatory timelines
- [ ] Post-incident reviews documented

Vendors:
- [ ] DPA/BAA signed with all processors
- [ ] Critical vendor SOC2 reports collected
- [ ] Annual vendor risk assessment completed

Training:
- [ ] Annual security awareness training completed (100% of staff)
- [ ] Specialist training for data stewards, DPO, security team
- [ ] Training records archived

Testing:
- [ ] BCP/DRP tested and results documented
- [ ] Penetration test completed (past 12 months)
- [ ] Vulnerability remediation within SLA
- [ ] Internal audit completed (ISO 27001 requirement)
```
