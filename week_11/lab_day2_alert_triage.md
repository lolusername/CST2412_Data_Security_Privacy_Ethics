# Week 11 Day 2 Individual Lab: Guided Alert Triage

**Course:** CST 2412 Data Security, Privacy, and Ethics  
**Work mode:** Individual only  
**What you submit:** 1 document with short answers and one small score table  
**Files you will use:** `day2_alert_queue.csv` and `day2_asset_context.csv`

## What you'll learn
By the end of this lab, you should be able to:
- read a small alert queue
- use asset context to understand why one alert matters more than another
- apply a simple score to organize your thinking
- choose one alert to escalate first
- write a short analyst-style note

## Background scenario
You are working as a **Tier 1 security analyst** reviewing a small morning alert queue.
You do **not** have time to fully investigate every alert.
Your job is to decide:
- what deserves attention first
- what can wait
- what may be lower priority

## Files
- `day2_alert_queue.csv`
  Contains the alert queue.
- `day2_asset_context.csv`
  Contains business context about the systems involved.

## Before you start
Use any tool you want:
- Excel
- Google Sheets
- Numbers
- VS Code
- the Week 11 notebook

You are **not** required to code.

## Simple score for today
Use this score for each alert:

- `severity`: high = 3, medium = 2, low = 1
- `confidence`: high = 3, medium = 2, low = 1
- `asset_criticality`: high = 3, medium = 2, low = 1
- add `1` if `internet_exposed = yes`
- add `1` if `sensitive_data = yes`

This score is just a starting point.
It helps organize the queue, but it does **not** replace judgment.

## Part 1 — Read the files
Answer in **1 sentence each**:

1. What does one row in `day2_alert_queue.csv` represent?
2. Which file tells you whether the asset is high value to the organization?
3. Which two columns are most useful for a quick first estimate of technical seriousness?

## Part 2 — Fill in the score table
Copy this table into your document and complete it.

| alert_id | severity points | confidence points | criticality points | internet exposed bonus | sensitive data bonus | total score |
|---|---:|---:|---:|---:|---:|---:|
| A1001 |  |  |  |  |  |  |
| A1002 |  |  |  |  |  |  |
| A1003 |  |  |  |  |  |  |
| A1004 |  |  |  |  |  |  |
| A1005 |  |  |  |  |  |  |
| A1006 |  |  |  |  |  |  |
| A1007 |  |  |  |  |  |  |
| A1008 |  |  |  |  |  |  |

Then answer:

1. Which alert has the highest score?
2. Which **three** alerts would you review first?

## Part 3 — Use judgment, not just the score
Answer these in **2-3 sentences each**:

1. Pick **one** alert that is **not** your highest score but still deserves attention. Why?
2. Pick **one** alert that seems lower priority. Why?

## Part 4 — Choose one escalation
Choose the **single** alert you would escalate first.

Answer these:

1. `Escalated alert:`
2. `Asset involved:`
3. `Why this alert stands out:`
4. `First next step:`

Write **4-5 sentences total**.

## Part 5 — Quick context check
Answer in **2-3 sentences**:

**Why is asset context important in security analytics, even when severity labels already exist?**

## Part 6 — Short ethics checkpoint
Answer in **1-2 sentences**:

**What is one rule the organization should follow so security monitoring does not become excessive surveillance?**

## What to submit
Your document must include these headings:
- Part 1: Read the files
- Part 2: Score table
- Part 3: Use judgment
- Part 4: Choose one escalation
- Part 5: Context check
- Part 6: Ethics checkpoint

## Grading rubric
Full credit if your work:
- completes the score table correctly
- identifies a reasonable top alert
- shows judgment beyond the score
- explains one escalation clearly
- includes a short monitoring-boundary answer
