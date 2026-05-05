"""Sample final project: security metrics daily summary.

This script is for inspiration only. Do not copy the report wording into your
own final project. Use it to understand the scale and structure expected for a
beginner coding project.
"""

from pathlib import Path

import pandas as pd


# Raw GitHub URL for the Week 12 class dataset.
# A raw URL gives pandas direct access to the CSV file contents.
CSV_URL = (
    "https://raw.githubusercontent.com/lolusername/"
    "CST2412_Data_Security_Privacy_Ethics/main/"
    "week_12/day_1/data/week12_security_metrics.csv"
)


def yes_no_points(value: str) -> int:
    """Return 1 point for yes and 0 points for anything else."""
    return 1 if str(value).strip().lower() == "yes" else 0


def severity_points(value: str) -> int:
    """Convert an alert severity label into simple priority points."""
    severity = str(value).strip().lower()
    if severity == "high":
        return 2
    if severity == "medium":
        return 1
    return 0


def criticality_points(value: str) -> int:
    """Convert an asset criticality label into simple priority points."""
    criticality = str(value).strip().lower()
    if criticality == "high":
        return 2
    if criticality == "medium":
        return 1
    return 0


def build_priority_score(row: pd.Series) -> int:
    """Calculate a simple priority score for one row of the dataset.

    A pandas Series is like one spreadsheet row. We read values from the row by
    column name, add points for risk signals, and return one total score.
    """
    score = 0

    score += severity_points(row["highest_alert_severity"])
    score += criticality_points(row["asset_criticality"])
    score += yes_no_points(row["internet_exposed"])
    score += yes_no_points(row["sensitive_data"])

    if row["failed_logins_24h"] >= 30:
        score += 1
    if row["successful_logins_after_failures"] > 0:
        score += 1
    if row["mfa_denials"] >= 5:
        score += 1
    if row["malware_alerts"] > 0:
        score += 1

    return score


def main() -> None:
    # read_csv loads the CSV into a DataFrame.
    # A DataFrame is like a spreadsheet table in Python.
    metrics = pd.read_csv(CSV_URL)

    # apply(..., axis=1) runs a function once for each row.
    # The result becomes a new column named priority_score.
    metrics["priority_score"] = metrics.apply(build_priority_score, axis=1)

    # sort_values orders the table by priority_score.
    # ascending=False means highest score first.
    ranked = metrics.sort_values("priority_score", ascending=False)

    # Select only the columns that make the summary easy to read.
    summary_columns = [
        "asset_id",
        "system_name",
        "business_unit",
        "asset_criticality",
        "sensitive_data",
        "internet_exposed",
        "highest_alert_severity",
        "priority_score",
        "notes",
    ]
    summary = ranked[summary_columns]

    print("Top systems by simple priority score")
    print(summary.head(5).to_string(index=False))

    # Export the summary so it can be included in a report if needed.
    output_path = Path("sample_security_metrics_summary.csv")
    summary.to_csv(output_path, index=False)
    print(f"\nWrote summary table to {output_path}")


if __name__ == "__main__":
    main()
