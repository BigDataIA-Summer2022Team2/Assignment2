import streamlit as st
import os
import streamlit.components.v1 as co

abs_path = os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__)))))
#print(abs_path)

path1 = abs_path+"/report.html"
fp = open(path1, 'r')

#st.markdown(data_v,unsafe_allow_html=True)



data = fp.read() 
#print(fp)
co.html(data, height = 13200)