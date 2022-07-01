import streamlit as st
import requests

def getFastAPIResponse(url): #data_bin
    #rlt = requests.post('http://127.0.0.1:8000/api/get/fileNameAndClass/', json=data_bin).json()
    response = requests.get(url)
    return response



link = '<a href="https://lemonsoldout.top/pandas/html/csv/" target="_self">Show Pandas Profiling CSV data analysis</a>'
st.markdown(link, unsafe_allow_html=True)

