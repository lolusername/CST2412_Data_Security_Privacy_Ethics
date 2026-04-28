# Week 12 Day 1 Lab: Reading Security Metrics

**Course:** CST 2412 Data Security, Privacy, and Ethics  
**Work mode:** Individual only  
**Time:** 25-30 minutes  
**File:** `week_12/data/week12_security_metrics.csv`  
**What you submit:** Short answers and one short analyst note

## Purpose
This lab is meant to be easy and practical.
You are not proving that an incident happened.
You are practicing how a security analyst reads a small table, compares signals, and writes a clear first judgment.

## Scenario
You are a junior security analyst reviewing a small daily metrics export.
Each row represents one system.

Your job is to decide:
- which systems deserve attention first
- what evidence supports that decision
- what privacy boundary should limit monitoring

You may use Excel, Google Sheets, Numbers, VS Code, or the Week 11 notebook.
You are **not required to code**.

## Part 1: Understand the Table
Answer in **one sentence each**.

1. What does one row in the CSV represent?
2. Which columns tell you whether a system is important to the organization?
3. Which columns suggest possible account compromise or suspicious login behavior?
4. Which column reminds you that alerts alone do not tell the whole story?

## Part 2: Use a Simple Priority Score
Use this simple scoring guide.

| Condition | Points |
|---|---:|
| `highest_alert_severity` is `high` | 2 |
| `highest_alert_severity` is `medium` | 1 |
| `asset_criticality` is `high` | 2 |
| `asset_criticality` is `medium` | 1 |
| `internet_exposed` is `yes` | 1 |
| `sensitive_data` is `yes` | 1 |
| `failed_logins_24h` is 30 or more | 1 |
| `successful_logins_after_failures` is greater than 0 | 1 |
| `mfa_denials` is 5 or more | 1 |
| `malware_alerts` is greater than 0 | 1 |

Complete this table for at least **five** systems.

| asset_id | system_name | total score | strongest reason this system matters |
|---|---|---:|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

Then answer:

1. Which system has the highest priority based on your score?
2. Which system would you personally review first?
3. If your answer to question 1 and question 2 are different, explain why. If they are the same, explain why the score seems reasonable.

## Part 3: Signal vs. Context
Fill in the table.

| Item | Signal, context, or both? | Why? |
|---|---|---|
| `failed_logins_24h` |  |  |
| `sensitive_data` |  |  |
| `internet_exposed` |  |  |
| `notes` |  |  |

## Part 4: Write a Short Analyst Note
Write **120-160 words** as if you are sending a note to a supervisor.

Use this structure:

1. `I reviewed the daily security metrics export.`
2. `The system I would review first is...`
3. `The strongest evidence is...`
4. `My first recommended action is...`
5. `One privacy boundary we should maintain is...`

## Part 5: Final Project Connection
Answer in **2-3 sentences**.

How could a small table like this become a final project?

Choose one:
- a coding project that analyzes security metrics
- a research essay about security monitoring, privacy, and ethics

## Grading
Full credit if your submission:
- completes the required short answers
- scores at least five systems
- explains one priority choice using evidence
- includes a privacy boundary
- connects the lab to a possible final project
