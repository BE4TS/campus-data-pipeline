# campus-data-pipeline
# Campus Data Pipeline

A pipeline that takes messy attendance and marks spreadsheets from a college
department, cleans them, stores them in one database, and flags students who
may need support.

## Problems found

### Teacher A (attendance_teacher_a.csv)
- Status has blank values: N rows
- Duplicate rows: N
- Names have mixed case / extra spaces (example: "  Gokul Pillai  ")
- ...

### Teacher B (attendance_teacher_b.csv)
- Present has inconsistent wording: Yes, yes, Y, present, No, absent, no, N
- ...

### Marks (internal_marks.csv)
- ...
### Decisions
AB means absent. It isn’t a mark, so it becomes missing (NaN) and the column can be numeric.
Marks above 20 are impossible. The maximum is 20, so these are data-entry errors. We can’t know the right value, so they become missing too. We don’t cap them at 20, because that would invent a mark.
Blanks stay missing.
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

   python generate_data.py              # make messy sample data
   python clean.py                      # clean into data/clean/
   python load.py                       # load into Postgres
   python -m uvicorn api:app --reload   # start the API, open /docs
   python -m pytest                     # run tests

## How to run
1. Install: `pip install -r requirements.txt`
2. Start Postgres and create a database called `campus`
3. Create `.env` with: `DATABASE_URL=postgresql://postgres:<password>@localhost:5432/campus`
4. `python generate_data.py`   # messy sample data
5. `python clean.py`           # clean into data/clean/
6. `python load.py`            # load into Postgres
7. `python -m uvicorn api:app --reload`   # API at http://127.0.0.1:8000/docs
8. `python -m pytest`          # run the tests