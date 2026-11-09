import os 
import pandas as pd
from  dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()
engine=create_engine(os.environ["DATABASE_URL"])

attendence=pd.read_csv("data/clean/attendance.csv",parse_dates=["date"])
marks=pd.read_csv("data/clean/marks.csv")

students=(attendence[["reg_no","name"]].drop_duplicates("reg_no").sort_values("reg_no"))

students.to_sql("students",engine,if_exists="replace",index=False)
attendence.drop(columns="name").to_sql("attendence",engine,if_exists="replace",index=False)
marks.to_sql("marks",engine,if_exists="replace",index=False)

print("loaded:",len(students),"students",
      len(attendence),"Attendence",
      len(marks),"marks")
