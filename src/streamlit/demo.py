import streamlit as st
import pymysql



global PAGE_SHOW; # 0:login page 1:register page
login_status = False
register_status = False
PAGE_SHOW = 0 

# if 'page_show' not in st.session_state:
#     st.session_state.page_show = 0


def displayLoginPage():
    st.header("Welcome to DAMG 7245 Team 2 Project")
    st.markdown("> You need access rights to join our API test!")

    username = st.text_input("Username",key="input_username")
    password = st.text_input("Password",type = "password",key="input_password")
    
    


    col1, col2,col3,col4,col5,col6,col7,col8,col9 = st.columns(9)
    with col1:
        isRegister = st.button("Register",key="register_button")
        st.write(isRegister)
        if(isRegister == True):
            
            PAGE_SHOW = 1
            #st.experimental_rerun()

    with col9:
        isClickOK = st.button("Login",key="login_button")

    st.markdown('<a href="mailto:wang.cheng3@northeastern.edu">Forget username or password</a>',unsafe_allow_html=True)

    if(username == "cheng" and password == "cheng"):
        login_status = True
        welcome_str = "Welcome " +  username
        st.success(welcome_str)
        PAGE_SHOW = 2
    elif(username == None or password == None):
        login_status = False
        st.error("Login  failed")
    else:
        st.write(username, password)
        st.warning("Something is wrong here! DEBUG!")



def displayRegisterPage():
    new_user = st.text_input("用户名")
    new_password = st.text_input("密码",type = "password")
    if(new_user == "cheng"):
        st.error("Username already exists!")
    else:
        register_status = True
        st.success("You have successfully created an account!")
        time.sleep(1)
        PAGE_SHOW = 2
        

def displayHomePage():
    st.header("Home Page")


if(PAGE_SHOW == 0):
    displayLoginPage()
if(PAGE_SHOW == 1):
    displayRegisterPage()
if(PAGE_SHOW == 2):
    
    displayHomePage()

    
    











