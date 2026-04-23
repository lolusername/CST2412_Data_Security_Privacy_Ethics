# Week 11: Data Analytics for Security

## Week focus
Week 11 begins the syllabus unit on **Data Analytics for Security**.
The emphasis this week is practical, individual skill building rather than group work.

Core thread for the week:
- read security data as evidence rather than noise
- distinguish events, alerts, and incidents
- build basic analyst habits: filtering, counting, prioritizing, and justifying action
- connect technical analysis to privacy, retention, and documentation choices
- practice career-connected writing that sounds like real entry-level security work

## Syllabus alignment
From `CST_2412.pdf`:
- Topic: Data Analytics for Security
- Reading: Selected reading

## Work mode
All Week 11 activities are **individual**.
There is **no group work** in either class meeting.

## Recommended class flow

### Day 1: Logs, Events, and Detection Basics
1. Lecture deck (25-30 min): what security analytics is, where data comes from, and how analysts find suspicious patterns
2. Individual skill-building lab (35-45 min): students inspect authentication events and user context in CSV form
3. Career-connected writing response (10-15 min): short SOC-style shift note based on the lab

### Day 2: Alert Triage, Prioritization, and Escalation
1. Mini lecture (10-15 min): use selected Day 2 slides to explain severity, confidence, asset context, and the simple score
2. Individual skill-building lab (50-60 min): students spend most of class triaging a fictional alert queue with a guided worksheet
3. Short exit writing (5-8 min): students write a brief escalation note based on the lab

## Week 11 files

### Day 1
- `week_11/week11_day1_security_analytics_foundations.pptx`
  Student-facing Day 1 lecture deck with word-for-word notes.
- `week_11/lab_day1_log_analysis.md`
  Individual lab on reading login events, spotting suspicious patterns, and choosing a first action.
- `week_11/day1_writing_response.md`
  Career-connected Day 1 writing prompt in the form of a junior SOC analyst shift note.
- `week_11/data/day1_auth_events.csv`
  Authentication event data for the Day 1 lab.
- `week_11/data/day1_user_context.csv`
  User and account context for the Day 1 lab.

### Day 2
- `week_11/week11_day2_alert_triage_and_escalation.pptx`
  Student-facing Day 2 lecture deck with word-for-word notes.
- `week_11/lab_day2_alert_triage.md`
  Easier guided individual lab on prioritizing alerts with severity, confidence, and asset context.
- `week_11/day2_writing_response.md`
  Shorter Day 2 exit memo in the form of a simple escalation note.
- `week_11/data/day2_alert_queue.csv`
  Alert queue data for the Day 2 lab.
- `week_11/data/day2_asset_context.csv`
  Asset context for the Day 2 lab.

### Notebook
- `week_11/week11_pandas_duckdb_examples.ipynb`
  Companion notebook for code-based examples using the Week 11 CSVs.
  Open in Colab:
  [week11_pandas_duckdb_examples.ipynb](https://colab.research.google.com/github/lolusername/CST2412_Data_Security_Privacy_Ethics/blob/main/week_11/week11_pandas_duckdb_examples.ipynb)

## Instructor note
Week 11 works best if students leave class with two concrete habits:
1. they can explain why a pattern looks suspicious using evidence from a table, and
2. they can write a short professional security note that justifies next steps clearly.

That keeps the analytics unit grounded in real analyst workflow instead of abstract buzzwords.
