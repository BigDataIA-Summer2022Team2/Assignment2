import streamlit as st
import streamlit_authenticator as stauth
import yaml
import requests
import json
import io
#from baseDatas import userAgents
#st.session_state
st.set_page_config(page_title="API Functions",page_icon=":heart:")

def check_xmin():
    if(st.session_state.xmin > st.session_state.xmax):
        st.warning("xmin value should be less than xmax value")
        st.session_state.xmin = 0
    
def check_xmax():
    if(st.session_state.xmax < st.session_state.xmin):
        st.warning("xmax value should be greater than xmin value")
        st.session_state.xmax = st.session_state.xmin + 100

def check_ymin():
    if(st.session_state.ymin > st.session_state.ymax):
        st.warning("ymin value should be less than ymax value")
        st.session_state.ymin = 0
def check_ymax():
    if(st.session_state.ymax < st.session_state.ymin):
        st.warning("ymax value should be greater than ymin value")
        st.session_state.ymax = st.session_state.ymin + 100


##################################################################
def getFastAPIResponse(url,data): #data_bin
    #rlt = requests.post('http://127.0.0.1:8000/api/get/fileNameAndClass/', json=data_bin).json()
    
    token_str = 'bearer ' + st.session_state["token"]
    headers = {'accept': 'application/json','authorization': str(token_str)}
    response = requests.get(url=url,params=data,headers=headers,verify=False).json()

    return response
##################################################################
def function1():
    st.markdown("# Function 1 🎈")
    st.sidebar.markdown("# Function 1 🎈")
    randNum = st.sidebar.number_input("Pick a number of random images",1,9,step=1)
    isClick = st.sidebar.button("OK")
    if isClick:
        #st.write(randNum)
        
        url = 'http://127.0.0.1:8000/api/get/random/'
        data = {'num' : randNum}
        response = getFastAPIResponse(url,data)

        #response = requests.get(url,headers=header).json()
        with st.expander("Here are filename list",expanded=True):
            st.json(response)
        
        
        with st.expander("Here are full images file info",expanded=False):
            for i in range(randNum):
                filename = str(response.get(str(i+1)))
                print(filename)
                data1 = {"filename":filename}
                url1 = 'http://127.0.0.1:8000/api/get/fileNameAndClass'
                response1 = getFastAPIResponse(url1,data1)
                st.json(response1)
        #Todo display images
        
        
        #response = requests.get(url,headers=header).json()
        # with st.expander("See Full Image files Info Response"):
        #     st.json(response1)    
    
    
def function2():
    st.markdown("# Function 2 ❄️")
    st.sidebar.markdown("# Function 2 ❄️")
    filename = st.sidebar.text_input(label="Please enter image filename(not required)",max_chars=32)
    className = st.sidebar.text_input(label="Please enter aircraft class")
    
    isClick = st.sidebar.button("OK")
    isShowHint = st.sidebar.button("Show Hint")
    if isClick:
        #st.write(filename,className)
        #Todo
        if(className != ""):
            st.success("You did it! :heart:")
            st.markdown("## Output Response")
            
            
            url = 'http://127.0.0.1:8000/api/get/fileNameAndClass'
            data = {'className':className,"filename":filename}
            response = getFastAPIResponse(url,data)

            
            
            #response = requests.get(url,headers=header).json()
            with st.expander("See API Response"):
                st.json(response)
        else:
            st.warning('Class value is required.')
    if isShowHint:
            #st.write(isShowHint)
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

 

def function3():
    st.markdown("# Function 3 🎉")
    st.sidebar.markdown("# Function 3 🎉")
    width = st.sidebar.number_input("Pick a width value",0,5000,step=100)
    height = st.sidebar.number_input("Pick a height value",0,5000,step=100)
    isclick = st.sidebar.button("OK")
    isShowHint = st.sidebar.button("Show Hint")
    if(isclick == True):
        #st.write(width, height)
        if(width == 0):
            st.warning('Width value is required.')
        if(height== 0):
            st.warning('Height value is required.')
        if(width != 0 and height != 0):
            url = 'https://lemonsoldout.top/api/get/imgSizeRange/' 
            data = {"width": str(width), "height": str(height)}#+ '?width=' + str(width) + '&height=' + str(height)
            with st.expander("See API Response"):
                st.json(getFastAPIResponse(url,data))
        
    if(isShowHint == True):
        st.markdown("## Sample Input")
        st.markdown("> getimgSizeRangeFilteredResult(width:int,height:int)")
        input_str = """
        |width|height|
        |:-:|:-:|
        |600|400|
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
        
       

def function4():
    st.markdown("# Function 4 🎉")
    st.sidebar.markdown("# Function 4 🎉")
    xmax = st.sidebar.number_input("Pick aircraft position xmax value in the image",0,5000,step=100,key='xmax',on_change=check_xmax)
    ymax = st.sidebar.number_input("Pick aircraft position ymax value in the image",0,5000,step=100,key='ymax',on_change=check_ymax)
    xmin = st.sidebar.number_input("Pick aircraft position xmin value in the image",0,5000,step=100,key='xmin',on_change=check_xmin)
    ymin = st.sidebar.number_input("Pick aircraft position ymin value in the image",0,5000,step=100,key='ymin',on_change=check_ymin)
    isclick = st.sidebar.button("OK")
    isShowHint = st.sidebar.button("Show Hint")
    if(isclick == True):
        
        if(st.session_state.xmin > st.session_state.xmax):
            st.warning("xmin value should be less than xmax value")
        if(st.session_state.xmax < st.session_state.xmin):
            st.warning("xmax value should be greater than xmin value")
        #https://lemonsoldout.top/api/get/aircraftPositionRange/?xmin=400&ymin=200&xmax=600&ymax=500
        url = 'https://lemonsoldout.top/api/get/aircraftPositionRange/' 
        data = {"xmin":str(xmin),"ymin":str(ymin),"xmax":str(xmax),"ymax":str}#+ '?xmin=' + str(xmin) + '&ymin=' + str(ymin) + '&xmax=' + str(xmax) + '&ymax='+ str(ymax)
        with st.expander("See API Response"):
            st.json(getFastAPIResponse(url,data))

    
    
    if(isShowHint == True):
        st.markdown("## Sample Input")
        st.markdown("> ")
        input_str = """
            |xmax|ymax|xmin|ymin|
            |:-:|:-:|:-:|:-:|
            |600|500|400|200|
            """
        
        st.markdown(input_str)
        st.markdown("## Sample Output")
        json_response = """
                {
                    "56": {
                        "filename": "0d4967170de7d1780f7d152da11cd732",
                        "width": "1595",
                        "height": "659",
                        "class": "EF2000",
                        "xmin": "402",
                        "ymin": "323",
                        "xmax": "578",
                        "ymax": "432"
                    },
                    "148": {
                        "filename": "1e802e79331a4a1f124e8d796f3a465d",
                        "width": "1600",
                        "height": "900",
                        "class": "F4",
                        "xmin": "457",
                        "ymin": "333",
                        "xmax": "592",
                        "ymax": "370"
                    },
                    "377": {
                        "filename": "6d1da5fe58e81490106722c7dc9a52bf",
                        "width": "960",
                        "height": "640",
                        "class": "EF2000",
                        "xmin": "421",
                        "ymin": "367",
                        "xmax": "568",
                        "ymax": "426"
                    }
                }
            
            """
        st.json(json_response)
        

def function5():
    st.markdown("# Function 5")
    st.sidebar.markdown("# Function 5")
    air_num = st.sidebar.number_input("Show all images with same input number of aircrafts",1,15,step=1)
    className = st.sidebar.text_input("Please enter aircraft class")
    isClick = st.sidebar.button("OK")
    if(isClick == True):
        url = 'http://127.0.0.1:8000/api/get/aircraftNumandClass/'
        data = {"num":air_num, "className": className}
        response = getFastAPIResponse(url,data)
        # for key, value in response.items():
        #     # url1 = 'http://127.0.0.1:8000/api/get/display/image/'
        #     # data1 = {"filename":value["filename"]}
        #     response1 = getFastAPIResponse(url,data)
            
            #st.write(key,value)
            # st.json(response1)
            #Todo display image
            
            
        with st.expander("See API Function Response"):
            st.json(response)
    
        

def function6():
    st.markdown("# Function 6")
    st.sidebar.markdown("# Function 6")
    img = st.sidebar.text_input("Input image file name")
    isClick = st.sidebar.button("OK")
    if(isClick == True):
        url = 'http://127.0.0.1:8000/display/image/'
        data = {"filename":img}
        response = getFastAPIResponse(url,data)
        # b = io.BytesIO()
        # response.save(b, 'jpeg')
        # response = b.getvalue()
        st.json(response)

def function7():
    st.markdown("# Function 7")
    st.sidebar.markdown("# Function 7")
    img = st.sidebar.text_input("Input image file name")
    isClick = st.sidebar.button("OK")
    if(isClick == True):
        url = 'http://127.0.0.1:8000/api/get/getboundingbox/'
        data = {"filename":img}
        response = getFastAPIResponse(url,data)
        st.write(response)


with open('./streamlit_config.yaml') as file:
        config = yaml.safe_load(file)
        
authenticator = stauth.Authenticate(
config['credentials'],
config['cookie']['name'],
config['cookie']['key'],
config['cookie']['expiry_days']
)

func_num = {
    "Function 1": function1,
    "Function 2": function2,
    "Function 3": function3,
    "Function 4": function4,
    "Function 5": function5,
    "Function 6": function6,
    "Function 7": function7,
}



with st.sidebar:
    if(st.session_state.authentication_status == True):
        st.info("User: ***%s***" % st.session_state.username)
        authenticator.logout('Logout')
    
if(st.session_state.authentication_status == None or st.session_state.authentication_status == False):
    st.header("Please go to ***Home Page and login***!")

if(st.session_state.authentication_status == True):
    selected_func = st.sidebar.selectbox("Select a function!", func_num.keys(),disabled=False)
    func_num[selected_func]()