import streamlit as st
import pandas as pd
import numpy as np


"""
# Document
    @author Cheng
    @date 6/20/2022
    @command streamlit run homePage.py
    This is a Streamlit Home Page demo
"""

str1="""
# 1. H1
## 2. H2
### 3. H3
- Hello World
- ni hao
- say hello

|1|2|3|
|:-:|:-:|:-:|
|eweqweqwewq|fddfdfsdfdf|ffdsffsdfs|

[web link](https://www.baidu.com)

> 鲁迅

"""

st.markdown(str1)
#st.balloons()git 
st.json({'a':'b'})

st.button('Click me')
st.checkbox('I agree')
st.radio('Pick one', ['cats', 'dogs'])
st.selectbox('Pick one', ['cats', 'dogs'])
st.multiselect('Buy', ['milk', 'apples', 'potatoes'])
st.slider('Pick a number', 0, 100)
st.select_slider('Pick a size', ['S', 'M', 'L'])
st.text_input('First name')
st.number_input('Pick a number', 0, 10)
st.text_area('Text to translate')
st.date_input('Your birthday')
st.time_input('Meeting time')
st.file_uploader('Upload a CSV')
st.download_button('Download file',data="something")
st.camera_input("Take a picture")
st.color_picker('Pick a color')



st.slider('Pick a number', 0, 100,key='slider1', disabled=True)

df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)



st.info('Info message')
st.success('Success message')
st.error("Error message")

#st.snow()
