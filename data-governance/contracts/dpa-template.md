# Data Processing Agreement (DPA) Template
# GDPR Article 28 Compliant

> **LEGAL NOTICE:** This template is a starting point only. Always have qualified legal counsel review before execution. Requirements vary by jurisdiction and specific processing context.

> **When to use:** Required under GDPR Art. 28 whenever a Controller engages a Processor to process personal data on its behalf. Must be signed BEFORE any personal data is shared.

---

## Variables to Replace
- `[CONTROLLER_NAME]` — Company name of the data controller
- `[CONTROLLER_ADDRESS]` — Registered address of controller
- `[CONTROLLER_COUNTRY]` — Controller's country
- `[PROCESSOR_NAME]` — Company name of the data processor (vendor/service provider)
- `[PROCESSOR_ADDRESS]` — Registered address of processor
- `[PROCESSOR_COUNTRY]` — Processor's country
- `[EFFECTIVE_DATE]` — Date agreement comes into force
- `[GOVERNING_LAW]` — Jurisdiction for disputes (e.g., "England and Wales", "State of Delaware")
- `[MAIN_AGREEMENT]` — Name/date of the underlying service agreement this DPA supplements

---

# DATA PROCESSING AGREEMENT

This Data Processing Agreement ("DPA") is entered into as of [EFFECTIVE_DATE] by and between:

**Controller:**
[CONTROLLER_NAME]
[CONTROLLER_ADDRESS]
("Controller")

**Processor:**
[PROCESSOR_NAME]
[PROCESSOR_ADDRESS]
("Processor")

This DPA supplements and forms part of [MAIN_AGREEMENT] between the parties ("Main Agreement"). In the event of conflict, this DPA prevails with respect to data protection matters.

---

## 1. DEFINITIONS

"**Applicable Data Protection Law**" means (a) Regulation (EU) 2016/679 (GDPR) and any national implementing legislation; (b) the UK GDPR and Data Protection Act 2018 (where applicable); and (c) any other data protection or privacy laws applicable to the processing described herein.

"**Personal Data**", "**Processing**", "**Data Subject**", "**Controller**", "**Processor**", "**Sub-Processor**", "**Supervisory Authority**", and "**Personal Data Breach**" have the meanings given in Applicable Data Protection Law.

"**Services**" means the services provided by Processor under the Main Agreement.

---

## 2. PROCESSING DETAILS (Schedule 1)

### 2.1 Subject Matter
Processing of personal data in connection with Processor's provision of [describe services] to Controller.

### 2.2 Duration
For the term of the Main Agreement plus any post-termination retention period specified in Section 9.

### 2.3 Nature and Purpose of Processing
[Describe: e.g., storage and retrieval of customer data to support CRM functionality]

### 2.4 Type of Personal Data
[List: e.g., name, email address, phone number, purchase history, IP address]

### 2.5 Categories of Data Subjects
[List: e.g., Controller's customers, employees, website visitors]

### 2.6 Special Category Data
☐ No special category data processed under this DPA
☐ Yes — specify: [health data / biometric / racial origin / etc.]
If yes, additional safeguards apply per Section 6.

---

## 3. CONTROLLER OBLIGATIONS

Controller shall:
(a) Ensure a valid lawful basis exists for all personal data provided to Processor for processing;
(b) Provide Processor with complete and accurate instructions for processing;
(c) Ensure all data subject rights requests are directed to Controller in the first instance;
(d) Comply with all obligations under Applicable Data Protection Law applicable to Controllers.

---

## 4. PROCESSOR OBLIGATIONS

Processor shall:

**(a) Instructions only:** Process personal data solely on documented instructions from Controller, unless required by applicable law (in which case Processor shall inform Controller before processing, unless prohibited by law).

**(b) Confidentiality:** Ensure all personnel authorized to process personal data are bound by confidentiality obligations (contractual or statutory).

**(c) Security:** Implement appropriate technical and organizational measures per Section 6.

**(d) Sub-processors:** Comply with Section 7 regarding sub-processors.

**(e) Data subject rights:** Assist Controller in responding to data subject requests within Controller's response deadlines, taking into account the nature of the processing.

**(f) Controller compliance:** Assist Controller in ensuring compliance with Arts. 32–36 GDPR (security, breach notification, DPIA, prior consultation), taking into account the nature of processing and information available to Processor.

**(g) Deletion/return:** Delete or return all personal data as per Section 9 on termination.

**(h) Audit:** Make available all information necessary to demonstrate compliance with this DPA and contribute to audits per Section 10.

**(i) Notification of illegal instructions:** Immediately inform Controller if Processor believes an instruction infringes Applicable Data Protection Law.

---

## 5. DATA SUBJECT RIGHTS

Processor shall:
(a) Notify Controller within **3 business days** of receiving a data subject request directly;
(b) Not respond to data subject requests directly unless authorized in writing by Controller or required by law;
(c) Provide Controller with all information, access, and assistance reasonably required to respond to data subject requests within applicable deadlines:
  - GDPR: 30 days (extendable to 90 days with notice)
  - CCPA: 45 days (extendable to 90 days with notice)

---

## 6. SECURITY MEASURES

### 6.1 Technical and Organizational Measures (TOMs)
Processor implements and maintains security measures appropriate to the risk, including as a minimum:

| Measure | Implementation |
|---------|---------------|
| Encryption in transit | TLS 1.2+ for all data transfers |
| Encryption at rest | AES-256 for all stored personal data |
| Access control | Role-based access, least privilege, MFA for privileged accounts |
| Pseudonymization | Applied where appropriate to reduce risk |
| Resilience | Regular backups, tested recovery procedures, availability SLA: [X]% |
| Testing | Annual penetration testing, quarterly vulnerability scans |
| Incident monitoring | 24/7 monitoring with defined escalation procedures |

### 6.2 Special Category Data (if applicable)
Additional safeguards for special category data:
- Explicit documented authorization required for access
- Enhanced encryption and access logging
- Staff with access subject to enhanced vetting
- Data minimization strictly enforced

### 6.3 Changes to Security Measures
Processor shall not reduce the overall level of security during the DPA term without prior written consent from Controller.

---

## 7. SUB-PROCESSORS

### 7.1 Authorization
Controller provides **general written authorization** for Processor to engage sub-processors, subject to:
(a) Processor maintaining an up-to-date list of sub-processors (Schedule 2);
(b) Processor notifying Controller of any intended addition or replacement of sub-processors with **[30] days** prior written notice;
(c) Controller having the right to object to new sub-processors within **[14] days** of notification.

### 7.2 Sub-Processor Obligations
Processor shall impose data protection obligations on sub-processors equivalent to those in this DPA. Processor remains fully liable to Controller for sub-processor performance.

### 7.3 Current Sub-Processors (Schedule 2)
| Sub-Processor | Location | Processing Activity | Legal Mechanism |
|--------------|----------|--------------------|----|
| [Name] | [Country] | [What they do] | [SCCs/Adequacy/etc.] |

---

## 8. INTERNATIONAL DATA TRANSFERS

### 8.1 Restricted Transfers
Processor shall not transfer personal data to a country outside the EEA/UK unless:
(a) An adequacy decision applies;
(b) Appropriate safeguards are in place (Standard Contractual Clauses — EU 2021/914 or UK IDTA);
(c) A derogation under Art. 49 GDPR applies.

### 8.2 Where Processor is established outside the EEA/UK
The EU Standard Contractual Clauses (Module 2: Controller to Processor) are incorporated by reference as Schedule 3.

---

## 9. PERSONAL DATA BREACH NOTIFICATION

Processor shall:
(a) Notify Controller of a confirmed or suspected Personal Data Breach without undue delay and **within 24 hours** of becoming aware;
(b) Provide the following in initial notification:
  - Nature of the breach (if known)
  - Categories and approximate number of data subjects affected
  - Categories and approximate volume of records affected
  - Processor contact for further information
  - Measures taken or proposed to address the breach
(c) Cooperate fully with Controller's investigation and provide updates as information becomes available;
(d) Not notify data subjects or Supervisory Authorities of the breach without Controller's prior written consent, unless required by law.

---

## 10. RETURN AND DELETION OF DATA

Upon termination or expiry of the Main Agreement, Processor shall, at Controller's election:
(a) **Return** all personal data to Controller in a machine-readable format within **[30] days**; OR
(b) **Delete** all personal data (including copies) within **[30] days** and provide written certification of deletion.

Processor may retain personal data only where required by applicable law, for the minimum period required, with continued application of all protections in this DPA.

---

## 11. AUDIT RIGHTS

### 11.1 Information
Processor shall make available all information reasonably necessary to demonstrate compliance with this DPA upon Controller's written request.

### 11.2 Audit
Controller (or authorized third-party auditor) may conduct audits of Processor's processing activities:
- **Notice:** [30] days written notice required (except in case of actual or suspected breach)
- **Frequency:** No more than once per calendar year (unless breach)
- **Cost:** Controller bears audit costs; Processor bears its own cooperation costs
- **Confidentiality:** Audit findings are confidential to both parties
- **Alternative:** Processor may satisfy audit obligations by providing current third-party audit reports (SOC2, ISO 27001) where these adequately address Controller's concerns

---

## 12. LIABILITY

Each party's liability under this DPA is subject to the limitations and exclusions set out in the Main Agreement, except to the extent prohibited by Applicable Data Protection Law.

---

## 13. TERM AND TERMINATION

This DPA remains in force for the duration of the Main Agreement. Termination of the Main Agreement automatically terminates this DPA, subject to Section 10 (return/deletion obligations which survive termination).

---

## 14. GOVERNING LAW AND JURISDICTION

This DPA is governed by the laws of [GOVERNING_LAW]. The parties submit to the exclusive jurisdiction of the courts of [GOVERNING_LAW].

---

## SIGNATURES

**CONTROLLER**
Signed: _______________________
Name: _________________________
Title: _________________________
Date: _________________________
[CONTROLLER_NAME]

**PROCESSOR**
Signed: _______________________
Name: _________________________
Title: _________________________
Date: _________________________
[PROCESSOR_NAME]

---

## SCHEDULE 3 — EU STANDARD CONTRACTUAL CLAUSES

*Where international transfer mechanism is required, attach the applicable EU SCCs (Commission Decision 2021/914) Module 2 (Controller to Processor) or UK IDTA. Do not modify SCCs — they must be used as adopted by the European Commission.*

*Reference: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32021D0914*
