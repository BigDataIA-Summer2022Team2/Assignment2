import streamlit as st

st.sidebar.markdown("# Function1")
st.markdown("# Function 1")
st.markdown("## Try it :smile:")

col1,col2 = st.columns(2)

def w_text_input_to_slider():
    if(st.session_state.w_text_input == ""):
        st.session_state.w_slider = 0
    else:
        st.session_state.w_slider = int(st.session_state.w_text_input) # "400" -> 400
def w_slider_to_text_input():
    st.session_state.w_text_input = str(st.session_state.w_slider)


def h_text_input_to_slider():
    if(st.session_state.h_text_input == ""):
        st.session_state.h_slider = 0
    else:
        st.session_state.h_slider = int(st.session_state.h_text_input) # "400" -> 400
def h_slider_to_text_input():
    st.session_state.h_text_input = str(st.session_state.h_slider)

with col1:
    width = st.text_input("Width",key="w_text_input",on_change=w_text_input_to_slider)
    width_slider = st.slider('Pick a width number', 0, 9999,key="w_slider",on_change=w_slider_to_text_input)
  
with col2:
    height = st.text_input("Height",key="h_text_input",on_change=h_text_input_to_slider)
    height_slider = st.slider('Pick a height number', 0, 9999,key="h_slider",on_change=h_slider_to_text_input)


def getFastAPIResponse(): #data_bin
    #response = requests.post('http://127.0.0.1:8000/api/get/imgSizeRange/?width=600&height=600', json=data_bin).json()
    response = requests.get(url).json()
    return response

if(width_slider != 0 and height_slider != 0):
    st.success("You did it! :heart:")
    st.markdown("## Output Response")
 
    url = 'http://204.15.72.120:8000/api/get/imgSizeRange/' + '?width=' + str(width_slider) + '&height=' + str(height_slider)
    st.json(getFastAPIResponse())
if(width_slider == 0):
    st.warning('Width value is required.')
if(height_slider == 0):
    st.warning('Height value is required.')


isClick = st.button("Show Hint")    

if(isClick == True):
    
    st.markdown("## Sample Input")
    st.markdown("> getimgSizeRangeFilteredResult(width:int,height:int)")
    input_str = """
    |width|height|
    |:-:|:-:|
    |700|700|
    """

    st.markdown(input_str)
    st.markdown("## Sample Output")
    json_response = """
    {
    "69": {
        "filename": "0dc3f3e32533d1909ec496e32a3f916c",
        "width": "512",
        "height": "303",
        "class": "SR71",
        "xmin": "178",
        "ymin": "121",
        "xmax": "331",
        "ymax": "209"
    },
    "186": {
        "filename": "2cf1ec46ef1a6534a784b25ce1d07978",
        "width": "512",
        "height": "341",
        "class": "Su57",
        "xmin": "28",
        "ymin": "162",
        "xmax": "236",
        "ymax": "282"
    },
    "187": {
        "filename": "2cf1ec46ef1a6534a784b25ce1d07978",
        "width": "512",
        "height": "341",
        "class": "Su57",
        "xmin": "115",
        "ymin": "43",
        "xmax": "483",
        "ymax": "172"
    },
    "201": {
        "filename": "2ebe35e67880d4f9609c9fa07b6f5f9e",
        "width": "590",
        "height": "369",
        "class": "C17",
        "xmin": "15",
        "ymin": "116",
        "xmax": "492",
        "ymax": "358"
    },
    "202": {
        "filename": "2ebe35e67880d4f9609c9fa07b6f5f9e",
        "width": "590",
        "height": "369",
        "class": "F15",
        "xmin": "329",
        "ymin": "50",
        "xmax": "486",
        "ymax": "101"
    },
    "203": {
        "filename": "2ebe35e67880d4f9609c9fa07b6f5f9e",
        "width": "590",
        "height": "369",
        "class": "F15",
        "xmin": "446",
        "ymin": "11",
        "xmax": "589",
        "ymax": "56"
    }
    }
    """
    st.json(json_response)



