import os
from dotenv import load_dotenv
from fastapi import FastAPI
from sqlalchemy import create_engine, text

load_dotenv()
engine = create_engine(os.environ["DATABASE_URL"])
app = FastAPI(title="Campus Data API")


@app.get("/at-risk")
def at_risk():
    with engine.connect() as conn:
        rows = conn.execute(text("SELECT * FROM at_risk_students")).mappings().all()
    return [dict(r) for r in rows]

@app.get("/students")
def student_data():
    with engine.connect() as conn:
        rows = conn.execute(
            text("SELECT reg_no, name FROM students")
        ).mappings().all()

    return [dict(row) for row in rows]