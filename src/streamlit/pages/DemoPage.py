import streamlit as st
import pandas as pd
import numpy as np
import time

"""
# Document
    @author Cheng
    @date 6/20/2022
    @command streamlit run homePage.py
    This is a Streamlit Home Page demo
"""



st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")




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

st.text("Seomthing is not right now~")
isClick =  st.button('Click me') #request {"button" : ["key" : "value"]}
st.write(isClick)

st.checkbox('I agree')
df1 = ['cats', 'dogs']
result = st.radio('Pick one', df1)
st.write(result)
sel_result = st.selectbox('Pick one', df1)
st.write(sel_result)
st.multiselect('Buy', ['milk', 'apples', 'potatoes'])
st.slider('Pick a number', 0, 100)
st.select_slider('Pick a size', ['S', 'M', 'L'])
strName = st.text_input('First name')
st.write(strName)

iNum = st.number_input('Pick a number', 0, 10)
st.write("Input number: ", iNum)

st.text_area('Text to translate')


st.date_input('Your birthday')
st.time_input('Meeting time')
st.file_uploader('Upload a CSV')
st.download_button('Download file',data="something")
st.camera_input("Take a picture")
custom_color = st.color_picker('Pick a color')
st.write("The color you choose is(Hex):",custom_color)

st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

expander = st.expander("See explanation")
expander.write("""
    The chart above shows some numbers I picked for you.
    I rolled actual dice for these, so they're *guaranteed* to
    be random.
""")
expander.image("https://static.streamlit.io/examples/dice.jpg")

st.slider('Pick a number', 0, 100,key='slider1', disabled=True)

df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)

#st.table(df)
#st.metric(label="Temperature", value="70 °F", delta="1.2 °F",delta_color="inverse")

st.info('Info message')
st.success('Success message')
st.error("Error message")
st.warning('Warning message')
e = RuntimeError('This is an exception of type RuntimeError')
st.exception(e)
#st.snow()


with st.container():
    st.write("This is inside the container")

    # You can call any Streamlit command, including custom components:
    st.bar_chart(np.random.randn(50, 3))

st.write("This is outside the container")



# with st.empty():
#      for seconds in range(60):
#          st.write(f"⏳ {seconds} seconds have passed")
#          time.sleep(1)
#      st.write("✔️ 1 minute over!")
     



placeholder = st.empty()

# Replace the placeholder with some text:
placeholder.text("Hello")

# Replace the text with a chart:
placeholder.line_chart({"data": [1, 5, 2, 6]})

# Replace the chart with several elements:
with placeholder.container():
     st.write("This is one element")
     st.write("This is another")

# Clear all those elements:
placeholder.empty()



# my_bar = st.progress(0)

# for percent_complete in range(100):
#      time.sleep(0.1)
#      my_bar.progress(percent_complete + 1)
     
     
with st.spinner('Wait for it...'):
    id1 = st.success('Done!')
    time.sleep(5)
    id1 = st.error("Error!")
