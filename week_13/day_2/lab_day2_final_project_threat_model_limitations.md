# Week 13 Day 2 Lab: Final Project Threat Model, Limits, and Recommendation

**Course:** CST 2412 Data Security, Privacy, and Ethics  
**Work mode:** Individual only  
**Due:** End of class  
**What you submit:** One document with Parts 1-6 completed  
**Final project due date:** May 26, 2026

## Purpose
Today you will use the idea of **model evasion** to make your final project more realistic.

Model evasion means that a system can be fooled at the moment it is used. A spam filter can miss a spam message. A login risk score can miss a suspicious login. A policy can look good on paper but fail when people route around it.

You do not need to build a machine learning model today. Your job is to ask:

**How could the system, dataset, policy, or recommendation in my final project fail?**

## Notebook Support
Use the shared Week 13 Colab notebook if you need a concrete example:

[Open the Week 13 notebook in Colab](https://colab.research.google.com/github/lolusername/CST2412_Data_Security_Privacy_Ethics/blob/main/week_13/week13_data_poisoning_evasion_colab.ipynb)

The notebook shows how thresholds, false positives, false negatives, and evasion can affect a simple security priority ranking. You may use it to help draft your limitation and recommendation.

## Part 1: Restate Your Final Project
Answer in short sentences.

1. My project path is:
2. My current project question is:
3. The system, technology, dataset, or issue I am studying is:
4. The main security issue is:
5. The main privacy or ethics issue is:

## Part 2: Mini Threat Model
A threat model is a structured way to ask what can go wrong.

Fill in the table.

| Question | Your answer |
|---|---|
| What needs protection? |  |
| Who or what could cause harm? |  |
| What mistake, weakness, or gap could be exploited? |  |
| What would the harm be? |  |
| Who would be affected? |  |
| What control or recommendation could reduce the risk? |  |

Keep this simple. You are not writing a professional security assessment. You are building one clear paragraph for your final project.

## Part 3: Evasion Thinking
Answer each question in **2-3 sentences**.

1. If someone wanted to avoid detection, monitoring, rules, or accountability in your topic, what might they try?
2. What signal might your project rely on too much?
3. What could create a false positive, where something normal looks risky?
4. What could create a false negative, where something risky looks normal?

Examples:
- A normal user forgets a password and creates many failed logins.
- A risky login succeeds because it happens from a familiar device.
- A dataset misses incidents that were never reported.
- A policy misses harm because it only measures technical success.
- A classification system treats a category as neutral when the category has bias built into it.

## Part 4: Write a Limitation Section
Write **120-180 words**.

Prompt:

**What is one important limitation of my final project?**

Your limitation should explain:
- what your project can show
- what your project cannot prove
- why that limit matters
- how you will avoid overclaiming

Sentence starter:

`One limitation of this project is...`

## Part 5: Write a Realistic Recommendation
Write one recommendation that is specific enough to be useful.

Weak recommendation:

`Organizations should improve security.`

Stronger recommendation:

`The organization should review high-risk login events that combine repeated failures, successful login after failure, sensitive accounts, and missing multi-factor authentication evidence.`

Fill this in:

1. My recommendation is:
2. The evidence that supports it is:
3. The security benefit is:
4. The privacy or ethics tradeoff is:
5. One reason this recommendation is realistic is:

## Part 6: Exit Ticket
Write **80-120 words**.

Prompt:

**What is one recommendation I can defend, and what is one limitation I need to admit?**

## What To Submit
Submit one document with:
- Part 1: project restatement
- Part 2: mini threat model
- Part 3: evasion thinking
- Part 4: limitation section
- Part 5: recommendation
- Part 6: exit ticket

## Grading
Full credit if:
- your threat model is connected to your final project
- you explain false positive or false negative risk
- you write one limitation
- you write one realistic recommendation
- you submit by the end of class
