import pandas as pd


A_COLUMNS={"Reg No":"reg_no","Student Name":"name","Date":"date","Status":"status"}
B_COLUMNS={"RegNo":"reg_no","Name":"name","Day":"date","Present":"status"}
MARKS_COLUMNS = {"Roll Number": "reg_no", "Subject": "subject",
                 "Internal 1": "internal_1", "Internal 2": "internal_2"}

A_DATE_FORMAT="%d/%m/%Y"
B_DATE_FORMAT="%d-%b-%y"


STATUS_MAP={"p":"P","yes":"P","y":"P","present":"P",
            "a":"A","no":"A","n":"A","absent":"A"}

def load_raw():
    a=pd.read_csv("data/RAW/attendance_teacher_a.csv").rename(columns=A_COLUMNS)
    b=pd.read_csv("data/RAW/attendance_teacher_b.csv").rename(columns=B_COLUMNS)
    c=pd.read_csv("data/RAW/internal_marks.csv").rename(columns=MARKS_COLUMNS)
    return a,b,c
def clean_regno(df):
    df=df.copy()
    df["reg_no"]=(df["reg_no"].str.strip()
                  .str.upper()
                  .str.replace(r"[\s\-]","",regex=True))
    return df
#cleaning names
def name__clean(df):
    df=df.copy()
    names=df["name"].str.strip()
    names=names.str.replace(r"^(.+?),\s*(.+)$",r"\2 \1",regex=True)
    df["name"]=names.str.title()
    return df
def fix_name_typos(df):
    df=df.copy()
    best=df.groupby("reg_no")["name"].agg(lambda s: s.mode() .iloc[0])
    df["name"]=df["reg_no"].map(best)
    return df 
def clean_dates(df,fmt):
    df=df.copy()
    df["date"]=pd.to_datetime(
        df["date"].str.strip(),format=fmt,errors="coerce"
    )
    return df

def clean_status(df):
    df=df.copy()
    df["status"]=df["status"].str.strip().str.lower().map(STATUS_MAP)

    return df 



if __name__=="__main__":
    a,b,c=load_raw()
    a=clean_status(clean_dates(fix_name_typos(name__clean(clean_regno(a))),A_DATE_FORMAT))
    b=clean_status(clean_dates(fix_name_typos(name__clean(clean_regno(b))),B_DATE_FORMAT))
    print("A bad dates:", a["date"].isna().sum())
    print("B bad dates:", b["date"].isna().sum())
    print("A status:\n", a["status"].value_counts(dropna=False))
    print("B status:\n", b["status"].value_counts(dropna=False))
    print(a.head())
    print(b.head())
    for col in  ["internal_1", "internal_2"]:
        nums=pd.to_numeric(c[col],errors="coerce")
        print(f"\n{col} text values:")
        print(c.loc[nums.isna() & c[col].notna(),col].value_counts())
        print(f"{col} above 20:",(nums>20).sum())
    # a2=clean_dates(a,A_DATE_FORMAT)
    # b2=clean_dates(b,B_DATE_FORMAT)
    # print("A range:",a2["date"].min(),"to",a2["date"].max())
    # print("B range:",b2["date"].min(),"to",b2["date"].max())
    # for name,df in [("A",a),("B",b)]:
    #     print(name, clean_status(df)["status"].value_counts(dropna=False))
    #     step1=clean_regno(df)
    #     step2=name__clean(step1)
    #     step3=fix_name_typos(step2)
    #     print(name, "unique names ->",
    #           "raw:", df["name"].nunique(),
    #           "after clean_names:", step2["name"].nunique(),
    #           "after typo fix:", step3["name"].nunique())
    #     # before=df["reg_no"].nunique()
        # after=clean_regno(df)["reg_no"].nunique()
        # print(name,"unique id before: ", before,"after: ", after)
    # print(a.columns.tolist())
    # print(b.columns.tolist())
    # print(c.columns.tolist())

