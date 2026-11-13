import pandas as pd
import requests
import streamlit as st 

api="http://127.0.0.1:8000"
st.set_page_config(page_title="Campus Data" , layout="wide")
st.title("Campus Attendence and Marks")

try:
    at_risk = pd.DataFrame(requests.get(f"{api}/at-risk", timeout=10).json())
    students = requests.get(f"{api}/students", timeout=10).json()
except requests.ConnectionError:
    st.error("Cannot reach the API. Start it with: python -m uvicorn api:app --reload")
    st.stop()
col1,col2=st.columns(2)
col1.metric("Students",len(students))
col2.metric("At risk",len(at_risk))

st.subheader("students at risk")
st.dataframe(at_risk)