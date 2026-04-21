# Week 11 Instructor Guide: Data Analytics for Security

Research status: verified and updated on April 21, 2026.
Audience: instructor-facing only.
Week alignment: `CST_2412.pdf` lists Week 11-12 as `Data Analytics for Security` with selected reading.

This guide is meant to teach you the content deeply enough that you can improvise, answer student questions, and connect the Week 11 labs to real security work.
It is intentionally more detailed than the slide notes.
Use it as:
- a content refresher before class
- a speaking guide when you want more than the deck gives you
- an answer key for the labs and writing responses
- a source-backed explanation of why this topic matters technically and ethically

## Week 11 in one sentence
Week 11 teaches students how to read security data as evidence, turn repeated patterns into defensible security judgments, and communicate those judgments in the form of realistic analyst writing.

## How Week 11 fits the course
By Week 11, students have already seen:
- core security concepts
- authentication and cryptography
- web and network security
- databases, cloud, and big data security
- privacy, law, and ethics through Chun, Benjamin, and Forensic Architecture

Week 11 shifts from "what security systems are" to "how a security analyst reasons from data."
This is important because students often think security jobs are either:
- purely technical implementation jobs, or
- highly advanced adversarial jobs

Week 11 shows the middle layer of real security operations:
- logs
- alerts
- queues
- prioritization
- evidence
- documentation

This is one of the most career-relevant transitions in the course.

## High-level goals for the week
By the end of Week 11, students should be able to:
- explain what security analytics is in plain English
- distinguish an event from an alert and an alert from an incident
- read authentication logs for repeated patterns and sequence
- identify likely password-spray-style behavior in a CSV
- use account or asset context to change urgency
- justify a first action instead of only naming a problem
- explain why analytics and monitoring still require privacy and governance limits
- write short professional notes similar to what junior analysts actually produce

## The core teaching frame
If you need a simple frame to repeat all week, use this:

1. Security teams rarely see the whole problem at once.
2. They see fragments.
3. Analytics turns fragments into patterns.
4. Context turns patterns into risk.
5. Judgment turns risk into action.
6. Writing turns action into something another person can use.

That progression is the backbone of both Day 1 and Day 2.

## The most important thing not to let students misunderstand
Do not let students leave with the idea that security analytics means machine learning.
That is too narrow and it will confuse the course.
A better line is:

`Security analytics is the practice of extracting useful security meaning from operational data.`

That includes:
- counts
- filters
- baselines
- thresholds
- sequence analysis
- context enrichment
- queue prioritization
- analyst notes

If students understand that, they will have a more realistic picture of how security work often begins.

## Primary-source research anchors
These are the best source anchors for teaching this week.
I recommend keeping them in mind, even if you do not cite them aloud in class.

### NIST SP 800-92: Guide to Computer Security Log Management
Link: [NIST SP 800-92](https://csrc.nist.gov/pubs/sp/800/92/final)

Why it matters:
- It is the classic log-management foundation.
- It explains why logs support security operations, auditing, troubleshooting, and incident response.
- It reinforces that logging is useful only if organizations can actually manage, protect, review, and use the data.

Teaching use:
- Use this to justify why logs matter.
- Also use it to justify why uncontrolled logging is not automatically good practice.

### NIST SP 800-137: Information Security Continuous Monitoring
Link: [NIST SP 800-137](https://csrc.nist.gov/pubs/sp/800/137/final)

Why it matters:
- It frames monitoring as an ongoing process tied to risk decisions.
- It helps you explain that monitoring is not just data collection; it is collection connected to organizational action.

Teaching use:
- Good support for the idea that security analytics exists to improve decisions, not only to create dashboards.

### NIST SP 800-61 Revision 3: Incident Response Recommendations and Considerations for Cybersecurity Risk Management
Link: [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final)

Why it matters:
- It is the current NIST incident response guidance.
- It supports careful distinction between signals, investigation, and incident handling.
- It fits the Day 1 event-alert-incident distinction and the Day 2 escalation logic.

Teaching use:
- Use this to remind students that not every event is an incident.
- Escalation needs evidence and process.

### NIST SP 800-63B: Digital Identity Guidelines - Authentication and Lifecycle Management
Link: [NIST SP 800-63B](https://pages.nist.gov/800-63-4/sp800-63b.html)

Why it matters:
- It covers modern authentication practice, including throttling/rate limiting and MFA guidance.
- It helps you explain why repeated failed logins and MFA events are important.

Teaching use:
- Useful when students ask why repeated failures matter or what a rational first action might look like.

### MITRE ATT&CK: Brute Force / Password Spraying / Credential Stuffing / MFA Request Generation
Links:
- [Brute Force (T1110)](https://attack.mitre.org/techniques/T1110/)
- [Password Spraying (T1110.003)](https://attack.mitre.org/techniques/T1110/003/)
- [Credential Stuffing (T1110.004)](https://attack.mitre.org/techniques/T1110/004/)
- [Multi-Factor Authentication Request Generation (T1621)](https://attack.mitre.org/techniques/T1621/)
- [Authentication Logs Data Component](https://attack.mitre.org/datacomponents/DC0002/)

Why it matters:
- ATT&CK gives students a taxonomy for common login-related attack behavior.
- It helps you connect simple CSV patterns to real-world attacker techniques.

Teaching use:
- Day 1: password spray and brute-force distinctions.
- Day 2: credential stuffing and MFA-fatigue style alerts.

### MITRE ATT&CK Mitigation M1036: Account Use Policies
Link: [Account Use Policies (M1036)](https://attack.mitre.org/mitigations/M1036/)

Why it matters:
- Useful for talking about lockouts, rate limits, and policy decisions.
- Also good for showing that defenses often have tradeoffs.

### NIST Privacy Framework / Privacy Engineering Objectives
Links:
- [NIST Privacy Framework](https://www.nist.gov/privacy-framework)
- [NISTIR 8062 Privacy Engineering and Risk Management](https://www.nist.gov/publications/privacy-engineering-and-risk-management-federal-systems)

Why it matters:
- Supports the privacy side of Week 11.
- Useful when explaining that monitoring should still be governed by purpose limitation, role-based access, and retention boundaries.

## Day 1: What you are really teaching
Day 1 is not just a lesson about authentication logs.
It is a lesson about how analysts think.

The real Day 1 sequence is:
1. raw events exist
2. some events repeat
3. repetition creates a pattern candidate
4. sequence can strengthen or weaken that candidate
5. account context changes urgency
6. a reasonable first action must be justified
7. the action has to be written clearly enough for someone else to use

That is the intellectual structure of the day.

## Day 1 concept deep dive

### 1. Security analytics is evidence work
A strong sentence to repeat:

`Security analytics is evidence work under uncertainty.`

Why this matters:
- Analysts almost never start with certainty.
- They start with pieces of evidence.
- Those pieces have to be combined, compared, and interpreted.

This is one reason Week 11 pairs naturally with Week 10.
Week 10 taught students that technology and evidence are not neutral.
Week 11 teaches them how operational evidence is actually used.

### 2. Event vs alert vs incident
Students confuse these constantly.
You should be strict about it.

Use this version:
- `Event`: one recorded activity.
  Example: a single failed login.
- `Alert`: a signal that some event pattern might matter.
  Example: 14 failed logins from one source or 9 MFA prompts in 3 minutes.
- `Incident`: a confirmed or strongly suspected security problem requiring response and tracking.

Why the distinction matters:
- If students turn every event into an incident, they will overreact.
- If they treat every alert like just another event, they will underreact.

### 3. Authentication data is a practical teaching source
Authentication logs are good for teaching because they are:
- common across organizations
- structured enough for beginners
- directly tied to compromise risk
- analyzable in a spreadsheet without special infrastructure

Authentication data can show:
- repeated failures
- password spray behavior
- success after repeated failures
- MFA failures or push fatigue
- rare or geographically inconsistent access
- changes in device familiarity

### 4. Pattern shape matters more than one dramatic row
This is the main Day 1 analytical idea.

Teach the three basic shapes clearly:

#### Normal user mistake
Typical shape:
- one user
- one or two failures
- then a success
- familiar device or location

Why it usually matters less:
- It fits expected user behavior.
- There is little evidence of broad or repeated attack effort.

#### Brute force
Typical shape:
- many attempts
- one account
- repeated effort on one target

What it suggests:
- An attacker is concentrating guesses against one account.
- The immediate target matters a lot.

#### Password spray
Typical shape:
- one source
- many accounts
- usually one or a few guesses per account

What it suggests:
- The attacker is trying common credentials across many users.
- This often avoids lockout thresholds that trigger on one account.

This distinction is supported by ATT&CK's password-spraying sub-technique.

### 5. Sequence can be more important than count
Counts are necessary, but order is often what makes the pattern operationally important.

Examples:
- many failures followed by one success
- password reset followed by unfamiliar login
- success followed by MFA trouble

What to say to students:

`One row can be weak evidence. A sequence can tell a much stronger story.`

### 6. Baseline is comparison, not magic
Students may hear "baseline" and assume you mean advanced statistical modeling.
Do not let that happen.

For this class, baseline means:
- what is usual for this user?
- what is usual for this system?
- what is usual at this time?
- what is usual for this source or device?

Strong Day 1 line:

`Suspicion only makes sense relative to an expectation of normal behavior.`

### 7. Enrichment is where technical data becomes meaningful
Enrichment means bringing in additional context that is not visible in the event row itself.

For Day 1 that context is:
- department
- role title
- privileged status
- sensitive-account status
- expected MFA

Why it matters:
- The same login pattern means something different on a finance admin account than on a low-risk student account.
- Students need to see that analytics is not just counting. It is counting plus context.

### 8. First action logic
Students usually want to jump to "solve the problem."
That is not how analysts work.

A better framework:
- What is the fastest reasonable step to reduce immediate risk?
- What evidence justifies that step?
- What downside does the step create?

Good options you can discuss:
- block a source IP
- force a password reset
- force MFA re-verification
- open a deeper incident investigation
- continue monitoring with justification

The lesson is not that one action is universally correct.
The lesson is that good analysts can justify why a first step is proportionate.

### 9. Why privacy still matters in a log-analysis week
The technical temptation is to say "more logs = better security."
That is too simplistic.

Key points to teach:
- Logs are useful for detection, investigation, and accountability.
- But retention should still have a purpose and a timeline.
- Access to logs should be limited and audited.
- Collection should be connected to a security need rather than open-ended institutional curiosity.

A good classroom line:

`Security visibility is useful, but it should not become unlimited surveillance by default.`

## Day 1 answer key and walkthrough
Files:
- `week_11/data/day1_auth_events.csv`
- `week_11/data/day1_user_context.csv`

### What is actually in the dataset
There are `24` total authentication rows.
There are `15` `login_failed` rows.

Failed-login counts by source IP:
- `198.51.100.77` -> `14`
- `203.0.113.24` -> `1`

Distinct users targeted from `198.51.100.77`:
- `12`
- `u_admin_fin`
- `u_afernandez`
- `u_garcia`
- `u_harris`
- `u_jlee`
- `u_nguyen`
- `u_ortiz`
- `u_patel`
- `u_sharma`
- `u_student2`
- `u_student3`
- `u_student4`

Strong teaching interpretation:
- this is not a single user forgetting a password
- this is not a clean one-account brute force
- the best classroom label is `likely password spray behavior`

### The risky success
The account with the most important success-after-failures sequence is:
- `u_admin_fin`
- source IP: `198.51.100.77`
- repeated failed attempts: `3`
- then `login_success`
- then `mfa_failed`

This is the center of the Day 1 story.

### Why `u_helpdesk` is a good teaching contrast
The dataset also contains:
- one failed login on `u_helpdesk`
- then a success from the same IP `203.0.113.24`

Why this is pedagogically useful:
- it reminds students that not every fail-then-success pattern is equally urgent
- a single failed attempt followed by a successful login from a managed laptop in Queens is much less suspicious than the `u_admin_fin` sequence from the spray IP using an unknown browser and unknown city

### Account context that changes urgency
For `u_admin_fin`:
- department: `Finance`
- role title: `finance-admin`
- privileged account: `yes`
- sensitive account: `yes`
- expected MFA: `yes`

That is exactly the kind of context that should raise urgency.

### Best Day 1 first-action reasoning
A strong answer for class discussion:
- Force a password reset for `u_admin_fin` and require MFA re-verification immediately.

Why this is strong:
- it directly reduces the risk that a compromised credential remains usable
- it is targeted to the most concerning account
- it works even if source blocking is incomplete

What students can say as a tradeoff:
- it may disrupt a legitimate user briefly
- it does not by itself explain how the credentials were obtained
- it should probably be paired with deeper review and possibly source blocking

Also acceptable:
- temporarily block the suspicious source IP while opening investigation
- open a full incident investigation immediately because the privileged account plus suspicious sequence is strong enough to justify it

Less strong but teachable:
- continue monitoring without action

Why it is weaker:
- the combination of repeated spray behavior, privileged account success, and MFA trouble is already strong enough to justify more than observation

## Day 1 code examples you can use in class or after class
Companion notebook:
- `week_11/week11_pandas_duckdb_examples.ipynb`

### Python / pandas example
```python
import pandas as pd

events = pd.read_csv("week_11/data/day1_auth_events.csv", parse_dates=["timestamp"])
users = pd.read_csv("week_11/data/day1_user_context.csv")

failed = events.query("event_type == 'login_failed'")
print(failed.groupby("src_ip").size().sort_values(ascending=False))

spray_ip = "198.51.100.77"
print(
    failed.loc[failed["src_ip"] == spray_ip, "user_id"]
    .value_counts()
    .sort_index()
)

merged = events.merge(users, on="user_id", how="left")
print(
    merged.loc[merged["user_id"] == "u_admin_fin",
               ["timestamp", "src_ip", "event_type", "outcome",
                "privileged_account", "sensitive_account"]]
)
```

What to explain:
- `query` keeps the code readable for filtering
- `groupby().size()` is one of the most useful beginner analytics operations
- `merge()` is the enrichment step students are practicing conceptually

### DuckDB / SQL example
DuckDB is a good fit here because the source files are CSVs and the queries stay readable.

```sql
-- Count failed logins by source IP
SELECT
    src_ip,
    COUNT(*) AS failed_count,
    COUNT(DISTINCT user_id) AS targeted_users
FROM read_csv_auto('week_11/data/day1_auth_events.csv')
WHERE event_type = 'login_failed'
GROUP BY src_ip
ORDER BY failed_count DESC;
```

```sql
-- Show the suspicious sequence for the finance admin account
SELECT
    timestamp,
    src_ip,
    event_type,
    outcome,
    factor
FROM read_csv_auto('week_11/data/day1_auth_events.csv')
WHERE user_id = 'u_admin_fin'
ORDER BY timestamp;
```

```sql
-- Enrich events with account context
SELECT
    e.timestamp,
    e.src_ip,
    e.user_id,
    e.event_type,
    u.department,
    u.role_title,
    u.privileged_account,
    u.sensitive_account
FROM read_csv_auto('week_11/data/day1_auth_events.csv') AS e
LEFT JOIN read_csv_auto('week_11/data/day1_user_context.csv') AS u
    ON e.user_id = u.user_id
WHERE e.src_ip = '198.51.100.77'
ORDER BY e.timestamp;
```

## Day 1 common student mistakes
These are the mistakes to expect.

### Mistake 1: Confusing count with certainty
Students may say:
- "14 failures means it is definitely an attack"

Better correction:
- `14 failures from one source against 12 users is strong suspicious evidence, but it is still a pattern that needs interpretation, not absolute proof by itself.`

### Mistake 2: Ignoring sequence
Students may focus only on the count and miss the successful login after the failures.

Correction:
- bring them back to time order
- ask: `What happened next?`

### Mistake 3: Treating all accounts equally
Students may say:
- "A failure is a failure"

Correction:
- ask whether the same pattern would feel equally urgent on a student account and a finance admin account

### Mistake 4: Jumping to giant responses
Students may propose massive actions immediately.

Correction:
- bring them back to first-action logic
- ask: `What is the first reasonable step, and what tradeoff does it create?`

### Mistake 5: Forgetting privacy limits
Students may talk as if logging everything forever is the obvious answer.

Correction:
- ask them why retention exists
- ask who should be allowed to see these logs
- ask how long is actually necessary

## Quick grading guidance for Day 1 writing
The Day 1 writing response is strongest when it sounds like an actual shift note rather than a mini-essay.

### A strong Day 1 note should usually do these things
- name the suspicious source or pattern early
- cite at least one exact detail from the CSVs
- explain why the account context changes urgency
- recommend one practical first action
- include one sentence showing privacy awareness without losing the operational focus

### A weak Day 1 note often sounds like this
- too vague
- only says `there were many failed logins`
- never names the IP, account, or sequence
- recommends an action without explaining why
- ignores the fact that privileged and sensitive accounts matter more

### Fast Day 1 grading rubric
- Full credit:
  clear pattern, exact evidence, strong context use, defensible first action, privacy sentence
- Partial credit:
  sees something suspicious but stays vague or ignores context
- Low credit:
  mostly summary with no defensible evidence or action

## Day 2: What you are really teaching
Day 2 is not just a scoring exercise.
It is about prioritization under limited analyst attention.

The deeper structure is:
1. a queue exists
2. not everything can be investigated at once
3. severity, confidence, and impact are related but distinct
4. asset context changes urgency
5. formulas help organize work but do not replace judgment
6. escalation is a communication act, not just a ranking result

## Day 2 concept deep dive

### 1. Triage is time management under uncertainty
A simple teaching line:

`Triage is the discipline of deciding what deserves attention first when time is limited.`

This matters because students may imagine analysts have infinite time.
They do not.
Queues build up.
Attention is scarce.
Prioritization is operationally essential.

### 2. Severity, confidence, and impact are not the same
Use this structure clearly:
- `Severity`: how technically serious the alert appears
- `Confidence`: how likely it is that the signal is meaningful or real
- `Impact`: how much harm could follow if the alert is true

Why this distinction matters:
- a high-severity, low-confidence alert may still be noisy
- a medium-severity alert on a critical system may deserve first attention
- a mathematically neat score is not the whole story

### 3. Asset context is what makes analytics business-relevant
Without asset context, triage is thin.
Students should learn to ask:
- Is the system high criticality?
- Is it internet exposed?
- Does it contain sensitive data?
- What function does it serve?

A good line:

`Asset context turns raw alerts into business-relevant risk.`

### 4. Simple scores are useful precisely because they are simple
Day 2 uses a deliberately basic scoring method.
That is good pedagogy.

Why:
- students can calculate it manually
- the logic is visible
- it creates disciplined comparison
- it makes the limits of formulas easier to discuss

Important teaching point:
- the score is a starting point for ordering attention
- the score is not a replacement for analyst judgment

### 5. Judgment beyond the score
Students should hear this explicitly:

`A good analyst can explain when to follow the score and when to question it.`

Examples:
- an alert may score lower but still deserve attention because of suspicious context not captured in the formula
- an alert may score well but be explained by a maintenance window or expected behavior

### 6. Escalation is a communication artifact
Escalation is not just saying "this looks bad."
It is handing someone else actionable information.

A strong escalation note includes:
- which alert
- why it stands out
- what asset is involved
- why that context matters
- what next action you want

### 7. Monitoring still needs governance
Day 2 should not drift into "monitor more and keep more forever."
Keep repeating:
- data collection needs purpose
- retention needs a timeline
- access to monitoring systems needs control
- security monitoring should not become general over-profiling of people

## Day 2 answer key and walkthrough
Files:
- `week_11/data/day2_alert_queue.csv`
- `week_11/data/day2_asset_context.csv`

### Scoring rubric from the lab
- severity: high = 3, medium = 2, low = 1
- confidence: high = 3, medium = 2, low = 1
- asset criticality: high = 3, medium = 2, low = 1
- add 1 if internet exposed = yes
- add 1 if sensitive data = yes

### Computed scores
- `A1006` -> `11`
- `A1001` -> `10`
- `A1002` -> `9`
- `A1003` -> `9`
- `A1007` -> `8`
- `A1004` -> `7`
- `A1005` -> `6`
- `A1008` -> `4`

### Best teaching interpretation of top priority
The strongest first escalation is `A1006`.

Why:
- alert type: `mfa-fatigue`
- severity: `high`
- confidence: `high`
- asset: `ASSET-SIS1`, the Student Information System
- criticality: `high`
- internet exposed: `yes`
- sensitive data: `yes`
- notes: `sensitive student records system`

Why it is the best first escalation:
- it combines a strong technical signal with a high-value system and sensitive data
- MFA fatigue implies active pressure on the user or account
- if successful, the attacker may gain access to student records infrastructure

### Why `A1001` is also very strong
`A1001` is the next strongest alert:
- impossible travel
- privileged finance account
- finance database
- high severity, high confidence, sensitive data

This is very strong and could also be defended as first escalation.
If a student chooses it and argues well, that is reasonable.

### Why `A1002` and `A1003` tie
Both score `9`, but they are different kinds of risk.

`A1002`:
- credential stuffing
- learning platform
- medium severity, high confidence
- internet exposed and sensitive data

`A1003`:
- large data download
- shared file server
- high severity, medium confidence
- high criticality and sensitive data

This tie is useful because it teaches judgment.
A student can argue either one should be reviewed first after the top two, as long as the reasoning is clear.

### A good alert to discuss beyond the score
`A1007` is a good "look beyond the number" case.

Why:
- it only scores `8`
- but it touches the VPN gateway, which is a critical entry point
- the notes say travel status is unknown

Teaching point:
- a lower score does not mean "ignore it"
- analysts still need to think about what the formula may be missing

### A good likely-low-priority case
`A1004` is a good low-priority or likely-benign teaching example.

Why:
- it has a planned maintenance window noted
- it involves a new admin-created token during a known change period
- the alert may be real but expected

Teaching point:
- context can lower urgency as well as raise it

### Best Day 2 escalation memo choice
If you want one clean answer for class discussion, use `A1006`.

Recommended first follow-up step:
- contact the identity or system owner immediately
- review the affected account's recent authentication activity in more depth
- consider temporary account protection steps if appropriate

Also acceptable as the first requested step:
- force a password reset and MFA rebind for the user, depending on local identity workflow
- temporarily restrict sign-in until validation occurs

## Day 2 code examples you can use in class or after class
Companion notebook:
- `week_11/week11_pandas_duckdb_examples.ipynb`

### Python / pandas scoring example
```python
import pandas as pd

alerts = pd.read_csv("week_11/data/day2_alert_queue.csv")
assets = pd.read_csv("week_11/data/day2_asset_context.csv")

severity_map = {"high": 3, "medium": 2, "low": 1}
confidence_map = {"high": 3, "medium": 2, "low": 1}
criticality_map = {"high": 3, "medium": 2, "low": 1}

merged = alerts.merge(assets, on="asset_id", how="left")
merged["score"] = (
    merged["severity"].map(severity_map)
    + merged["confidence"].map(confidence_map)
    + merged["asset_criticality"].map(criticality_map)
    + (merged["internet_exposed"] == "yes").astype(int)
    + (merged["sensitive_data"] == "yes").astype(int)
)

print(
    merged[["alert_id", "alert_type", "asset_name", "score"]]
    .sort_values(["score", "alert_id"], ascending=[False, True])
)
```

### DuckDB / SQL example
```sql
WITH scored AS (
    SELECT
        a.alert_id,
        a.alert_type,
        a.severity,
        a.confidence,
        x.asset_name,
        x.asset_criticality,
        x.internet_exposed,
        x.sensitive_data,
        CASE a.severity
            WHEN 'high' THEN 3
            WHEN 'medium' THEN 2
            ELSE 1
        END
        + CASE a.confidence
            WHEN 'high' THEN 3
            WHEN 'medium' THEN 2
            ELSE 1
        END
        + CASE x.asset_criticality
            WHEN 'high' THEN 3
            WHEN 'medium' THEN 2
            ELSE 1
        END
        + CASE WHEN x.internet_exposed = 'yes' THEN 1 ELSE 0 END
        + CASE WHEN x.sensitive_data = 'yes' THEN 1 ELSE 0 END
        AS total_score
    FROM read_csv_auto('week_11/data/day2_alert_queue.csv') a
    LEFT JOIN read_csv_auto('week_11/data/day2_asset_context.csv') x
        ON a.asset_id = x.asset_id
)
SELECT *
FROM scored
ORDER BY total_score DESC, alert_id;
```

## Quick grading guidance for Day 2 writing
The Day 2 memo should sound like an escalation handoff.

### A strong Day 2 memo should usually do these things
- identify one alert ID clearly
- explain why the alert stands out using severity, confidence, and context
- mention the affected asset in a meaningful way
- recommend one next step that another analyst or lead could actually take
- explain briefly why judgment still matters beyond a numeric score
- include one sentence about monitoring boundaries or privacy

### A weak Day 2 memo often sounds like this
- only repeats the score
- does not explain why the asset matters
- gives no next step
- uses generic wording like `this seems bad`
- forgets that monitoring still needs governance

### Fast Day 2 grading rubric
- Full credit:
  clear alert choice, solid priority logic, asset-aware reasoning, practical next step, privacy-aware sentence
- Partial credit:
  acceptable alert choice but shallow explanation or vague next step
- Low credit:
  mostly restates the queue without ranking or justification

## What to emphasize while teaching the Day 1 and Day 2 labs

### Emphasize on Day 1
- Pattern shape matters.
- Sequence matters.
- Context matters.
- One clear first action is better than a vague dramatic response.

### Emphasize on Day 2
- A score is helpful, not sacred.
- Asset context changes urgency.
- Escalation is a communication task.
- Security monitoring still needs boundaries.

## Good whole-class questions that do not require group work
You said no group work, so these are whole-class or individual response questions.

### Day 1 questions
- What pattern makes you think this is a password spray instead of one user mistake?
- Which single row in the Day 1 dataset matters most, and why?
- Why is `u_admin_fin` more important than `u_student4` in this context?
- What first action reduces risk fastest without overclaiming the evidence?

### Day 2 questions
- Why is `A1006` stronger than `A1004`, even before a full investigation?
- What does the score help with, and what can the score miss?
- Why might `A1007` still deserve attention even if it is not the top score?
- What makes an escalation memo useful to the next analyst or incident lead?

## Practical phrasing you can use in class
These are simple lines you can use out loud.

### Good instructor lines for Day 1
- `Analytics starts with pattern recognition, not magic.`
- `Do not ask only what happened. Ask what repeats.`
- `A single row can be weak evidence. A sequence is often stronger.`
- `Context is what turns suspicious data into urgent data.`
- `Your first action should reduce risk, not perform theater.`

### Good instructor lines for Day 2
- `Triage is how analysts spend limited attention wisely.`
- `Severity is not the same thing as impact.`
- `A score can organize work, but it cannot replace thinking.`
- `If someone else cannot act on your note, the analytics work is incomplete.`
- `Monitoring can be necessary without becoming limitless.`

## Common misconceptions across the week

### Misconception: more data is always better
Correction:
- More data can increase storage cost, privacy risk, analyst noise, and alert fatigue.
- Better collection is usually more useful than indiscriminate collection.

### Misconception: analytics means prediction only
Correction:
- Descriptive and diagnostic analytics are already central in security operations.
- Counting, filtering, grouping, and baselining are all analytics.

### Misconception: an alert is basically proof
Correction:
- Alerts are signals, not verdicts.
- They need context, corroboration, and judgment.

### Misconception: professional writing is separate from technical skill
Correction:
- In operations work, writing is how technical reasoning becomes usable to a team.
- A weak note can waste strong analysis.

## How to pace the week

### Day 1 pacing suggestion for a full hour lecture before lab
- 5 min: frame Week 11 and explain why analytics matters
- 10 min: define security analytics, telemetry sources, events/alerts/incidents
- 10 min: authentication logs, fields, counts, sequence, pattern types
- 10 min: baseline and enrichment
- 10 min: Day 1 worked examples from the CSVs
- 10 min: first-action logic, false positives, privacy limits
- 5 min: transition into lab instructions

### Day 2 pacing suggestion for a full hour lecture before lab
- 5 min: recap Day 1
- 10 min: triage, severity, confidence, impact
- 10 min: asset context and business relevance
- 10 min: scoring model and its limitations
- 10 min: worked alert-queue example
- 10 min: escalation and queue health
- 10 min: privacy boundaries and memo expectations

## If students ask harder questions

### What if students ask, "Why not just automate all of this?"
Answer:
- Many parts can be automated.
- But alert quality, business context, false positives, and response tradeoffs still require human judgment.
- Automation changes the workflow; it does not eliminate the need for reasoning.

### What if students ask, "Is impossible travel always a serious problem?"
Answer:
- No.
- It can be noisy due to VPNs, mobile networks, stale IP geolocation, or data lag.
- That is exactly why confidence and context matter.

### What if students ask, "Why keep logs if they are also a privacy risk?"
Answer:
- Because organizations need evidence for detection, investigation, and accountability.
- The privacy question is not whether to log anything.
- The privacy question is what to log, why, who can see it, and how long it should be retained.

### What if students ask, "How is this different from data science?"
Answer:
- Security analytics borrows from data analysis broadly, but it is oriented toward operational decisions under uncertainty, often with incomplete and time-sensitive evidence.
- It also has stronger ties to incident response, monitoring, and governance.

## Final teaching priority
If you have to reduce the week to the single most important lesson, it is this:

`Security analytics is the disciplined process of turning partial operational data into proportional, explainable security action.`

That sentence captures:
- data
- uncertainty
- proportionality
- communication
- judgment
- ethics

If students understand that, the week is doing its job.

## Source list
Primary or official sources used for this guide:
- [NIST SP 800-92: Guide to Computer Security Log Management](https://csrc.nist.gov/pubs/sp/800/92/final)
- [NIST SP 800-137: Information Security Continuous Monitoring](https://csrc.nist.gov/pubs/sp/800/137/final)
- [NIST SP 800-61 Rev. 3: Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final)
- [NIST SP 800-63B: Digital Identity Guidelines - Authentication and Lifecycle Management](https://pages.nist.gov/800-63-4/sp800-63b.html)
- [MITRE ATT&CK: Brute Force (T1110)](https://attack.mitre.org/techniques/T1110/)
- [MITRE ATT&CK: Password Spraying (T1110.003)](https://attack.mitre.org/techniques/T1110/003/)
- [MITRE ATT&CK: Credential Stuffing (T1110.004)](https://attack.mitre.org/techniques/T1110/004/)
- [MITRE ATT&CK: Multi-Factor Authentication Request Generation (T1621)](https://attack.mitre.org/techniques/T1621/)
- [MITRE ATT&CK: Authentication Logs Data Component](https://attack.mitre.org/datacomponents/DC0002/)
- [MITRE ATT&CK Mitigation: Account Use Policies (M1036)](https://attack.mitre.org/mitigations/M1036/)
- [NIST Privacy Framework](https://www.nist.gov/privacy-framework)
- [NISTIR 8062: Privacy Engineering and Risk Management](https://www.nist.gov/publications/privacy-engineering-and-risk-management-federal-systems)
