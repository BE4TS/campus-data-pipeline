import pandas as pd
from clean import clean_regno, clean_status, clean_marks


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