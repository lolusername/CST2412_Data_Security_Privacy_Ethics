# Week 14 Day 2 Lab: Privacy Incident Detective

**Course:** CST 2412 Data Security, Privacy, and Ethics  
**Work mode:** Individual only  
**Due:** End of class  
**What you submit:** One document with Parts 1-7 completed  
**Final project due date:** May 26, 2026

## Purpose
Today is a fictional privacy incident investigation.

You are the incident detective. Your job is not to panic, blame people, or make the story dramatic. Your job is to use evidence to answer practical security, privacy, and ethics questions:

- What happened?
- What data was exposed?
- Who could be affected?
- What should be done first?
- What should be changed so it is less likely to happen again?

This class connects to the syllabus themes of data security, privacy, law and ethics, cloud computing, governance, access control, and risk management.

## Case File: CampusQuest Rewards
CampusQuest Rewards is a fictional student app that gives points for attending campus events. A small team exported a CSV from the app database so they could test a dashboard.

The CSV was placed in cloud storage. Someone changed the sharing setting from `private` to `public link`. The link was posted in a test chat and later indexed by a search engine.

A student emailed the help desk after finding the CSV online.

## Evidence Cards
Use the evidence below. Treat it like a case file.

### Evidence A: What the CSV Contains
| Column | Example value | Notes |
|---|---|---|
| student_name | Maya Chen | full name |
| school_email | maya.chen@example.edu | school email |
| student_id_last4 | 4821 | last four digits only |
| major | Data Science | academic program |
| event_points | 180 | reward points |
| last_login_date | 2026-05-09 | recent activity |
| help_request_note | asked about disability seating | free-text note |
| consent_status | yes | app consent checkbox |

### Evidence B: What Was Not in the CSV
The CSV did **not** include passwords, full student ID numbers, Social Security numbers, grades, payment cards, home addresses, or medical records.

### Evidence C: Access Clues
| Clue | Detail |
|---|---|
| Public link created | May 8, 2026 at 3:12 PM |
| Public link discovered by student | May 13, 2026 at 9:40 PM |
| Link disabled | May 14, 2026 at 10:05 AM |
| Logged downloads | 138 total downloads |
| Unknown IP addresses | 41 downloads from unfamiliar networks |
| Confirmed internal downloads | 97 downloads from campus and vendor networks |

### Evidence D: People Involved
| Person or team | Detail |
|---|---|
| Student reporter | Found the public link and emailed help desk |
| Dashboard intern | Exported the CSV for testing |
| Vendor support | Asked for sample data to troubleshoot dashboard bug |
| App owner | Approved dashboard testing but did not approve public sharing |
| IT help desk | Disabled the link after receiving the report |

### Evidence E: The Red Herring
One rumor says, “Passwords were leaked.” The evidence file does not support that claim. No password field appears in the CSV, and there is no evidence that the app login database was accessed.

A rumor can still cause fear, but your incident write-up should separate confirmed facts from assumptions.

## Part 1: Confirmed Facts vs. Assumptions
Fill in the table.

| Confirmed fact from the evidence | Assumption or unknown that still needs checking |
|---|---|
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |

## Part 2: Data Classification
Classify each field as `low`, `medium`, or `high` concern. Then explain why.

| Field | Concern level | Why? |
|---|---|---|
| student_name |  |  |
| school_email |  |  |
| student_id_last4 |  |  |
| major |  |  |
| event_points |  |  |
| last_login_date |  |  |
| help_request_note |  |  |
| consent_status |  |  |

Answer in 3-4 sentences:

Which field creates the biggest privacy or ethics concern? Why?

## Part 3: Incident Timeline
Put the events in order and write a one-sentence explanation of why the timeline matters.

| Order | Event |
|---|---|
|  | CSV exported for dashboard testing |
|  | Public link created |
|  | Student discovers link |
|  | Help desk receives report |
|  | Link disabled |
|  | Incident review begins |

Timeline explanation:

## Part 4: Triage Score
Use this simple score to decide how serious the incident is.

Rate each category from `1` to `5`.

| Category | Score | Why? |
|---|---|---|
| Data sensitivity |  |  |
| Exposure level |  |  |
| Confidence in evidence |  |  |
| Possible harm to students |  |  |
| Urgency |  |  |

Total score:

Interpret your total:

- `5-10`: low concern, document and monitor
- `11-17`: moderate concern, contain and notify internal stakeholders
- `18-25`: high concern, urgent response and careful communication

My incident severity is:

## Part 5: First-Hour Response Plan
Choose **five** actions the organization should take first.

| Action | Why this matters |
|---|---|
| Disable the public link |  |
| Preserve logs and evidence |  |
| Identify exactly what data was exposed |  |
| Identify who had access to the link |  |
| Reset passwords |  |
| Contact legal/privacy office |  |
| Notify every student immediately |  |
| Confirm whether passwords were actually involved |  |
| Review cloud storage permissions |  |
| Delete all logs immediately |  |

Which action from the list is a bad idea or premature? Why?

## Part 6: Write a Plain-Language Incident Update
Write **120-180 words** to affected students.

Your update should include:

- what happened
- what information was involved
- what the organization already did
- what is still being checked
- what students can do or watch for
- a calm tone that does not exaggerate or hide the issue

Draft update:

## Part 7: Prevention and Ethics
Choose **three** controls that would reduce the chance of this happening again.

| Control | How it helps |
|---|---|
| Cloud storage private by default |  |
| Access review before sharing files |  |
| Use fake or minimized test data |  |
| Remove free-text notes from exports |  |
| Retention rule: delete test exports after 7 days |  |
| Logging and alerting for public links |  |
| Vendor data-sharing checklist |  |
| Training for interns and staff |  |

Write **100-150 words**:

What is the main ethics lesson from this case?

## Exit Ticket
Answer in short sentences.

1. What was the most important confirmed fact?
2. What was the most dangerous assumption or rumor?
3. What was the strongest first-hour action?
4. What control would best prevent a repeat incident?
5. How could this case connect to your final project topic, if useful?

## What To Submit
Submit one document with:

- Part 1: facts vs. assumptions
- Part 2: data classification
- Part 3: incident timeline
- Part 4: triage score
- Part 5: first-hour response plan
- Part 6: incident update
- Part 7: prevention and ethics
- exit ticket

## Grading
Full credit if:

- you use evidence from the case file
- you separate facts from assumptions
- you classify the data thoughtfully
- you choose realistic response actions
- your incident update is clear and calm
- you submit by the end of class
