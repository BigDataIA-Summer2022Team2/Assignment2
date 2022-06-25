import streamlit as st

st.set_page_config(page_title="API Function 1",page_icon=":heart:")

st.sidebar.markdown("# Function1")
st.markdown("# Function 1")
st.markdown("## Try it :smile:")


col1,col2 = st.columns(2)

with col1:
    filename = st.text_input('File name')
    width = st.text_input("Width",key="w_text_input")#on_change=w_text_input_to_slider
    width_slider = st.slider('Pick a width number', 0, 9999,key="w_slider")#on_change=h_text_input_to_slider
    xmin = st.text_input("xmin",key="xmin_text_input")#on_change=xmin_text_input_to_slider
    xmin_slider = st.slider('Pick a xmin number', 0, 9999,key="xmin_slider")#on_change=xmin_slider_to_text_input
    ymin = st.text_input("ymin",key="ymin_text_input")#on_change=ymin_text_input_to_slider
    ymin_slider = st.slider('Pick a ymin number', 0, 9999,key="ymin_slider")#on_change=ymin_slider_to_text_input
 
    
with col2:
    className = st.text_input('Class')
    height = st.text_input("Height",key="h_text_input")#on_change=h_text_input_to_slider
    height_slider = st.slider('Pick a height number', 0, 9999,key="h_slider")#on_change=h_text_input_to_slider
    xmax = st.text_input("xmax",key="xmax_text_input")#on_change=h_text_input_to_slider
    xmax_slider = st.slider('Pick a xmax number', 0, 9999,key="xmax_slider")#on_change=h_slider_to_text_input
    ymax = st.text_input("ymax",key="xmax_text_input")#on_change=h_text_input_to_slider
    ymax_slider = st.slider('Pick a ymax number', 0, 9999,key="ymax_slider")#on_change=h_slider_to_text_input

    




