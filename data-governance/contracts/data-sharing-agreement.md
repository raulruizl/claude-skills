# Data Sharing Agreement (DSA) Template

> **LEGAL NOTICE:** This template is a starting point only. Always have qualified legal counsel review before execution. Data sharing between organizations carries significant legal, privacy, and security obligations.

> **When to use:** When two or more organizations share data with each other for a defined purpose. Unlike a DPA (where one party controls and one processes), a DSA is used when both parties act as independent Controllers, or when sharing for joint purposes, research, or analytics.

> **Distinguish from DPA:** If Party B only processes data on behalf of Party A (no independent use), use a DPA instead.

---

## Variables to Replace
- `[PARTY_A_NAME]` — First organization (data provider / initiating party)
- `[PARTY_A_ADDRESS]` — Registered address
- `[PARTY_B_NAME]` — Second organization (data recipient)
- `[PARTY_B_ADDRESS]` — Registered address
- `[EFFECTIVE_DATE]` — Agreement effective date
- `[EXPIRY_DATE]` — Agreement end date (or "until terminated")
- `[GOVERNING_LAW]` — Jurisdiction

---

# DATA SHARING AGREEMENT

This Data Sharing Agreement ("Agreement") is entered into as of [EFFECTIVE_DATE] between:

**Party A:** [PARTY_A_NAME], [PARTY_A_ADDRESS] ("Party A")

**Party B:** [PARTY_B_NAME], [PARTY_B_ADDRESS] ("Party B")

Collectively referred to as the "Parties."

---

## 1. PURPOSE AND SCOPE

### 1.1 Purpose of Data Sharing
The Parties wish to share data for the following purpose(s) only:
[Describe specifically: e.g., "joint analytics to improve customer experience for customers of both parties" / "academic research under protocol IRB-XXXX" / "fraud detection across both platforms"]

**Permitted purposes are limited to those stated above. Any other use requires a separate written amendment.**

### 1.2 Data Shared

**Party A provides to Party B:**
| Dataset | Data Elements | Format | Frequency |
|---------|--------------|--------|-----------|
| [Name] | [Fields] | [CSV/API/etc.] | [Daily/weekly/one-time] |

**Party B provides to Party A (if reciprocal):**
| Dataset | Data Elements | Format | Frequency |
|---------|--------------|--------|-----------|
| [Name] | [Fields] | [CSV/API/etc.] | [Daily/weekly/one-time] |

### 1.3 Personal Data Involved
☐ This Agreement does not involve personal data — proceed without DPA requirements.
☐ This Agreement involves personal data — Sections 4–7 apply in full.

If personal data: specify categories of data subjects:
[e.g., customers, employees, research participants, website visitors]

---

## 2. PERMITTED USE

### 2.1 Recipient's Permitted Uses
Each Party receiving data from the other ("Recipient") may only:
(a) Use the data for the purposes stated in Section 1.1;
(b) Access data on a need-to-know basis within its organization;
(c) Use data to create Derived Data (aggregated, anonymized outputs) as specified in Section 2.2.

### 2.2 Derived Data
Recipient may create Derived Data (statistical analyses, aggregated insights, anonymized outputs) subject to:
(a) Derived Data must not be capable of identifying individuals;
(b) Derived Data is owned by the creating Party unless otherwise agreed in Schedule 1;
(c) Raw input data underlying Derived Data remains subject to all restrictions in this Agreement.

### 2.3 Prohibited Uses
Recipient shall NOT:
(a) Sell, license, or transfer the shared data to any third party;
(b) Use the data for any purpose not specified in Section 1.1;
(c) Combine the data with other datasets in a way that re-identifies de-identified data;
(d) Use the data for training machine learning models without explicit written consent;
(e) Use the data for advertising targeting without explicit written consent;
(f) Retain the data beyond the period specified in Section 8.

---

## 3. DATA QUALITY AND ACCURACY

### 3.1 Provider Obligations
Each Party providing data ("Provider") warrants that:
(a) It has the legal right to share the data with Recipient for the stated purposes;
(b) The data is accurate, complete, and current as of the transfer date to the best of Provider's knowledge;
(c) All required consents, lawful bases, or authorizations are in place for the sharing;
(d) It will promptly notify Recipient of any material inaccuracies discovered after sharing.

### 3.2 No Warranty on Fitness
Provider makes no warranty that the data is fit for Recipient's specific analytical or operational purposes beyond what is stated in this Agreement.

---

## 4. DATA PROTECTION AND PRIVACY (if personal data)

### 4.1 Independent Controllers
Where both Parties determine the purposes and means of processing shared personal data, each Party acts as an independent Controller with respect to its own processing activities. Each Party is independently responsible for compliance with Applicable Data Protection Law.

### 4.2 Joint Controllers (if applicable)
☐ Not applicable — Parties are independent Controllers.
☐ Parties are Joint Controllers under GDPR Art. 26 for the following processing:
[Describe joint processing activity]

If Joint Controllers, a separate Joint Controller Agreement (JCA) must be executed and made available to data subjects. Parties shall agree which is the primary point of contact for data subjects.

### 4.3 Lawful Basis
Each Party confirms it has documented a lawful basis for sharing and receiving the personal data:
- Party A lawful basis: [e.g., legitimate interests / consent / contract]
- Party B lawful basis: [e.g., legitimate interests / consent / contract]

### 4.4 Privacy Notice
Each Party shall ensure its privacy notice accurately describes the data sharing contemplated by this Agreement prior to the first data transfer.

### 4.5 Data Subject Rights
Each Party is responsible for responding to data subject rights requests relating to its own processing. Where a request requires cooperation (e.g., deletion of data already shared), Parties shall cooperate promptly.

If data subject exercises erasure right: Recipient must delete the relevant records within **[30 days]** of notification.

---

## 5. SECURITY

### 5.1 Security Standards
Each Party shall implement appropriate technical and organizational security measures, including at minimum:
- Encryption in transit: TLS 1.2+ for all data transfers
- Encryption at rest: AES-256 for all stored shared data
- Access control: role-based, least privilege, MFA for administrative access
- Logging: access to shared data logged and retained for minimum [12 months]
- Vulnerability management: regular scanning and patching

### 5.2 Transfer Mechanism
Shared data shall be transferred only via:
☐ Encrypted SFTP (PGP encrypted files)
☐ Secure API (mutual TLS)
☐ Encrypted cloud storage ([specify provider + bucket/container])
☐ Other: [specify]

No data shall be transferred via unencrypted email or unencrypted file transfer.

### 5.3 Access Controls
Recipient shall restrict access to shared data to personnel who:
(a) Require access for the permitted purposes;
(b) Are bound by confidentiality obligations; and
(c) Have received appropriate data protection training.

Maximum number of authorized users: [specify or "minimum necessary"]

---

## 6. INCIDENT AND BREACH NOTIFICATION

Each Party shall notify the other:
(a) Of any actual or suspected security incident affecting shared data **within 24 hours** of discovery;
(b) Of any confirmed Personal Data Breach **within 48 hours** of confirmation;
(c) Notification shall include: nature of incident, data affected, number of subjects potentially affected, and remediation steps taken.

Each Party is independently responsible for regulatory breach notifications to Supervisory Authorities and data subjects relating to its own processing, but shall cooperate to allow the other Party to meet its notification deadlines.

---

## 7. INTERNATIONAL DATA TRANSFERS

Data shall only be transferred across international borders via:
☐ Adequacy decision (specify country/decision): ___________
☐ Standard Contractual Clauses (EU SCCs — attached as Appendix [X])
☐ Binding Corporate Rules
☐ Not applicable — all processing within EEA/UK/USA

---

## 8. DATA RETENTION AND DELETION

### 8.1 Retention Period
Recipient shall retain shared data for no longer than:
[Specify: e.g., "12 months from date of receipt" / "duration of the joint project" / "as required by law, and no longer"]

### 8.2 Deletion
Upon expiry of the retention period or termination of this Agreement (whichever is earlier), Recipient shall:
(a) Securely delete all shared data (including backup copies);
(b) Ensure deletion from all systems including analytics platforms and data warehouses;
(c) Provide written certification of deletion within **[30 days]** of deletion completion;
(d) Derived Data that cannot identify individuals may be retained.

---

## 9. INTELLECTUAL PROPERTY

### 9.1 Ownership
Each Party retains all intellectual property rights in the data it provides. This Agreement does not transfer ownership of any data.

### 9.2 License Grant
Each Provider grants Recipient a limited, non-exclusive, non-transferable, revocable license to use the shared data solely for the purposes stated in Section 1.1 and for the duration of this Agreement.

---

## 10. CONFIDENTIALITY

Each Party shall treat the other's shared data as confidential. Neither Party shall disclose shared data to third parties without prior written consent, except:
(a) To employees/contractors who need access for permitted purposes and are bound by confidentiality;
(b) As required by law, regulation, or court order (with prompt prior notice where legally permitted).

Confidentiality obligations survive termination of this Agreement for **[5 years]**.

---

## 11. LIABILITY

### 11.1 Each Party is liable for its own regulatory fines, penalties, and third-party claims arising from its own breaches of data protection law or this Agreement.

### 11.2 Neither Party is liable for the other's non-compliance with Applicable Data Protection Law.

### 11.3 Maximum liability of either Party to the other under this Agreement: **[specify cap or "as per Main Agreement"]**.

---

## 12. TERM AND TERMINATION

### 12.1 Term
This Agreement is effective from [EFFECTIVE_DATE] until [EXPIRY_DATE / "terminated by either party"].

### 12.2 Termination
Either Party may terminate this Agreement:
(a) For convenience, with **[30 days]** written notice;
(b) Immediately upon written notice if the other Party materially breaches this Agreement and fails to cure within **[14 days]**.

### 12.3 Effect of Termination
On termination: (a) all data sharing ceases immediately; (b) Section 8.2 deletion obligations apply; (c) Sections 10 (confidentiality), 11 (liability), and 13 (governing law) survive.

---

## 13. GOVERNING LAW AND DISPUTES

This Agreement is governed by the laws of [GOVERNING_LAW]. Disputes shall first be attempted to be resolved by senior management of each Party within [30 days]. If unresolved, disputes shall be submitted to [arbitration in [city] under [rules] / courts of [jurisdiction]].

---

## SCHEDULES

**Schedule 1 — Derived Data Ownership (if applicable)**
[Specify any special ownership arrangements for derived/combined outputs]

**Schedule 2 — Security Assessment**
[Attach or reference most recent security assessments, SOC2 reports, or pen test summaries]

**Schedule 3 — Standard Contractual Clauses (if applicable)**

---

## SIGNATURES

**PARTY A**
Signed: _______________________
Name: _________________________
Title: _________________________
Date: _________________________
[PARTY_A_NAME]

**PARTY B**
Signed: _______________________
Name: _________________________
Title: _________________________
Date: _________________________
[PARTY_B_NAME]
