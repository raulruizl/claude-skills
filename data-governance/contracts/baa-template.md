# Business Associate Agreement (BAA) Template
# HIPAA 45 CFR §164.504(e) Compliant

> **LEGAL NOTICE:** This template is a starting point only. Always have qualified legal counsel review before execution. HIPAA requirements are strictly enforced; non-compliant BAAs expose both parties to significant penalties.

> **When to use:** Required under HIPAA before any Business Associate (vendor, contractor, subcontractor) receives, creates, maintains, or transmits Protected Health Information (PHI) on behalf of a Covered Entity. No PHI may be shared before a signed BAA is in place.

---

## Variables to Replace
- `[COVERED_ENTITY_NAME]` — Healthcare provider, health plan, or clearinghouse
- `[COVERED_ENTITY_ADDRESS]` — Registered address
- `[BA_NAME]` — Business Associate (vendor/service provider) name
- `[BA_ADDRESS]` — Business Associate registered address
- `[EFFECTIVE_DATE]` — Agreement effective date
- `[SERVICES_DESCRIPTION]` — Description of services BA provides to CE
- `[GOVERNING_STATE]` — State law governing the agreement

---

# BUSINESS ASSOCIATE AGREEMENT

This Business Associate Agreement ("Agreement") is entered into as of [EFFECTIVE_DATE] between:

**Covered Entity:** [COVERED_ENTITY_NAME], [COVERED_ENTITY_ADDRESS] ("CE")

**Business Associate:** [BA_NAME], [BA_ADDRESS] ("BA")

This BAA supplements and is incorporated into the underlying services agreement between the parties. In the event of conflict regarding PHI matters, this BAA controls.

---

## 1. DEFINITIONS

Terms used but not otherwise defined have the meanings given in HIPAA (45 CFR Parts 160 and 164).

"**PHI**" means Protected Health Information as defined in 45 CFR §160.103, limited to PHI that BA creates, receives, maintains, or transmits on behalf of CE.

"**ePHI**" means PHI in electronic form.

"**HIPAA Rules**" means the Privacy Rule (45 CFR Part 164, Subparts A and E), Security Rule (45 CFR Part 164, Subparts A and C), and Breach Notification Rule (45 CFR Part 164, Subpart D).

"**Breach**" has the meaning given in 45 CFR §164.402.

"**Subcontractor**" means a person who acts on behalf of BA, other than in the capacity of a member of BA's workforce.

---

## 2. OBLIGATIONS OF BUSINESS ASSOCIATE

### 2.1 Permitted Uses and Disclosures
BA may use or disclose PHI only:
(a) To perform functions, activities, or services for CE as specified in [SERVICES_DESCRIPTION];
(b) As required by law;
(c) As permitted or required by this Agreement;
(d) As otherwise permitted in writing by CE.

BA shall not use or disclose PHI in a manner that would violate the HIPAA Privacy Rule if done by CE, except as permitted in Sections 2.2 and 2.3.

### 2.2 BA's Own Operations (Permitted)
BA may use PHI for BA's own proper management and administration, or to carry out BA's legal responsibilities, provided:
(a) Uses are necessary; AND
(b) Disclosures are required by law, OR BA obtains reasonable assurances from the recipient of confidentiality and prompt breach notification.

### 2.3 Data Aggregation (if applicable)
☐ BA is **not** authorized to perform data aggregation services.
☐ BA is authorized to perform data aggregation services relating to CE's health care operations.

### 2.4 De-Identification
BA may de-identify PHI in accordance with 45 CFR §164.514(b). De-identified data is no longer PHI and is not subject to this Agreement.

---

## 3. SAFEGUARDS

### 3.1 Appropriate Safeguards (all PHI)
BA shall implement appropriate administrative, physical, and technical safeguards to prevent use or disclosure of PHI other than as provided in this Agreement.

### 3.2 Security Rule Compliance (ePHI)
BA shall comply with the HIPAA Security Rule (45 CFR Part 164, Subpart C) with respect to ePHI, including:

**Administrative Safeguards:**
- [ ] Security Management Process (risk analysis + risk management)
- [ ] Assigned Security Responsibility (designated Security Officer)
- [ ] Workforce Security (training, sanctions, termination procedures)
- [ ] Information Access Management (minimum necessary access)
- [ ] Security Awareness and Training (annual)
- [ ] Contingency Plan (backup, DR, emergency access)
- [ ] Evaluation (periodic technical and non-technical evaluations)

**Physical Safeguards:**
- [ ] Facility Access Controls
- [ ] Workstation Use and Security Policies
- [ ] Device and Media Controls (disposal, re-use, accountability)

**Technical Safeguards:**
- [ ] Access Control (unique user IDs, automatic logoff, encryption/decryption)
- [ ] Audit Controls (hardware/software activity logs)
- [ ] Integrity Controls (authentication of ePHI)
- [ ] Transmission Security (encryption in transit: TLS 1.2+ minimum)

### 3.3 Encryption Standards
- At rest: AES-256 (renders data unusable per HHS guidance — breach safe harbor applies)
- In transit: TLS 1.2 or higher
- Portable media: encrypted before any ePHI is stored

---

## 4. SUBCONTRACTORS

BA shall:
(a) Ensure any Subcontractor that creates, receives, maintains, or transmits PHI on behalf of BA executes a written agreement imposing obligations equivalent to this BAA **before** any PHI is shared;
(b) Ensure Subcontractors comply with the HIPAA Security Rule for ePHI;
(c) Remain fully liable to CE for Subcontractor's compliance failures.

Current Subcontractors handling PHI:
| Subcontractor | Service | BAA Executed Date |
|--------------|---------|-----------------|
| [Name] | [Service] | [Date] |

---

## 5. INDIVIDUAL RIGHTS

BA shall:
(a) **Access (§164.524):** Make PHI available to CE (or, at CE's direction, to the individual) for inspection and copying within **[30 days]** of CE's written request;
(b) **Amendment (§164.526):** Make PHI available for amendment and incorporate amendments as directed by CE;
(c) **Accounting of Disclosures (§164.528):** Document and provide CE with information necessary for CE to respond to individual requests for an accounting of disclosures;
(d) **Restriction Requests:** Notify CE of restriction requests BA receives directly from individuals within **[5 business days]**.

---

## 6. BREACH NOTIFICATION

### 6.1 Discovery and Notification
BA shall notify CE of a Breach of Unsecured PHI:
- **Timing:** Without unreasonable delay and **no later than 30 calendar days** after discovery
- BA treats Breach as discovered on the first day BA knew or should have known of the Breach

### 6.2 Content of Notification
BA's notification shall include, to the extent reasonably possible:
(a) Identification of individuals whose PHI was involved (name, address, DOB, SSN if used);
(b) Brief description of what happened (date of breach and discovery);
(c) Description of PHI types involved;
(d) Steps individuals should take to protect themselves;
(e) Brief description of what CE/BA is doing to investigate, mitigate, and prevent future breaches;
(f) Contact procedures for individuals to ask questions.

### 6.3 Breach Risk Assessment
Where BA determines an impermissible use or disclosure is not a Breach (4-factor risk assessment), BA shall document the risk assessment and provide it to CE upon request.

### 6.4 CE's Notification Obligations
CE is responsible for notifying:
- Affected individuals (within 60 days of discovery)
- HHS (within 60 days of discovery; annually if < 500 affected)
- Media (if > 500 residents in a state — within 60 days)

---

## 7. MINIMUM NECESSARY

BA shall make reasonable efforts to use, disclose, and request only the minimum PHI necessary to accomplish the intended purpose, consistent with 45 CFR §164.502(b).

---

## 8. REPORTING OBLIGATIONS

BA shall report to CE, **without unreasonable delay**:
(a) Any use or disclosure of PHI not provided for by this Agreement;
(b) Any Security Incident (attempted or successful unauthorized access, use, disclosure, modification, or destruction of ePHI);
(c) Any Breach of Unsecured PHI per Section 6.

For Security Incidents that constitute unsuccessful attempts (e.g., routine pings, port scans, failed logins), BA shall report the types and general frequency on a **[quarterly]** basis rather than individually.

---

## 9. AUDIT AND ACCESS RIGHTS

BA shall:
(a) Make its internal practices, books, and records relating to the use and disclosure of PHI available to the Secretary of HHS for purposes of determining CE's compliance with HIPAA;
(b) Make available to CE all records, policies, and procedures relating to PHI within **[10 business days]** of CE's written request;
(c) Permit CE (or CE's authorized agent) to audit BA's compliance with this Agreement upon **[30 days]** written notice, no more than **[once per calendar year]** (unless a Breach has occurred).

---

## 10. TERM AND TERMINATION

### 10.1 Term
This Agreement is effective as of [EFFECTIVE_DATE] and continues until the termination of the underlying services agreement, unless terminated earlier.

### 10.2 Termination for Cause
CE may terminate this Agreement and the underlying services agreement immediately upon written notice if:
(a) BA materially breaches this Agreement and fails to cure within **[30 days]** of written notice; OR
(b) CE reasonably determines that cure is not possible.

### 10.3 Return or Destruction of PHI
Upon termination:
(a) BA shall **return or destroy** all PHI (including copies held by Subcontractors) within **[30 days]**;
(b) BA shall provide written certification of return or destruction;
(c) If return or destruction is infeasible, BA shall extend protections of this Agreement to remaining PHI and limit further use or disclosure;
(d) Retained PHI remains subject to this Agreement indefinitely.

---

## 11. GOVERNING LAW

This Agreement is governed by the laws of the State of [GOVERNING_STATE] and applicable federal law (including HIPAA).

---

## 12. NO THIRD-PARTY BENEFICIARIES

Nothing in this Agreement confers any rights or remedies on individuals whose PHI is subject to this Agreement.

---

## 13. AMENDMENT

The parties agree to amend this Agreement as necessary to comply with changes in HIPAA Rules. Either party may request amendment; parties shall negotiate in good faith.

---

## SIGNATURES

**COVERED ENTITY**
Signed: _______________________
Name: _________________________
Title: _________________________
Date: _________________________
[COVERED_ENTITY_NAME]

**BUSINESS ASSOCIATE**
Signed: _______________________
Name: _________________________
Title: _________________________
Date: _________________________
[BA_NAME]
