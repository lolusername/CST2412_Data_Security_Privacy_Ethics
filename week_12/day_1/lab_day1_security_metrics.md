# Week 12 Day 1 Lab: Campus Systems Security Metrics

**Course:** CST 2412 Data Security, Privacy, and Ethics  
**Work mode:** Individual only  
**Time:** Most of class  
**Dataset:** `week_12/day_1/data/week12_security_metrics.csv`  
**Dataset name:** Campus Systems Daily Security Metrics  
**What you submit:** One document with Parts 1-7 completed

## Important
You do **not** need to choose a dataset for this lab.

Use the provided class dataset:

`week_12/day_1/data/week12_security_metrics.csv`

This dataset is fictional, beginner-friendly, and designed for this class. It is relevant because it looks like the kind of daily security metrics export a junior analyst might review before deciding what needs attention first.

## Purpose
This lab is meant to be easy, practical, and directly connected to the final project.

You are not proving that an incident happened.
You are practicing how a security analyst reads a small table, compares signals, considers context, and writes a clear first judgment.

By the end of the lab, you should have:
- read a security metrics dataset
- scored several systems by priority
- identified one system to review first
- explained the evidence behind your choice
- named one privacy boundary for security monitoring
- written a short analyst-style note that could inspire a final project

## Scenario
You are a junior security analyst for a fictional college.

The college has exported one daily security metrics table for ten campus systems. Each row represents one system.

The security team wants a first-pass review. Your job is to decide:
- which systems deserve attention first
- what evidence supports that decision
- what privacy boundary should limit monitoring
- how this kind of analysis could become a small final project

## Tools
Use any tool you already know:
- Excel
- Google Sheets
- Numbers
- VS Code table view
- a CSV viewer
- the Week 11 notebook
- Python, only if you want to

You are **not required to code**.

## Part 1: Open the Dataset
Open:

`week_12/day_1/data/week12_security_metrics.csv`

Answer in **one sentence each**.

1. What does one row in this dataset represent?
2. How many systems are listed?
3. Which column tells you the system name?
4. Which column tells you the business unit?
5. Which column gives plain-English context that numbers alone may not explain?

## Part 2: Understand the Columns
Fill in the table.

| Column | What it means in plain English | Signal, context, or both? |
|---|---|---|
| `asset_criticality` |  |  |
| `internet_exposed` |  |  |
| `sensitive_data` |  |  |
| `failed_logins_24h` |  |  |
| `successful_logins_after_failures` |  |  |
| `mfa_denials` |  |  |
| `malware_alerts` |  |  |
| `highest_alert_severity` |  |  |
| `notes` |  |  |

Use these definitions:

- **Signal:** something that may show suspicious activity or a security event
- **Context:** information that explains why the system matters
- **Both:** information that can act as evidence and also help interpret other evidence

## Part 3: Use a Simple Priority Score
Use this scoring guide.

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

### Worked example
Use `S001 Student Portal`.

| Reason | Points |
|---|---:|
| high alert severity | 2 |
| high asset criticality | 2 |
| internet exposed | 1 |
| sensitive data | 1 |
| failed logins are 30 or more | 1 |
| successful logins after failures is greater than 0 | 1 |
| MFA denials are 5 or more | 1 |
| malware alerts greater than 0 | 0 |
| **Total** | **9** |

So `S001 Student Portal` has a priority score of **9**.

## Part 4: Score All Ten Systems
Complete the table for all ten systems.

| asset_id | system_name | total score | strongest reason this system matters |
|---|---|---:|---|
| S001 | Student Portal | 9 | repeated failures, successful logins after failures, sensitive data, and high criticality |
| S002 |  |  |  |
| S003 |  |  |  |
| S004 |  |  |  |
| S005 |  |  |  |
| S006 |  |  |  |
| S007 |  |  |  |
| S008 |  |  |  |
| S009 |  |  |  |
| S010 |  |  |  |

## Part 5: Choose What To Review First
Answer in short paragraphs.

1. Which system has the highest priority score?
2. Which system would you personally review first?
3. If your answer to Questions 1 and 2 are different, explain why. If they are the same, explain why the score seems reasonable.
4. Which system might look noisy but lower priority? Explain why.
5. Which system has sensitive data but not many obvious security signals? Explain why that still matters.

Helpful hint:
- A system can be noisy because it has many failed logins.
- A system can be high priority because it combines security signals with sensitive data, high criticality, or internet exposure.

## Part 6: Privacy and Ethics Boundary
Security monitoring can protect systems, but it can also become excessive.

Answer in **3-5 sentences**:

1. What is one reason the college should collect login and alert metrics?
2. What is one privacy risk if the college collects or keeps too much monitoring data?
3. What rule should limit how the security team uses this data?

Examples of privacy boundaries:
- use logs only for security and reliability work
- limit who can view detailed user activity
- keep logs only as long as needed
- avoid using security logs for unrelated discipline or surveillance
- summarize data when detailed user-level data is not needed

## Part 7: Write a Short Analyst Note
Write **150-220 words** as if you are sending a note to a supervisor.

Use this structure:

1. `I reviewed the Campus Systems Daily Security Metrics dataset.`
2. `The system I would review first is...`
3. `The strongest evidence is...`
4. `My first recommended action is...`
5. `One system that looks noisy but may be lower priority is...`
6. `One privacy boundary we should maintain is...`

## Final Project Connection
Answer in **3-4 sentences**:

How could this lab become a beginner security analyst coding final project?

Your answer should mention:
- the dataset
- one simple code action, such as sorting, scoring, grouping, or charting
- one finding
- one privacy or ethics concern

## What To Submit
Submit one document with:
- Part 1: open the dataset
- Part 2: understand the columns
- Part 4: score all ten systems
- Part 5: review-first answers
- Part 6: privacy and ethics boundary
- Part 7: analyst note
- Final Project Connection

## Grading
Full credit if your submission:
- uses the provided Week 12 Day 1 dataset
- scores all ten systems
- explains one priority choice using evidence
- identifies one noisy or lower-priority system
- includes a privacy boundary
- connects the lab to the final project
