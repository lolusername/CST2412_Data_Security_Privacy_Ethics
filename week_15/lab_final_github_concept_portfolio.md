# Final Lab: Create a GitHub Concept Portfolio Artifact

**Course:** CST 2412 Data Security, Privacy, and Ethics  
**Class date:** May 19, 2026  
**Work mode:** Individual only  
**Due:** End-of-class checkpoint  
**Final project due date:** May 26, 2026

## Purpose
Today you will create a small GitHub artifact that explains **one concept from this class**.

This is meant to help you after the course. A clear GitHub artifact can show an interviewer, internship reviewer, or future professor that you can explain a security/privacy concept in your own words.

You may choose either path:

1. **Markdown guide path:** create a `README.md` that teaches one concept.
2. **Code + explanation path:** create a small code example or notebook plus a `README.md` that explains what the code demonstrates.

Both paths are valid.

## Step 1: Choose One Concept
Choose one concept from the course.

Good options:

- CIA triad: confidentiality, integrity, availability
- risk and threat modeling
- authentication and access control
- password hashing or password safety
- cryptography basics
- TLS and secure web connections
- web security and input validation
- network security basics
- databases, tables, JSON, and MongoDB documents
- cloud storage permissions
- data dictionaries
- privacy and data minimization
- algorithmic bias and classification
- security logs and alert triage
- false positives and false negatives
- data poisoning
- model evasion
- privacy incident response
- ethical use of security data

My concept:

## Step 2: Create or Choose a GitHub Space
Choose one:

- Create a new GitHub repository.
- Add a new folder to an existing class/practice repository.
- Draft the files locally or in Google Docs first, then upload after class.

Suggested repository name:

`cst2412-security-privacy-concept`

Suggested folder name if using an existing repository:

`cst2412-concept-guide`

## Step 3: Required README Structure
Create a `README.md` with these sections.

```markdown
# Concept Title

## What This Means
Explain the concept in beginner-friendly language.

## Why It Matters
Explain why this concept matters for security, privacy, or ethics.

## Simple Example
Give a small example from class, a fictional example, or a short code example.

## What Can Go Wrong
Explain one mistake, risk, false assumption, or harm.

## How To Talk About This In An Interview
Write 2-3 sentences you could say in a job interview.

## Connection To CST 2412
Name 2-3 course topics this concept connects to.
```

## Step 4A: Markdown Guide Path
If you are doing the Markdown guide path, add at least two of these:

- a table
- a short checklist
- a simple diagram written in text
- a glossary of 3-5 terms
- a “bad example vs. better example” comparison
- one sentence about privacy or ethics

Example table:

| Term | Plain meaning | Why it matters |
|---|---|---|
| False positive | Normal activity flagged as risky | Can waste analyst time or frustrate users |
| False negative | Risky activity missed by the system | Can allow harm to continue |

## Step 4B: Code + Explanation Path
If you are doing the code path, include one small code file or notebook.

Keep it simple. Good examples:

- a Python list or dictionary explaining security concepts
- a tiny CSV analysis using class-style data
- a password-strength checklist function
- a risk scoring table
- a data dictionary generator
- a false positive / false negative example

Your code must include comments that explain what each part does.

Example Python starter:

```python
# This is a tiny example, not a real security tool.
# It shows how a simple threshold can classify events as "review" or "no review".

events = [
    {"system": "Student Portal", "failed_logins": 42, "sensitive_data": True},
    {"system": "Lab Printer", "failed_logins": 2, "sensitive_data": False},
]

for event in events:
    # A threshold is a cutoff. Here, 10 or more failed logins means review.
    needs_review = event["failed_logins"] >= 10

    # Sensitive systems deserve extra attention, even when the number is small.
    if event["sensitive_data"]:
        needs_review = True

    print(event["system"], "needs review?", needs_review)
```

## Step 5: Interview Sentence
Write a short answer to this prompt:

**Tell me about something you learned in your data security, privacy, and ethics course.**

Use this structure:

1. I learned that...
2. I practiced this by...
3. This matters in a workplace because...

Draft answer:

## Step 6: Final Project Bridge
Answer in 3-4 sentences:

How could this GitHub artifact help you finish or explain your final project?

## Step 7: End-of-Class Submission
Submit one of these:

- a GitHub repository link
- a GitHub file link
- a Markdown file
- a screenshot or copied text of your draft if GitHub is not ready

## Exit Ticket
Answer in short sentences.

1. What concept did you explain?
2. What is the strongest section of your artifact so far?
3. What still needs revision?
4. What will you finish before the final project is due on May 26, 2026?

## Grading
Full credit if:

- your artifact explains one course concept clearly
- your README includes the required sections
- your work connects to security, privacy, or ethics
- your interview sentence is specific
- you submit an end-of-class checkpoint
