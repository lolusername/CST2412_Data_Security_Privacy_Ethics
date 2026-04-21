# Week 11 Day 2 Individual Lab: Alert Triage, Risk Scoring, and Escalation

**Course:** CST 2412 Data Security, Privacy, and Ethics  
**Work mode:** Individual only  
**What you submit:** 1 document with short answers  
**Files you will use:** `day2_alert_queue.csv` and `day2_asset_context.csv`

## What you'll learn
By the end of this lab, you should be able to:
- read an alert queue the way an entry-level analyst would
- enrich alert data with asset context
- use a simple scoring method to prioritize work
- separate high-priority escalation from lower-priority noise
- communicate one escalation decision clearly

## Background scenario
You are working as a **Tier 1 security analyst** reviewing a small morning alert queue.
You do not have time to investigate everything at once.
Your job is to decide what should be escalated first, what can wait, and what may be low-priority noise.

## Files
- `day2_alert_queue.csv`
  Contains a fictional alert queue with severity, confidence, alert type, user, and asset information.
- `day2_asset_context.csv`
  Contains business context about each asset, including criticality, internet exposure, and whether sensitive data is involved.

## Part 1 — Read the queue
Answer in **1 sentence each**:

1. What does one row in `day2_alert_queue.csv` represent?
2. Which column seems most useful for estimated technical seriousness?
3. Which column seems most useful for estimated confidence?
4. Which file tells you whether an asset is high value to the organization?

## Part 2 — Use a simple score
For each alert, compute this score:

- `severity`: high = 3, medium = 2, low = 1
- `confidence`: high = 3, medium = 2, low = 1
- `asset_criticality`: high = 3, medium = 2, low = 1
- add `1` if `internet_exposed = yes`
- add `1` if `sensitive_data = yes`

### What to submit for this part
Create a small table with:
- `alert_id`
- `total score`

Then answer:
1. Which alert has the highest score?
2. Which **three** alerts should be reviewed first?

## Part 3 — Do not trust the score blindly
Pick **one** alert that is **not** in your top three and explain why it might still deserve attention.
Then pick **one** alert that might be low-priority or a likely false positive.

Write **2-3 sentences** for each choice.

## Part 4 — Escalate one alert
Choose the **single** alert you would escalate first.
Then answer:

1. What is the `alert_id`?
2. What asset is involved?
3. Why does this alert matter more than the others right now?
4. What is the first follow-up step you would request?

Write **4-6 sentences** total.

## Part 5 — Communication checkpoint
A good analyst does not just rank alerts. They explain the reasoning.
Write **3-4 sentences** answering this:

**Why is asset context important in security analytics, even when severity labels already exist?**

## Part 6 — Ethics checkpoint
Security monitoring can help reduce harm, but it can also expand surveillance.
Write **2-3 sentences** answering this:

**What is one reason alerting data should be retained, and what is one rule the organization should follow to avoid over-monitoring people?**

## What to submit
Your document must include these headings:
- Part 1: Queue reading
- Part 2: Risk score table
- Part 3: Beyond the score
- Part 4: Escalation choice
- Part 5: Asset context
- Part 6: Ethics checkpoint

## Grading rubric
Full credit if your work:
- calculates the score correctly
- prioritizes alerts in a defensible order
- shows judgment beyond the formula
- explains one escalation clearly
- includes an ethics-aware monitoring answer
