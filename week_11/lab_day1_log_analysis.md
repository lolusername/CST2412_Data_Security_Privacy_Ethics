# Week 11 Day 1 Individual Lab: Login Event Analysis and Detection Basics

**Course:** CST 2412 Data Security, Privacy, and Ethics  
**Work mode:** Individual only  
**What you submit:** 1 document with short answers  
**Files you will use:** `day1_auth_events.csv` and `day1_user_context.csv`

## What you'll learn
By the end of this lab, you should be able to:
- read basic authentication event data
- spot repeated failure patterns
- tell the difference between normal log noise and something worth investigating
- use account context to make a better decision
- write a short analyst-style justification for a first action

## Tools
Use any tool you already know how to use:
- spreadsheet software
- CSV viewer
- Google Sheets
- VS Code table view
- simple sorting/filtering in any app you prefer

You are **not** writing code for this lab unless you want to.
The goal is analyst reasoning, not programming.

## Background scenario
You are acting as a **junior SOC analyst** for a fictional college technology team.
The team collected one morning of authentication activity from several campus systems.
Your job is to decide whether the data shows a normal busy morning, a brute-force pattern, a password spray, or something else.

## Files
- `day1_auth_events.csv`
  Contains authentication activity such as login attempts, resets, and MFA outcomes.
- `day1_user_context.csv`
  Contains account context such as department, privilege level, and whether the account is sensitive.

## Part 1 — Read the fields first
Open both CSV files.
Answer these in **1 sentence each**:

1. What does one row in `day1_auth_events.csv` represent?
2. Which column seems most useful for tracking **where** activity came from?
3. Which column seems most useful for deciding **whether the account is sensitive**?

## Part 2 — Count the obvious patterns
Use sorting or filtering to answer these.
Write the exact value, not just a sentence.

1. How many rows show `login_failed`?
2. Which `src_ip` appears most often in failed logins?
3. How many different `user_id` values were targeted from that IP?
4. Does that pattern look more like:
   - one user forgetting a password,
   - a brute-force attack against one account, or
   - a password spray across many accounts?

Explain your choice in **2-3 sentences**.

## Part 3 — Find the risky success
Now look for a successful login that happens after repeated failures.
Answer:

1. Which `user_id` had a successful login after repeated failed attempts from the same source IP?
2. What was the `src_ip`?
3. Why is a success after many failures often more important than failures alone?

## Part 4 — Use account context
Open `day1_user_context.csv` and match the account you identified.
Answer:

1. What department is the account in?
2. Is the account marked as privileged?
3. Is the account marked as sensitive?
4. Why does this context change the urgency of the event?

Answer Question 4 in **2-3 sentences**.

## Part 5 — Recommend the first action
Pick **one** first action from this list:
- temporarily block the source IP
- require a password reset for the affected account
- force MFA re-verification
- open a full incident investigation
- continue monitoring without action

Then answer:
1. Which action did you choose?
2. Why is it the best **first** step instead of the others?
3. What is one tradeoff or downside of your choice?

Write **4-6 sentences** total.

## Part 6 — Privacy and logging checkpoint
Security analytics can help detect abuse, but logging also creates privacy obligations.
Answer in **2-3 sentences**:

**What is one reason the college should keep authentication logs, and what is one rule it should follow to avoid collecting or retaining too much information?**

## What to submit
Your document must include these headings:
- Part 1: Field reading
- Part 2: Pattern count
- Part 3: Risky success
- Part 4: Account context
- Part 5: First action
- Part 6: Privacy checkpoint

## Grading rubric
Full credit if your work:
- uses evidence from the CSV files
- correctly identifies the suspicious pattern
- uses context to justify urgency
- recommends a defensible first action
- includes a clear privacy checkpoint answer
