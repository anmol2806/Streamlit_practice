

import streamlit as st
import pandas as pd

st.write(""" Hello *world!*
""")

df=pd.read_csv("adult.csv")
st.line_chart(df)
