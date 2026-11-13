import os
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()
engine = create_engine(os.environ["DATABASE_URL"])

# The view depends on the tables, so drop it before rebuilding them
with engine.begin() as conn:
    conn.execute(text("DROP VIEW IF EXISTS at_risk_students"))

attendance = pd.read_csv("data/clean/attendance.csv", parse_dates=["date"])
marks = pd.read_csv("data/clean/marks.csv")

students = (attendance[["reg_no", "name"]]
            .drop_duplicates("reg_no")
            .sort_values("reg_no"))

students.to_sql("students", engine, if_exists="replace", index=False)
attendance.drop(columns="name").to_sql("attendance", engine, if_exists="replace", index=False)
marks.to_sql("marks", engine, if_exists="replace", index=False)

# Recreate the view from the saved SQL file
view_sql = Path("sql/at_risk_view.sql").read_text()
with engine.begin() as conn:
    conn.execute(text(view_sql))

print("Loaded:", len(students), "students,",
      len(attendance), "attendance rows,",
      len(marks), "marks rows")