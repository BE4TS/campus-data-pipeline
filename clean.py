import pandas as pd


A_COLUMNS={"Reg No":"reg_no","Student Name":"name","Date":"date","Status":"status"}
B_COLUMNS={"RegNo":"reg_no","Name":"name","Day":"date","Present":"status"}
MARKS_COLUMNS = {"Roll Number": "reg_no", "Subject": "subject",
                 "Internal 1": "internal_1", "Internal 2": "internal_2"}

def load_raw():
    a=pd.read_csv("data/RAW/attendance_teacher_a.csv").rename(columns=A_COLUMNS)
    b=pd.read_csv("data/RAW/attendance_teacher_b.csv").rename(columns=B_COLUMNS)
    c=pd.read_csv("data/RAW/internal_marks.csv").rename(columns=MARKS_COLUMNS)
    return a,b,c
if __name__=="__main__":
    a,b,c=load_raw()
    print(a.columns.tolist())
    print(b.columns.tolist())
    print(c.columns.tolist())

