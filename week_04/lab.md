# Week 4 Quick Lab (Individual): Host + Network Incident Triage

## Duration
20-25 minutes (in class)

## Purpose
Practice incident reasoning across endpoint and network evidence.
You are not exploiting anything. You are performing defensive triage and mitigation planning.

## Rules
- Work independently.
- Use only the sanitized samples below.
- Do not test live systems.
- No exploit development steps.
- Use course vocabulary: CIA, trust boundary, least privilege, containment, recovery, accountability.

## Scenario Context
A campus service experiences suspicious endpoint activity and sudden network instability during a high-usage period.
Your task is to analyze evidence quality and recommend high-leverage controls in the right order.

## How to Answer (Student Scaffold)
Use this exact mini-workflow for each sample:

1. **State what happened in plain language**
   - One sentence only.
   - Start with: `The evidence suggests...`

2. **Pick the primary CIA impact**
   - `Confidentiality`: data might be exposed.
   - `Integrity`: system behavior or records may be altered.
   - `Availability`: service performance or uptime is degraded.
   - If two apply, pick one primary and mention the secondary briefly.

3. **Choose one immediate containment action**
   - Ask: `What action most reduces harm in the next 5-15 minutes?`
   - Choose one action only, then justify briefly.

4. **Add one verification step**
   - Ask: `What evidence would increase confidence before/after containment?`
   - Example types: hash check, process tree review, SIEM correlation, sign-in log validation.

5. **Name one owner role**
   - SOC analyst, system admin, security engineer, identity admin, incident lead, etc.
   - Use the role most likely to execute the first action.

6. **Set urgency with one reason**
   - `now`: active risk likely expanding.
   - `today`: serious but not clearly propagating.
   - `this sprint`: important hardening or prevention follow-up.

## Fast Decision Table

| Prompt Type | What "Strong" Looks Like | What to Avoid |
|---|---|---|
| Security concern | Specific mechanism (not generic fear) | "Something suspicious happened" |
| CIA impact | One primary + brief why | Listing all 3 without explanation |
| Containment | Immediate, feasible, and bounded | Vague "improve security" statements |
| Verification | Concrete evidence request | "Investigate more" |
| Owner | Real role tied to action | "Team" / "everyone" |
| Urgency | Time + risk reason | Time label without rationale |

## Sample A: Endpoint Alert Snapshot
```text
Timestamp: 09:14:22
Host: ADV-WS-14
User: svc_reporting
Alert: Unsigned process launched from privileged context
Parent process: powershell.exe
Child process: updaterhost.exe
Command line: updaterhost.exe --sync --silent
Hash reputation: unknown
```

### Your Required Analysis for Sample A
1. Most likely security concern (one sentence)
2. Primary CIA impact if confirmed
3. Immediate containment action
4. One verification step to increase confidence
5. Named control owner (SOC analyst, system admin, security engineer, etc.)
6. Urgency: `now`, `today`, or `this sprint` + one-sentence justification

## Sample B: Network Flow Excerpt
```text
Time window: 09:20-09:28
Source subnet: 10.42.18.0/24
Destination IPs: 185.73.11.44, 203.17.99.118, 91.200.15.33
Protocol: HTTPS (443)
Pattern: outbound connections increased 7x baseline
Average payload size: high variance
Internal service impact: transaction latency up 48%
```

### Your Required Analysis for Sample B
1. Most likely risk hypothesis (interruption, exfiltration, or both)
2. Primary CIA impact and why
3. One network control to apply first
4. One monitoring improvement for faster future detection
5. Named control owner
6. Urgency + one-sentence justification

## Sample C: Identity + Email Chain
```text
08:57 User receives email: "Urgent Payroll Verification"
09:02 User clicks link and enters credentials on look-alike page
09:06 VPN login from unfamiliar location succeeds
09:09 New MFA device enrollment attempted
09:12 Access requests to internal HR reporting portal increase
```

### Your Required Analysis for Sample C
1. Where trust failed first
2. Most likely attack objective
3. First identity control action
4. One user-support action that reduces downstream harm
5. Named control owner
6. Urgency + one-sentence justification

## Worked Format Example (Use This Structure)
Example only for format/style (not one of the graded samples):

- Concern: `The evidence suggests a likely credential misuse event with potential unauthorized access.`
- Primary CIA: `Confidentiality, because unauthorized access could expose protected records.`
- First containment: `Force session revocation for the account and require reauthentication.`
- Verification: `Review sign-in logs for impossible travel and device fingerprint mismatch.`
- Owner: `Identity administrator.`
- Urgency: `Now, because active access may still be ongoing.`

## Final Deliverable Format (One Page)
Use this structure:

1. **Top Priority Control (Across all samples):**
   - Control:
   - Why this first:
   - Owner:

2. **Sample A Summary (3-4 lines)**
3. **Sample B Summary (3-4 lines)**
4. **Sample C Summary (3-4 lines)**

5. **Reflection (2-3 sentences):**
   - What evidence was strongest?
   - What evidence is still uncertain?
   - What would you request next?

## Grading Lens (Used in Class Debrief)
- Mechanism accuracy
- CIA mapping quality
- Mitigation feasibility
- Ownership clarity
- Professional writing clarity
