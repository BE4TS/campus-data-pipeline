# campus-data-pipeline
# Campus Data Pipeline

A pipeline that takes messy attendance and marks spreadsheets from a college
department, cleans them, stores them in one database, and flags students who
may need support.

## The problem
Each teacher keeps their own Excel/CSV file. Column names, date formats and
student IDs differ between files, and there are typos, duplicates, missing
marks and entries like "AB" inside numeric columns. The department office
cannot answer simple questions because the data cannot be combined.

## The question
Which students are at risk (low attendance plus falling marks), and what is
the attendance trend for each class?

## Planned approach
1. Generate realistic messy sample data (no real student records are used)
2. Clean and standardize it with pandas
3. Load it into PostgreSQL
4. Expose it through a FastAPI service
5. Show results in a dashboard

## Status
Work in progress. Started November 2026.