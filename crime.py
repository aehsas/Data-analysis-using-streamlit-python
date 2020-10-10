import streamlit as st
import numpy as np 
import pandas as pd 
import plotly.express as px
st.title("Sanfrancisco Crime analysis ")
st.markdown('Crime in Sanfrancisco')
st.sidebar.title('Sanfrancisco Crime analysis')
st.sidebar.subheader('Crime in Sanfrancisco')
@st.cache(persist=True)
def load_data():
    data = pd.read_csv('/home/aehsas/Documents/train.csv')
    data['Dates']=pd.to_datetime(data['Dates'])
    return data

data = load_data()
data.columns = ['Dates','Category','Descript','DayOfWeek','PdDistrict','Resolution','Address','longitude','latitude']

st.sidebar.markdown('Type of crimes and their stats')
select = st.sidebar.selectbox('visualization type',['Histogram','Pie chart'],key=1)
crime_count = data['Category'].value_counts()
crime_count = pd.DataFrame({'Crime':crime_count.index, 'Numbers': crime_count.values})
if not st.sidebar.checkbox("Hide",True):
    st.markdown("Rate of crime as per type")
    if select == "Histogram":
        fig = px.bar(crime_count,x="Crime",y="Numbers",color="Numbers",height =600,width=900)
        st.plotly_chart(fig)
    else:
        fig = px.pie(crime_count,values="Numbers",names="Crime")
        st.plotly_chart(fig)

st.sidebar.subheader("crime based on the time of day")
hour = st.sidebar.slider("Hours of day",0,23)
year = st.sidebar.slider("Year",2003,2015)
day = st.sidebar.slider("Month",1,12)
mod_dat = data[data['Dates'].dt.hour == hour]
mod_dat = mod_dat[data['Dates'].dt.year == year]
mod_dat = mod_dat[data['Dates'].dt.month == day]
if not st.sidebar.checkbox("close",True,key='1'):
    st.markdown("Crime location based on time")
    st.markdown("%i crime between %i:00 and %i:00 in the Month of %i" % (len(mod_dat),hour,hour+1%24,day))
    st.map(mod_dat)
