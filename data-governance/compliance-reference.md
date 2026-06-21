# Compliance Reference — GDPR, CCPA/CPRA, HIPAA, SOX

## GDPR — General Data Protection Regulation (EU 2016/679)

### Scope
Applies to any organization processing personal data of EU/EEA residents, regardless of where the org is based.

### Key Definitions
- **Personal data**: Any info relating to identified/identifiable natural person
- **Special category data**: Race, ethnicity, political opinions, religion, union membership, health, biometric, sexual orientation — requires explicit consent or specific exemptions
- **Controller**: Decides purpose and means of processing
- **Processor**: Processes on behalf of controller
- **DPO**: Data Protection Officer — mandatory for public authorities, large-scale systematic monitoring, large-scale special category processing

### Lawful Bases (Art. 6) — Must document ONE per processing activity
| Basis | When to use |
|-------|-------------|
| Consent | Freely given, specific, informed, unambiguous. Can be withdrawn. Not for employment (power imbalance) |
| Contract | Processing necessary to perform contract with the data subject |
| Legal obligation | Required by EU/member state law |
| Vital interests | Life-threatening emergency |
| Public task | Official authority / public interest |
| Legitimate interests | Org's interest that doesn't override subject's rights — requires LIA (Legitimate Interest Assessment) |

### Key Articles
| Article | Requirement |
|---------|------------|
| Art. 5 | Principles: lawfulness, fairness, transparency, purpose limitation, minimization, accuracy, storage limitation, integrity, accountability |
| Art. 13/14 | Privacy notices — what to tell subjects at collection |
| Art. 17 | Right to erasure ("right to be forgotten") |
| Art. 20 | Data portability |
| Art. 25 | Privacy by design and by default |
| Art. 28 | Data Processing Agreement (DPA) required with all processors |
| Art. 30 | ROPA — Record of Processing Activities |
| Art. 32 | Technical + organizational security measures |
| Art. 33 | Breach notification to supervisory authority — 72 HOURS from awareness |
| Art. 34 | Breach notification to subjects — when high risk to rights and freedoms |
| Art. 35 | DPIA required for high-risk processing |
| Art. 37 | DPO designation |
| Art. 44–49 | Third-country transfers — adequacy decision, SCCs, BCRs, or derogations |

### Third-Country Transfers
- **Adequacy decision**: EU Commission approves country (UK, Canada, Japan, etc.)
- **SCCs**: Standard Contractual Clauses — use when no adequacy decision (e.g., USA)
- **BCRs**: Binding Corporate Rules — for multinational group internal transfers
- **After Schrems II**: Must conduct Transfer Impact Assessment (TIA) for US transfers

### Breach Notification (Art. 33/34)
```
T+0: Awareness of breach
T+72h: Notify supervisory authority (DPA) — even if incomplete info, update later
T+ASAP: Notify affected subjects if high risk
Required content:
  - Nature of breach
  - Categories + approximate number of subjects/records
  - DPO contact details
  - Likely consequences
  - Measures taken/proposed
```

### Penalties
- Up to €20M or 4% of global annual turnover (whichever higher) — serious violations
- Up to €10M or 2% — administrative violations (ROPA, DPO, DPIA)

### GDPR Audit Evidence Checklist
- [ ] ROPA current and complete
- [ ] Lawful basis documented per processing activity
- [ ] Privacy notices published (website, app, point of collection)
- [ ] DPA signed with all processors and sub-processors
- [ ] Data subject request log with response times
- [ ] DPIA conducted for high-risk processing
- [ ] Transfer mechanism documented for any non-EEA transfers
- [ ] Breach log (including near-misses)
- [ ] DPO appointed (if required) and registered with supervisory authority
- [ ] Training records for staff handling personal data
- [ ] Consent records (if consent used as lawful basis)

---

## CCPA / CPRA — California Consumer Privacy Act + California Privacy Rights Act

### Scope
Applies to for-profit businesses that:
- Have gross annual revenue > $25M, OR
- Buy/sell/share personal information of 100,000+ consumers or households, OR
- Derive 50%+ of revenue from selling/sharing personal information
AND do business in California or collect data of California residents

### CPRA Additions (effective Jan 2023)
- Sensitive Personal Information (SPI) category with opt-out right
- Right to correct
- Data minimization + purpose limitation obligations
- California Privacy Protection Agency (CPPA) enforcement

### Consumer Rights
| Right | Deadline | Notes |
|-------|----------|-------|
| Know (categories + specific pieces) | 45 days (+45 extension) | Free twice per year |
| Delete | 45 days (+45 extension) | With exceptions (legal obligation, security research, etc.) |
| Opt-out of sale/sharing | 15 business days | Must honor Global Privacy Control (GPC) signal |
| Non-discrimination | Immediate | Cannot deny service for exercising rights |
| Correct | 45 days (+45 extension) | CPRA addition |
| Limit use of SPI | 15 business days | CPRA addition |
| Data portability | 45 days | Machine-readable format |

### Sensitive Personal Information (CPRA)
SSN, driver's license, financial account + credentials, precise geolocation, racial/ethnic origin, religious beliefs, union membership, mail/email/text content, genetic/biometric data, health data, sexual orientation/gender identity

### Required Documentation
- [ ] Privacy Policy updated with CCPA/CPRA disclosures
- [ ] "Do Not Sell or Share My Personal Information" link on homepage
- [ ] Consumer request intake mechanism
- [ ] Response log with timestamps
- [ ] Contracts with service providers (equivalent to DPA) prohibiting sale of data
- [ ] Data inventory mapping CA resident data
- [ ] GPC signal honored in all digital properties

### Penalties
- $2,500 per unintentional violation
- $7,500 per intentional violation
- Private right of action for data breaches: $100–$750 per consumer per incident

---

## HIPAA — Health Insurance Portability and Accountability Act (USA)

### Scope
Covered Entities: healthcare providers, health plans, healthcare clearinghouses
Business Associates (BA): any vendor receiving PHI on behalf of covered entity — must sign BAA

### PHI — Protected Health Information
Individually identifiable health information in any medium (electronic, paper, oral).
18 identifiers that make health info PHI (name, DOB, address, phone, SSN, MRN, etc.)

### Three Rules

**Privacy Rule**
- Minimum necessary standard: disclose only PHI needed for purpose
- Patient rights: access, amendment, accounting of disclosures, restrict disclosures
- Permitted uses without authorization: treatment, payment, operations, public health
- Required authorization for: marketing, sale of PHI, most research

**Security Rule (ePHI only)**
| Safeguard | Examples |
|-----------|---------|
| Administrative | Security officer, workforce training, risk analysis, contingency plan |
| Physical | Facility access controls, workstation security, device controls |
| Technical | Access controls, audit controls, integrity controls, transmission security (TLS) |

**Breach Notification Rule**
- Covered Entity → HHS: 60 days after discovery (< 500 affected: annual log)
- Covered Entity → HHS: < 60 days if > 500 in a state → media notice required
- Covered Entity → Individuals: 60 days
- BA → Covered Entity: 60 days (covered entity owns breach notification)

### BAA — Business Associate Agreement
Required before ANY PHI sharing with vendors. Must include:
- Permitted uses of PHI
- Safeguard requirements
- Breach reporting obligation
- Return/destruction of PHI at contract end
- Sub-contractor BAA chain

### HIPAA Audit Evidence Checklist
- [ ] Risk Analysis completed and documented (annual)
- [ ] Risk Management Plan with mitigation timeline
- [ ] Policies and procedures current (reviewed annually)
- [ ] Workforce training records (annual)
- [ ] BAAs signed with all business associates
- [ ] Sanction policy in place and enforced
- [ ] Access control audit log (who accessed which PHI, when)
- [ ] Incident log including near-misses
- [ ] Contingency plan tested (backup + DR)
- [ ] Physical access controls documented

### Penalties (2023 tiers)
| Tier | Per violation | Annual cap |
|------|--------------|-----------|
| Did not know | $100–$50,000 | $1,919,173 |
| Reasonable cause | $1,000–$50,000 | $1,919,173 |
| Willful neglect — corrected | $10,000–$50,000 | $1,919,173 |
| Willful neglect — not corrected | $50,000 | $1,919,173 |

---

## SOX — Sarbanes-Oxley Act (USA, Public Companies)

### Scope
US public companies + their subsidiaries. Foreign private issuers filing with SEC.

### Key Sections

**Section 302 — CEO/CFO Certification**
Officers must certify quarterly/annual reports are accurate and that internal controls have been evaluated and any deficiencies disclosed.

**Section 404 — Internal Controls over Financial Reporting (ICFR)**
- Management assessment of ICFR effectiveness (every annual report)
- External auditor attestation (large accelerated filers)
- Framework used: COSO 2013

**Section 802 — Records Retention**
Criminal penalties for altering, destroying, mutilating records with intent to obstruct federal investigation.

### Data Governance Obligations Under SOX
- Financial data must be accurate, complete, and auditable
- Retention: 7 years for audit workpapers, financial records
- Access controls on financial systems must be documented and tested
- Change management for financial systems must be controlled and logged
- Segregation of duties in financial data processing

### IT General Controls (ITGC) — What SOX Auditors Test
| Control Domain | What is tested |
|---------------|---------------|
| Access Management | User provisioning/deprovisioning, privileged access, password policy, MFA |
| Change Management | Authorized changes to financial systems, testing before deployment, emergency change process |
| Computer Operations | Batch job monitoring, backup and recovery, incident management |
| System Development | SDLC controls, security in development, acceptance testing |

### SOX Audit Evidence Checklist
- [ ] COSO framework documented and adopted
- [ ] Risk assessment of financial reporting risks
- [ ] Control matrix (RCM — Risk Control Matrix) current
- [ ] Evidence of control operation (screenshots, exports, logs) for audit period
- [ ] User access reviews completed quarterly
- [ ] Privileged access logged and reviewed
- [ ] Change tickets for all financial system changes
- [ ] Segregation of duties enforced (no one person can initiate + approve + record transaction)
- [ ] Financial data retention policy enforced (7 years)
- [ ] Management's written assessment signed by CEO + CFO
