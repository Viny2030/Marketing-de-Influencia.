import streamlit as st
import requests

st.title("📊 Attribution Dashboard")

res = requests.get("http://localhost:8000/report").json()

st.subheader("💰 Revenue por campaña")

for k, v in res.items():
    st.write(f"{k}: ${v}")
