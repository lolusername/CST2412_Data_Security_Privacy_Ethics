# Week 5 Day 2 Individual Lab (Book-Aligned, No Coding)

## Title
Chapter 7 + Chapter 8 Applied Lab: Databases, Cloud, and Big Data Security

## Syllabus Anchor
Week 5 topic in `CST_2412.pdf`:
- Databases, Cloud, Big Data Security
- Reading: Chapters 7-8

## Purpose
This Day 2 lab is a direct application of textbook Chapter 7 and Chapter 8 concepts.
You will complete one coherent case packet that uses the same section logic as the book.

## Duration
85-90 minutes (full class period)

## Format
- Individual work only
- No coding required
- Every answer must include a short justification

## Required textbook section alignment
- 7.2 Security Requirements of Databases
- 7.3 Reliability and Integrity
- 7.4 Database Disclosure
- 8.1 Cloud Computing Concepts
- 8.2 Moving to the Cloud
- 8.3 Cloud Security Tools and Techniques
- 8.4 Cloud Identity Management
- 8.5 Securing IaaS

## Supplemental real-world alignment (industry practice)
- NIST CSF 2.0 function mapping (GV/ID/PR/DE/RS/RC)
- NIST SP 800-61r3 incident response as continuous risk management
- CISA CPG 2.0 baseline control prioritization mindset
- OWASP API Security Top 10 category tagging for API/token issues

---

## Current threat context (5-minute kickoff briefing)
Use these 2025 data points for urgency framing before students begin:
- Third-party involvement in breaches doubled to 30%.
- Exploitation of vulnerabilities increased by 34%.
- Credential abuse (22%) and vulnerability exploitation (20%) were top initial vectors.
- Ransomware appeared in 44% of breaches.

Source: Verizon DBIR 2025 release summary  
https://www.verizon.com/about/news/2025-data-breach-investigations-report

---

## Case Context (used across all checkpoints)
CampusBridge is a student-support platform:
- PostgreSQL database stores case and advising data.
- Cloud object storage holds report exports.
- API integrations feed dashboards.
- A new analytics workload is being prepared in cloud infrastructure.

Security has observed abnormal reads and policy drift during a normal business day.

---

## What You Submit (one packet)
1. Section A: Database security requirements map (7.2)
2. Section B: Reliability/integrity decisions (7.3)
3. Section C: Disclosure risk analysis (7.4)
4. Section D: Cloud model + shared responsibility map (8.1, 8.2)
5. Section E: Cloud control prioritization (8.3, 8.4, 8.5)
6. Section F: Executive response memo (150-180 words)
7. Section G (optional bonus): Real-world analyst artifacts

---

## Full-Class Workflow

| Time | Checkpoint | Book Section | Output |
|---|---|---|---|
| 0-8 min | Setup | N/A | Packet header |
| 8-22 min | A | 7.2 | Requirements map |
| 22-36 min | B | 7.3 | Integrity decisions |
| 36-50 min | C | 7.4 | Disclosure analysis |
| 50-65 min | D | 8.1 + 8.2 | Model + ownership map |
| 65-80 min | E | 8.3 + 8.4 + 8.5 | Control priority plan |
| 80-90 min | F | Synthesis | Executive memo |
| Optional | G | Supplemental practice | Analyst artifacts |

---

## Section A (7.2): Security Requirements of Databases

### Evidence packet A
Current controls in CampusBridge:
- MFA for DB admins
- Quarterly role review
- Audit logs enabled for privileged queries
- Daily encrypted backups
- No formal availability target defined

### Your task
Map each item to one primary requirement from 7.2:
- Element integrity
- Auditability
- Access control
- User authentication
- Availability
- CIA balance (integrity/confidentiality/availability)

Then answer:
1. Which requirement is weakest right now?
2. One control you would add immediately.

---

## Section B (7.3): Reliability and Integrity

### Evidence packet B
Incident timeline:
```text
10:03 bulk update started for advising_status
10:04 network interruption during write phase
10:05 retries triggered by app service
10:08 records show mixed old/new values
10:09 restore point exists from 09:45
```

### Your task
1. Identify the primary integrity risk.
2. Choose the best first protection/response from 7.3 concepts:
   - two-phase update discipline
   - concurrency/consistency controls
   - recovery from known-good backup
   - redundancy/internal consistency checks
3. Explain why your choice should be first.
4. Name one verification artifact.

---

## Section C (7.4): Database Disclosure Risk

### Evidence packet C
Requested data release for analytics pilot:
- Table 1: student demographic fields (de-identified IDs)
- Table 2: advising outcomes and risk labels
- Table 3: location + program + scholarship flag

Analyst note:
```text
Single rows in small subgroups can still be uniquely inferred.
```

### Your task
1. Identify likely disclosure type(s):
   - direct disclosure
   - inference disclosure
   - aggregation/linkage disclosure
2. Select one first mitigation from 7.4:
   - suppression
   - generalization
   - perturbation/swapping
   - minimum subgroup threshold rule
3. Explain one tradeoff between utility and privacy.

---

## Section D (8.1 + 8.2): Cloud Concepts + Moving to Cloud

### Evidence packet D
Planned architecture:
- Managed database service
- Object storage for exports
- External analytics SaaS dashboard
- VM-based batch transform job

### Your task
1. Label each component as IaaS, PaaS, or SaaS (8.1).
2. For each component, assign primary owner for:
   - patching
   - identity configuration
   - data classification policy
   - logging retention
3. Based on 8.2, list:
   - one cloud provider assessment question
   - one migration risk analysis item

---

## Section E (8.3 + 8.4 + 8.5): Cloud Control Prioritization

### Evidence packet E
Current cloud findings:
```text
Object storage policy allowed broad read path for 18 minutes.
OAuth token used from unfamiliar IP range.
IaaS security group allowed 0.0.0.0/0 on admin port.
Control-plane logs exist but alerts are low fidelity.
```

### Your task
Pick your first **5 controls in order** from this list:
- explicit deny for public object reads
- rotate/revoke OAuth tokens
- tighten security group ingress
- enable high-confidence alert rules for control-plane events
- enforce short-lived privileged access
- segment workload network paths
- keep as-is until weekly change window

For each chosen control include:
1. Why it is at that position
2. Which section it maps to (8.3, 8.4, or 8.5)
3. Owner role
4. One CSF function tag (GV/ID/PR/DE/RS/RC)

---

## Section F: Executive Response Memo (150-180 words)
Write for a non-technical dean:
1. What happened
2. What was prioritized first and why
3. Current CIA risk status
4. What must happen in the next 24 hours
5. Which responsibilities are provider-owned vs customer-owned

---

## Section G (Optional Bonus): Real-World Analyst Artifacts

### G1 Incident ticket (SOC style)
Create a short ticket with:
- incident title
- severity level
- current scope
- first action
- current owner
- next status update time

### G2 ATT&CK behavior mapping
Pick one likely adversary behavior and justify:
- T1078 Valid Accounts
- T1190 Exploit Public-Facing Application
- T1566 Phishing

### G3 Validation evidence line
For one control from Section E, add:
1. Expected success signal
2. Verification artifact
3. Fallback action if validation fails

---

## Grading Rubric (100 points)
- 15: Section A (7.2 mapping accuracy)
- 15: Section B (7.3 integrity reasoning)
- 15: Section C (7.4 disclosure + mitigation quality)
- 20: Section D (8.1/8.2 model and ownership clarity)
- 25: Section E (8.3/8.4/8.5 prioritization quality)
- 10: Section F executive communication quality
- Optional +10 bonus: Section G practical analyst artifacts

## Quality Standard
Strong submissions:
- use correct chapter concepts
- prioritize practical controls
- separate facts from assumptions
- assign clear owners
- explain decisions briefly and defensibly
- tie controls to current operational risk patterns
