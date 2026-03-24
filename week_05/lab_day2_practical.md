# Week 5 Day 2 Lab: Cloud Security Incident Analysis and Control Planning (Individual)

## What you are doing
You are acting as an entry-level cloud security analyst on an active CampusBridge security incident.

Your job is to produce a professional analysis packet that a security lead could review and use.

## Time and format
- 85-90 minutes
- Individual
- No coding required
- Professional writing (clear, specific, actionable)

## Required chapter alignment
- 8.1 Cloud Computing Concepts
- 8.2 Moving to the Cloud
- 8.3 Cloud Security Tools and Techniques
- 8.4 Cloud Identity Management
- 8.5 Securing IaaS

---

## Case context
CampusBridge is a student-support platform running on cloud services:
- Managed PostgreSQL service for student support records
- Cloud object storage for report exports
- Serverless API functions for integrations
- VM-based batch transform job in a VPC
- External analytics SaaS dashboard

Security observed abnormal reads, identity anomalies, and policy drift during business hours.

---

## What to submit (one packet)
Submit one document with sections A-G in order.

Required sections:
1. Section A (8.1 + 8.2): Cloud model and shared responsibility map
2. Section B (8.4): Identity incident response decision
3. Section C (8.3): Storage exposure containment recommendation
4. Section D (8.5): IaaS hardening response decision
5. Section E (8.3 + 8.4 + 8.5): 24-hour cloud control prioritization
6. Section F (Supabase example): Platform configuration risk analysis
7. Section G: Executive update memo (150-180 words)

Optional bonus:
8. Section H: One advanced analyst artifact

---

## How to do this lab (workflow)
Use this workflow in order. Do not skip steps.

### Step 1: Extract facts
Pull only direct facts from each evidence packet.
Do not mix facts with assumptions.

### Step 2: Label the cloud risk mechanism
For each section, name the mechanism first (identity abuse, policy drift, excessive trust boundary, network exposure, etc.).

### Step 3: Pick one first action
Choose the first control/action that reduces current risk fastest.

### Step 4: Assign ownership
Name the role that owns execution (not just "IT").

### Step 5: Add verification
Name one artifact or signal that proves your action worked.

### Step 6: Communicate clearly
Write for mixed audiences: technical peers and non-technical leadership.

---

## Section A (8.1 + 8.2): Cloud Model and Shared Responsibility Map

### Evidence A
- Managed PostgreSQL database service
- Object storage for exported reports
- Serverless function for API processing
- VM-based nightly transform job
- External analytics dashboard service

### Task
1. Classify each component as IaaS, PaaS, or SaaS.
2. For each component assign primary owner for:
- patching and runtime hardening
- identity configuration
- data classification and handling
- logging retention
3. Add one provider due-diligence question.
4. Add one migration risk item.

### Output format
- One cloud responsibility matrix
- One short paragraph for due-diligence + migration risk

---

## Section B (8.4): Identity Incident Response Decision

### Evidence B
```text
11:08 OAuth refresh token used from unfamiliar ASN
11:10 Service account used to list sensitive export objects
11:12 Conditional access policy showed recent exception for legacy client
11:16 Failed token-rotation job alert reopened (age: 13 days)
11:18 Privileged login without MFA challenge from new location
```

### Task
1. State the primary identity risk mechanism.
2. Choose the best first response action.
3. Defend why that action is first.
4. Name one identity verification artifact.

### Output format
- 1-2 paragraph incident decision note
- Must include: mechanism, first action, rationale, verification artifact

---

## Section C (8.3): Storage Exposure Containment Recommendation

### Evidence C
- Object storage policy allowed broad read path for 22 minutes.
- Access logs show read requests from unfamiliar IP ranges.
- Public read rollback occurred, but no blocklist or explicit deny is in place.
- Data type in bucket: exported advising reports with PII fields.

### Task
1. Identify the exposure mechanism and likely impact.
2. Pick one first containment action.
3. Add one governance control to prevent recurrence.
4. Explain one utility or operations tradeoff.

### Output format
- One short analysis brief (about 150-220 words)
- Must include: mechanism label, containment action, governance fix, tradeoff

---

## Section D (8.5): IaaS Hardening Response Decision

### Evidence D
```text
Admin jump host security group allowed 0.0.0.0/0 on management port.
Base image patch level is 47 days behind standard.
Instance profile includes wildcard read on storage path prefix.
Network flow logs exist but alert threshold is too high to trigger in time.
```

### Task
1. State the primary IaaS security failure.
2. Choose the best first hardening action.
3. Defend why that action is first.
4. Name one verification artifact.

### Output format
- 1-2 paragraph hardening decision note
- Must include: failure mode, first action, rationale, verification artifact

---

## Section E (8.3 + 8.4 + 8.5): 24-Hour Cloud Control Prioritization

### Evidence E
```text
Storage exposure event: contained but monitoring remains weak.
OAuth token misuse event: active investigation, uncertain blast radius.
IaaS admin port exposure: corrected in one region, not globally verified.
Control-plane logs exist but alert quality is low and noisy.
```

Control options:
- enforce explicit deny for public object reads on sensitive buckets
- rotate/revoke high-risk OAuth and service account credentials
- tighten all admin ingress rules and verify region-wide parity
- enforce MFA for privileged cloud console and identity admin roles
- enable high-confidence control-plane alerts with tuned thresholds
- enforce short-lived privileged access with approval workflow
- segment workload network paths to reduce lateral movement
- keep as-is until weekly change window

### Task
Pick your first 5 controls in order.

For each selected control, include:
1. Why this rank position
2. Chapter mapping (8.3, 8.4, or 8.5)
3. Owner role
4. One CSF function tag (GV/ID/PR/DE/RS/RC)

### Output format
- Ranked table (1 through 5)
- One sentence per row for rationale

---

## Section F (Supabase Example): Platform Configuration Risk Analysis

### Evidence F
CampusBridge pilot team used Supabase for a prototype student-case app:
- `anon` key is embedded in the frontend client (expected for public client use)
- `service_role` key was stored in CI and appeared once in job logs
- Row Level Security (RLS) enabled on 6 of 8 sensitive tables
- Storage bucket `case-exports` was set to public during testing
- Dashboard admin accounts do not enforce MFA
- Audit logs are enabled, but no alert rule exists for policy changes

### Task
1. Identify the top 3 cloud security risks in this Supabase setup.
2. Rank the first 4 remediation actions in order.
3. For each remediation, map it to a Supabase control area:
- RLS
- API key and secret handling
- Storage access policy
- Auth and admin access controls
- Audit/monitoring
4. Name one verification artifact for each remediation.

### Output format
- Ranked remediation table (1 through 4)
- One short paragraph (120-160 words) explaining your priority order

---

## Section G: Executive Update Memo (required)

### Audience
Non-technical dean

### Length
150-180 words

### Task
Write an executive update that includes:
1. What happened
2. What was prioritized first and why
3. Current CIA risk status
4. Next 24-hour actions
5. Provider-owned vs customer-owned responsibilities

### Output format
- Single memo block

---

## Section H (optional bonus)
Choose one:
- SOC-style cloud incident ticket
- Cloud attack-path mapping with justification
- Validation evidence line for one selected control

---

## Grading (100 points + bonus)
- 15: Section A
- 15: Section B
- 15: Section C
- 15: Section D
- 20: Section E
- 10: Section F
- 10: Section G
- Optional +10: Section H

## Quality bar (what strong work looks like)
Strong work:
- identifies cloud mechanism clearly
- prioritizes controls with defensible order
- names ownership precisely
- uses evidence from the case
- includes verification artifacts
- communicates clearly for intended audience

Weak work:
- generic checklist with no sequencing logic
- vague ownership labels
- no verification signal
- conclusions not tied to evidence
- memo disconnected from technical choices
