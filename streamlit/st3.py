import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt


'''We can display the text in different ways. Streamlit allows you to write the title, header, and also supports various functions.

st.title()- to set the title
st.text() to write the description for the particular graph
st.markdown() to display text as markdown
st.latex() to display the mathematical expressions in the dashboard.
st.write() helps to display everything such as plotly graph, dataframe, functions, model, etc.
st.sidebar() is used for displaying data on the sidebar.
st.dataframe() to display the data frame
st.map() to display the map in just a single line code etc'''


st.title("Covid_19 Dashboard For India")
st.markdown("The dashboard will visualize the Covid_19 Situation in India")
st.markdown("Coronavirus disease (COVID_19) is an infectious disease caused by a newly discovered coronavirus. Most people infected with the COVID-19 virus will experience mild to moderate respiratory illness and recover without requiring special treatment.’. This app gives you the real-time impact analysis of Confirmed, Deaths, active, and recovered cases of COVID-19 ")
st.sidebar.title("Visualization Selector")
st.sidebar.markdown("Select the Charts/Plots accordingly:")
 




def load_data():
    data=pd.read_csv("covid_data.csv")
    return data

covid19_data=load_data()


st.sidebar.checkbox("Show Analysis by State", True, key=1)
select = st.sidebar.selectbox('Select a State',covid19_data['continent'])

#get the state selected in the selectbox
state_data = covid19_data[covid19_data['continent'] == select]
select_status = st.sidebar.radio("Covid-19 patient's status", ('Confirmed',
'Active', 'Recovered', 'Deceased'))



def get_total_dataframe(dataset):
    total_dataframe = pd.DataFrame({
    'Status':['Confirmed', 'Recovered', 'Deaths','Active'],
    'Number of cases':(dataset.iloc[0]['confirmed'],
    dataset.iloc[0]['recovered'], 
    dataset.iloc[0]['deaths'],dataset.iloc[0]['active'])})
    return total_dataframe

state_total = get_total_dataframe(state_data)

if st.sidebar.checkbox("Show Analysis by State", True, key=2):
    st.markdown("## **State level analysis**")
    st.markdown("### Overall Confirmed, Active, Recovered and " +
    "Deceased cases in %s yet" % (select))
    if not st.checkbox('Hide Graph', False, key=1):
        state_total_graph = px.bar(
        state_total, 
        x='Status',
        y='Number of cases',
        labels={'Number of cases':'Number of cases in %s' % (select)},
        color='Status')
        st.plotly_chart(state_total_graph)