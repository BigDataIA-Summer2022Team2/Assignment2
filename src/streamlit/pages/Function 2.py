import streamlit as st
import requests
import time

st.sidebar.markdown("# Function 2")
st.markdown("# Function 2")
st.markdown("## Try it :smile:")

col1,col2 = st.columns(2)

with col1:
    className = st.text_input('Class')
    
with col2:
    filename = st.text_input('File name')
# 'http://127.0.0.1:8000/api/get/fileNameAndClass/?className=V22&filename=1a6c746f6f852a70f0b8b719aa281932'

def getFastAPIResponse(): #data_bin
    #rlt = requests.post('http://127.0.0.1:8000/api/get/fileNameAndClass/', json=data_bin).json()
    response = requests.get(url).json()
    return response


if(className != ""):
    st.success("You did it! :heart:")
    st.markdown("## Output Response")
    url = 'http://127.0.0.1:8000/api/get/fileNameAndClass/' + '?className=' + className + '&filename=' + filename

    st.json(getFastAPIResponse())
else:
    st.warning('Class value is required.')




isClick = st.button("Show hint")
if(isClick == True):
    st.markdown("> getFileNameClassNameFilteredResult(className:str,fileName:str)")
    st.markdown("## Sample Input")
    input_str = """
    |class|filename|
    |:-:|:-:|
    |V22|1a6c746f6f852a70f0b8b719aa281932|
    """

    st.markdown(input_str)
    st.markdown("## Sample Output")
    json_response = """
    {
    "104": {
        "filename": "1a6c746f6f852a70f0b8b719aa281932",
        "width": "1920",
        "height": "1080",
        "class": "V22",
        "xmin": "44",
        "ymin": "325",
        "xmax": "1447",
        "ymax": "1075"
    },
    "105": {
        "filename": "1a6c746f6f852a70f0b8b719aa281932",
        "width": "1920",
        "height": "1080",
        "class": "V22",
        "xmin": "981",
        "ymin": "149",
        "xmax": "1814",
        "ymax": "478"
    },
    "106": {
        "filename": "1a6c746f6f852a70f0b8b719aa281932",
        "width": "1920",
        "height": "1080",
        "class": "V22",
        "xmin": "1408",
        "ymin": "79",
        "xmax": "1920",
        "ymax": "253"
    }
    }
    """
    st.json(json_response)
