import pandas as pd
from clean import (clean_regno, clean_status, clean_marks, name__clean,
                   clean_dates, clean_subjects, A_DATE_FORMAT, B_DATE_FORMAT)


def test_clean_regno():
    df = pd.DataFrame({"reg_no": ["cs21001", " CS21-031 ", "CS21 002"]})
    result = clean_regno(df)["reg_no"].tolist()
    assert result == ["CS21001", "CS21031", "CS21002"]


def test_clean_status():
    df = pd.DataFrame({"status": ["Yes", "n", "absent", "P", None]})
    result = clean_status(df)["status"].tolist()
    assert result[:4] == ["P", "A", "A", "P"]
    assert pd.isna(result[4])


def test_clean_marks():
    df = pd.DataFrame({"internal_1": ["18", "AB", "55", None],
                       "internal_2": ["20", "0", "7", "12"]})
    result = clean_marks(df)
    assert result["internal_1"].iloc[0] == 18
    assert pd.isna(result["internal_1"].iloc[1])   # AB -> missing
    assert pd.isna(result["internal_1"].iloc[2])   # above 20 -> missing
    assert result["internal_2"].iloc[1] == 0       # a real zero is kept
def test_clean_names():
    df = pd.DataFrame({"name": ["  ANJALI NAIR ", "Nair, Anjali", "rahul menon"]})
    result = name__clean(df)["name"].tolist()
    assert result == ["Anjali Nair", "Anjali Nair", "Rahul Menon"]


def test_clean_dates():
    a = pd.DataFrame({"date": ["03/08/2026", "31/02/2026"]})
    b = pd.DataFrame({"date": ["3-Aug-26"]})
    ra = clean_dates(a, A_DATE_FORMAT)["date"]
    rb = clean_dates(b, B_DATE_FORMAT)["date"]
    assert ra.iloc[0] == pd.Timestamp("2026-08-03")
    assert pd.isna(ra.iloc[1])                   # impossible date becomes missing
    assert rb.iloc[0] == pd.Timestamp("2026-08-03")


def test_clean_subjects():
    df = pd.DataFrame({"subject": ["dbms", "Database Mgmt", "Operating Systems", "DSA"]})
    result = clean_subjects(df)["subject"].tolist()
    assert result == ["DBMS", "DBMS", "OS", "DSA"]