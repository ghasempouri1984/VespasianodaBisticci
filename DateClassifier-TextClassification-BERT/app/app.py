import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
# importing geopy library
from geopy.geocoders import Nominatim

st.title("Welcome to Vespasiano's Letters App")
st.sidebar.title("explore letters archive")

st.markdown('### a prototype dashboard for letters archive')
st.sidebar.markdown("book seller of Florence")

data_url = 'C:\\Github\\VespasianodaBisticci\\VespasianodaBisticci\\DateClassifier-TextClassification-BERT\\extended-data.csv'

@st.cache(persist=True)
def load_data():
    data = pd.read_csv(data_url)
    #data['years']=pd.to_datetime(data['years'])
    return data
    
data =load_data()

st.sidebar.subheader("show random letter's text")
random_text=st.sidebar.radio('year:',('1446','1450','1463'))
st.sidebar.markdown(data.query('years==@random_text')[["testo"]].sample(n=1).iat[0,0])

#data.query('years==@random_text')[["letter_number"]]
#random_text_2=st.sidebar.radio('letter:',('1446','1450','1457'))
st.sidebar.markdown("### The Letter Number is:")
st.sidebar.markdown(data.query('years==@random_text')[["letter_number"]].iat[0,0])

st.sidebar.markdown("### viz")
select=st.sidebar.selectbox('Viz Type', ['Histogram', 'Pie Chart'], key='1')
years_count=data['years'].value_counts()
years_count=pd.DataFrame({'years': years_count.index, 'testo': years_count.values})

if not st.sidebar.checkbox("Hide", True):
    st.markdown("### number of texts by years")
    if select == "Histogram":
        fig = px.bar(years_count, x='years', y='testo', color='testo', height=500)
        st.plotly_chart(fig)
    else:
        fig=px.pie(years_count, values='testo', names='years')
        st.plotly_chart(fig)



#uri_from=data['uri_from'].to_list()
# calling the Nominatim tool
#loc = Nominatim(user_agent="GetLoc")
#lat=[]
#long=[]
# entering the location name
#for elem in uri_from:
#    getLoc = loc.geocode(elem)
#    lat.append(getLoc.latitude)
#    long.append(getLoc.longitude)