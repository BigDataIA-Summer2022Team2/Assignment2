import streamlit as st
import streamlit_authenticator as stauth
import yaml

#st.session_state
st.set_page_config(page_title="API Functions",page_icon=":heart:")

def function1():
    st.markdown("# Function 1 🎈")
    st.sidebar.markdown("# Function 1 🎈")

def function2():
    st.markdown("# Page 2 ❄️")
    st.sidebar.markdown("# Page 2 ❄️")

def function3():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")

def function4():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")

def function5():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")

def function6():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")

def function7():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")

with open('./config.yaml') as file:
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
    "Function 7": function7
}



with st.sidebar:
    if(st.session_state.authentication_status == True):
        st.info("User: %s" % st.session_state.username)
        authenticator.logout('Logout')
    
if(st.session_state.authentication_status == None or st.session_state.authentication_status == False):
    st.header("Please go to ***Home Page and login***!")

if(st.session_state.authentication_status == True):
    selected_func = st.sidebar.selectbox("Select a function!", func_num.keys(),disabled=False)
    func_num[selected_func]()