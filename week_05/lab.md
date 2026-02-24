# Week 5 Quick Lab (Individual): Database + Cloud Incident Analysis

## Duration
20-25 minutes (in class)

## Purpose
Practice Week 5 control prioritization using Chapter 7 and Chapter 8 concepts.
You are not exploiting systems. You are analyzing risk and selecting defensible first actions.

## Rules
- Work independently.
- Use only the sanitized evidence samples below.
- No exploit development or live system testing.
- Use course terms: CIA, least privilege, shared responsibility, containment, verification, accountability.

## Scenario Context
A campus student-support platform uses:
- managed relational database for case and advising records
- cloud object storage for report exports
- API integrations for downstream dashboards

The security team observed unusual data access patterns with no immediate full outage.
Your task is to identify likely risk mechanisms and prioritize first controls.

## How to Answer Each Sample
Use this exact mini-workflow:

1. **State what likely happened**
   - One sentence.
   - Start with: `The evidence suggests...`

2. **Choose the primary CIA impact**
   - Pick one: `Confidentiality`, `Integrity`, or `Availability`.
   - If a secondary impact exists, mention it in one short phrase.

3. **Choose one first control action**
   - Ask: `What action most reduces active harm in the next 5-15 minutes?`
   - Choose one action only.

4. **Add one verification step**
   - Ask: `What evidence confirms whether my hypothesis is correct?`

5. **Name one owner role**
   - SOC analyst, database admin, cloud engineer, identity admin, incident lead, etc.

6. **Set urgency and justify**
   - `now`, `today`, or `this sprint`
   - One sentence explaining why.

## Sample A: Database Access Anomaly
```text
Time window: 14:02-14:14
DB role: reporting_app
Observed query: SELECT * FROM student_support_cases
Baseline pull volume: ~450 rows/day
Observed volume: 18,220 rows in 12 minutes
Source endpoint: /reports/export/full
Change ticket for role scope update: none
```

### Required Analysis for Sample A
1. Most likely security concern
2. Primary CIA impact and why
3. First control action
4. One verification step
5. Owner role
6. Urgency + reason

## Sample B: Cloud Storage Policy Drift
```text
Service: object storage bucket 'stu-support-exports'
Policy change time: 13:51
Change detail: read access widened beyond approved application role
External read requests from unfamiliar ASN increased 6x baseline
Portal performance impact: minimal
```

### Required Analysis for Sample B
1. Where trust failed first
2. Primary CIA impact and why
3. First cloud control action
4. One governance fix to prevent recurrence
5. Owner role
6. Urgency + reason

## Sample C: API Token Reuse
```text
Integration service token age: 214 days
Token used from three new source IP ranges in one hour
API path: /analytics/export/v2
Failed token-rotation job alerts present for past two weeks
```

### Required Analysis for Sample C
1. Most likely attack objective
2. Primary CIA impact and why
3. First identity/secrets control action
4. One user-support or communication action
5. Owner role
6. Urgency + reason

## Final Deliverable Format (One Page)
1. **Top Priority Control Across All Samples**
   - Control:
   - Why first:
   - Owner:

2. **Sample A Summary (3-4 lines)**
3. **Sample B Summary (3-4 lines)**
4. **Sample C Summary (3-4 lines)**

5. **Reflection (2-3 sentences)**
   - Which evidence item was strongest?
   - What uncertainty remains?
   - What extra evidence would you request next?

## Grading Lens (In-Class Debrief)
- Mechanism accuracy
- CIA mapping quality
- Feasibility of first action
- Ownership clarity
- Professional writing clarity
