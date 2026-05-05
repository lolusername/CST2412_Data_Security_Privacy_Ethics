# Sample Final Project Report: Security Metrics Daily Summary

**Important:** This is an inspiration sample, not language to copy into your own final project.

## Project Question
How can a beginner security analyst use a small daily security metrics table to decide which system should be reviewed first?

## Dataset Description
This sample project uses the Week 12 class dataset, `week12_security_metrics.csv`. Each row represents one fictional system. The columns include system name, business unit, asset criticality, internet exposure, sensitive data, failed logins, successful logins after failures, multi-factor authentication denials, malware alerts, highest alert severity, and notes.

The dataset is fictional and designed for this class. Because it is fictional, it is useful for practicing analysis without exposing real users or real systems.

## What the Code Does
The code loads the CSV file from the course GitHub repository using pandas. It then creates a simple priority score. The score gives points for signals such as high alert severity, high asset criticality, internet exposure, sensitive data, repeated failed logins, successful logins after failures, multi-factor authentication denials, and malware alerts.

After calculating the score, the code sorts the systems from highest priority to lowest priority. It then creates a summary table with the most important columns so the result is easier to explain in a short report.

## Findings
One finding is that the highest-priority systems are not necessarily the systems with the most alerts. A system becomes more important when alert severity is combined with business context, sensitive data, and exposure.

A second finding is that successful logins after failures deserve special attention. Failed logins alone can happen for normal reasons, but a successful login after repeated failures can suggest that someone eventually guessed, reused, or obtained a valid password.

A third finding is that the notes column matters because numbers do not explain everything. The notes column can show whether an alert happened during normal activity, whether there was a maintenance window, or whether the system contains sensitive records.

## Recommendation
The organization should review the highest-scoring systems first, especially systems that combine high criticality, sensitive data, internet exposure, high alert severity, and successful logins after failures. The review should begin with a narrow check of authentication logs, multi-factor authentication evidence, and recent account activity.

## Privacy or Ethics Concern
Security metrics can help protect systems, but they can also become excessive monitoring if an organization collects more user activity than it needs. A privacy-aware approach should collect only the logs needed for security, limit who can view them, and avoid using security data for unrelated employee or student surveillance.

## Limitation
This sample project cannot prove that an incident happened. The score is a simple prioritization tool, not a full investigation. The dataset is small and fictional, and the scoring method is based on class logic rather than a professional detection model. A real organization would need more evidence before making a serious incident decision.

## Entry-Level Job Connection
This project resembles an entry-level security analyst task: reviewing a daily metrics export, ranking systems by priority, explaining the evidence, and recommending a first action.
