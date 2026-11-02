import pandas as pd

a=pd.read_csv("data/RAW/attendance_teacher_a.csv")
b=pd.read_csv("data/RAW/attendance_teacher_b.csv")
c=pd.read_csv("data/RAW/internal_marks.csv")

for name , df in [("A",a), ("B",b) , ("C", c)]:

    print(f"\n===== {name} =====")
    print(df.shape)
    print(df.info())
    print("Duplicate rows:", df.duplicated().sum())
print("\nA status values:\n", a["Status"].value_counts(dropna=False))
print("\nB present values:\n", b["Present"].value_counts(dropna=False))
print("\nMarks subjects:\n", c["Subject"].value_counts(dropna=False))
print("\nInternal 1 values:\n", c["Internal 1"].value_counts(dropna=False).head(15))
for name, df in [("A", a), ("B", b), ("C", c)]:
    print(f"\n{name} blanks per column:")
    print(df.isna().sum())
    print(name,"Duplicated ones ", df.duplicated().sum())