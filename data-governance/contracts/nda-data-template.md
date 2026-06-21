# Non-Disclosure Agreement (NDA) — Data-Focused Template

> **LEGAL NOTICE:** This template is a starting point only. Always have qualified legal counsel review before execution. NDA enforceability varies by jurisdiction.

> **When to use:** Before sharing confidential data, system architecture, technical specifications, or proprietary datasets with a third party (partner, vendor, potential acquirer, researcher, contractor). Use BEFORE sharing any sensitive information — even in early discussions.

> **Mutual vs One-Way:**
> - **Mutual (bilateral):** Both parties share confidential information. Use for partnerships, joint ventures, M&A discussions.
> - **One-way (unilateral):** Only one party shares. Use when hiring a contractor, vendor evaluation, or sharing data for a specific purpose.

---

## Variables to Replace
- `[DISCLOSING_PARTY]` — Party sharing the confidential information
- `[RECEIVING_PARTY]` — Party receiving the confidential information
- `[DISCLOSING_ADDRESS]` / `[RECEIVING_ADDRESS]` — Registered addresses
- `[EFFECTIVE_DATE]` — Agreement start date
- `[PURPOSE]` — Specific reason for sharing (be precise)
- `[NDA_TERM]` — Duration of NDA (e.g., "2 years", "3 years")
- `[CONFIDENTIALITY_SURVIVAL]` — How long obligations survive after NDA ends (e.g., "3 years", "indefinitely for trade secrets")
- `[GOVERNING_STATE]` — State/jurisdiction for governing law

---

# NON-DISCLOSURE AGREEMENT

This Non-Disclosure Agreement ("Agreement") is entered into as of [EFFECTIVE_DATE] between:

**Disclosing Party:** [DISCLOSING_PARTY], [DISCLOSING_ADDRESS]

**Receiving Party:** [RECEIVING_PARTY], [RECEIVING_ADDRESS]

*(For mutual NDA: each Party may be both Disclosing Party and Receiving Party with respect to their own Confidential Information.)*

---

## 1. PURPOSE

The Parties wish to explore or engage in the following:
**[PURPOSE]**
(the "Purpose")

In connection with the Purpose, Disclosing Party may share Confidential Information with Receiving Party. This Agreement governs the protection of that information.

---

## 2. DEFINITION OF CONFIDENTIAL INFORMATION

### 2.1 Confidential Information Includes
"Confidential Information" means any information disclosed by Disclosing Party to Receiving Party in connection with the Purpose, including:

**Data and Datasets:**
- Proprietary datasets, databases, data models, schemas
- Customer data, user data, behavioral data, transaction records
- Personal data (subject to applicable data protection law)
- Training data, labeled datasets, model weights
- Analytical outputs, insights, benchmarks

**Technical Information:**
- System architecture, infrastructure design, API specifications
- Source code, algorithms, software, technical documentation
- Security configurations, vulnerability assessments, penetration test reports
- Encryption keys, access credentials (note: sharing credentials is discouraged — use secrets management)

**Business Information:**
- Business plans, financial projections, pricing
- Customer lists, partner relationships, contracts
- Intellectual property, trade secrets
- Research and development plans

### 2.2 Marking
Confidential Information may be:
(a) Marked "CONFIDENTIAL", "PROPRIETARY", or similar; OR
(b) Identified as confidential at time of oral disclosure, confirmed in writing within **[10 business days]**; OR
(c) Of a nature that a reasonable person would understand it to be confidential.

### 2.3 Exclusions
Confidential Information does NOT include information that:
(a) Is or becomes publicly known through no breach by Receiving Party;
(b) Was rightfully known to Receiving Party before disclosure (documented evidence required);
(c) Is rightfully received from a third party without restriction;
(d) Is independently developed by Receiving Party without use of Confidential Information (documented evidence required);
(e) Is required to be disclosed by law, regulation, or court order — Receiving Party shall give prompt written notice to Disclosing Party and cooperate in seeking protective order.

---

## 3. OBLIGATIONS OF RECEIVING PARTY

Receiving Party shall:
(a) **Protect** Confidential Information with at least the same degree of care it uses for its own confidential information, and no less than reasonable care;
(b) **Use** Confidential Information solely for the Purpose;
(c) **Restrict access** to personnel who have a need to know for the Purpose and are bound by confidentiality obligations no less protective than this Agreement;
(d) **Not disclose** Confidential Information to any third party without prior written consent;
(e) **Not copy or reproduce** Confidential Information except as necessary for the Purpose;
(f) **Promptly notify** Disclosing Party upon discovering any unauthorized use or disclosure;
(g) **Cooperate** in any reasonable steps to prevent further unauthorized disclosure.

---

## 4. DATA PROTECTION OBLIGATIONS

Where Confidential Information includes personal data:

### 4.1 Compliance
Each Party shall comply with all Applicable Data Protection Laws (including GDPR, CCPA/CPRA, HIPAA where applicable) with respect to personal data disclosed under this Agreement.

### 4.2 No Independent Processing
Receiving Party shall not process personal data included in Confidential Information for any purpose other than the Purpose, and shall not combine it with other data to re-identify individuals.

### 4.3 Security Measures
Receiving Party shall implement appropriate technical and organizational security measures for personal data, including:
- Encryption at rest (AES-256) and in transit (TLS 1.2+)
- Access controls and audit logging
- Incident response capability

### 4.4 Breach Notification
Receiving Party shall notify Disclosing Party within **24 hours** of discovering any actual or suspected security incident affecting personal data shared under this Agreement.

### 4.5 Supplemental Agreements
If the Parties determine that a Data Processing Agreement (DPA) or Data Sharing Agreement (DSA) is required under applicable data protection law, the Parties shall execute such agreement before any personal data is transferred.

---

## 5. PERMITTED DISCLOSURES

Receiving Party may disclose Confidential Information to:
(a) Its employees, directors, officers who need to know for the Purpose, provided they are bound by confidentiality obligations at least as protective as this Agreement;
(b) Its professional advisors (lawyers, accountants) under professional duty of confidentiality;
(c) As required by law, court order, or regulatory requirement (subject to Section 2.3(e)).

Receiving Party remains liable for any breach by persons to whom it discloses Confidential Information.

---

## 6. NO LICENSE

Nothing in this Agreement grants Receiving Party any license, right, or interest in Disclosing Party's intellectual property, data, or Confidential Information except the limited right to use it for the Purpose during the term of this Agreement.

---

## 7. RETURN AND DESTRUCTION

Upon written request from Disclosing Party or upon termination of this Agreement:
(a) Receiving Party shall promptly **return or destroy** all Confidential Information and copies thereof;
(b) Receiving Party shall provide written certification of destruction within **[10 business days]**;
(c) Receiving Party may retain one archival copy solely for legal compliance purposes, subject to continued application of this Agreement's obligations;
(d) Receiving Party's counsel may retain copies of documents subject to attorney-client privilege.

---

## 8. TERM

### 8.1 Agreement Term
This Agreement is effective from [EFFECTIVE_DATE] for a period of **[NDA_TERM]**, unless terminated earlier by mutual written agreement.

### 8.2 Survival of Obligations
Confidentiality obligations survive termination for **[CONFIDENTIALITY_SURVIVAL]** with respect to all Confidential Information disclosed during the Agreement term.

Trade secrets are protected for as long as they qualify as trade secrets under applicable law, regardless of Agreement term.

---

## 9. REMEDIES

### 9.1 Injunctive Relief
Receiving Party acknowledges that any breach of this Agreement would cause irreparable harm to Disclosing Party for which monetary damages would be inadequate. Disclosing Party shall be entitled to seek injunctive or other equitable relief in any court of competent jurisdiction without the requirement to post bond.

### 9.2 Damages
In addition to injunctive relief, Disclosing Party may seek all available legal remedies, including monetary damages.

---

## 10. GENERAL

### 10.1 No Obligation
This Agreement does not obligate either Party to disclose any information, enter into any business relationship, or conclude any transaction.

### 10.2 No Warranty
Disclosing Party makes no representation or warranty regarding the accuracy, completeness, or fitness for purpose of Confidential Information.

### 10.3 Entire Agreement
This Agreement constitutes the entire agreement between the Parties regarding confidentiality of information shared for the Purpose and supersedes all prior agreements on the same subject.

### 10.4 Amendment
No amendment is effective unless in writing signed by both Parties.

### 10.5 Waiver
Failure to enforce any provision is not a waiver of future enforcement.

### 10.6 Severability
If any provision is unenforceable, the remaining provisions continue in full force.

### 10.7 Assignment
Neither Party may assign this Agreement without prior written consent of the other Party, except in connection with a merger, acquisition, or sale of substantially all assets.

---

## 11. GOVERNING LAW AND JURISDICTION

This Agreement is governed by the laws of the State of [GOVERNING_STATE] without regard to conflict of law principles. The Parties consent to the exclusive jurisdiction of the state and federal courts located in [GOVERNING_STATE] for disputes arising under this Agreement.

---

## SIGNATURES

**DISCLOSING PARTY**
Signed: _______________________
Name: _________________________
Title: _________________________
Date: _________________________
[DISCLOSING_PARTY]

**RECEIVING PARTY**
Signed: _______________________
Name: _________________________
Title: _________________________
Date: _________________________
[RECEIVING_PARTY]

---

## APPENDIX A — DESCRIPTION OF CONFIDENTIAL INFORMATION SHARED

*(Optional but recommended: list specific datasets, systems, or documents being shared under this NDA)*

| Item | Format | Classification | Sensitivity |
|------|--------|----------------|-------------|
| [Dataset/document name] | [Format] | [Confidential/Restricted] | [Reason sensitive] |
