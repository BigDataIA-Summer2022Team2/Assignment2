import streamlit as st
import pymysql

if 'count' not in st.session_state:
    st.session_state.count = 0

con = pymysql.connect(host="localhost", user="root", password="lemon@123", database="damg7245", charset="utf8")

c = con.cursor()
def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT, password TEXT)')

def add_userdata(username, password):

    if c.execute('SELECT username FROM userstable WHERE username = %s',(username)):
        st.warning("Username already exists. Please choose another one.")
    else:
        c.execute('INSERT INTO userstable(username,password) VALUES(%s,%s)',(username,password))
        con.commit()
        st.success("Congratulation! Your account has been created successfully.")

def login_user(username,password):
    if c.execute('SELECT username FROM userstable WHERE username = %s',(username)):
        c.execute('SELECT * FROM userstable WHERE username = %s AND password = %s',(username,password))
        data=c.fetchall()
        return data
    else:
        st.warning("Username does not exist! Please sign up for an account!")

def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data

def home():
    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")

def login():
    st.subheader("Login Page")

    username = st.text_input("username")
    password = st.text_input("password",type = "password")
    if st.button("Login"):
        logged_user = login_user(username,password)
        if logged_user:
            st.sidebar.success("Welcome {}".format(username))

            st.title("After login success, see content!")
               
        else:
            st.warning("Your username or password does not exist!")   
    
    

def sign_up():
    st.subheader("Sign Up")
    new_user = st.text_input("Username")
    new_password = st.text_input("Password",type = "password")

    if(new_user == None or new_user == ""):
        st.warning("Please do not leave a username blank!")
    elif(new_password == None or new_password == ""):
        st.warning("Please do not leave a password blank!")
    else:
        st.button("Sign Up")
        create_usertable()
        add_userdata(new_user,new_password)

    

def forget():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")

def logout():
    pass


page_name = {
    "Home Page": home,
    "Login": login,
    "Sign Up": sign_up,
    "forget": forget,
}

selected_page = st.sidebar.radio("Please Select.", page_name.keys(),disabled=False)
st.sidebar.button("Sign Out")
page_name[selected_page]()