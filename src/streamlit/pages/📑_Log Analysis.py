import streamlit as st
import streamlit_authenticator as stauth
import yaml
import datetime
import numpy as np
import pandas as pd
import pymysql
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import altair as alt
import seaborn as sns

st.session_state

def modify_start_date_to_default():
    if(st.session_state.log_start > st.session_state.log_end):
        st.session_state.log_start = datetime.date(2022, 6, 29)    
        st.error("Start date should be earlier than or equal to end date")
    
def modify_end_date_to_default():
    if(st.session_state.log_end < st.session_state.log_start):
        st.session_state.log_end = datetime.date(2022, 6, 29)    
        st.error("End date should be later than or rqual to start date")

with open('./streamlit_config.yaml') as file:
        config = yaml.safe_load(file)
        
authenticator = stauth.Authenticate(
config['credentials'],
config['cookie']['name'],
config['cookie']['key'],
config['cookie']['expiry_days']
)

#abs_path
#con = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_database, charset="utf8")
#Todo
con = pymysql.connect(host='localhost', user='root', password='lemon@123', database='damg7245', charset="utf8")
c = con.cursor()

with st.sidebar:
    if(st.session_state.authentication_status == True):
        st.info("User: ***%s***" % st.session_state.username)
        authenticator.logout('Logout')
        
        options = st.multiselect(
            'What log info you want to get?',
            ['logId','requestUrl','userId', 'response', 'logTime', 'code_', 'username','level_','processTime'],
            ['logId','username','requestUrl','code_','level_'],key="log_output_selection")
    
if(st.session_state.authentication_status == None or st.session_state.authentication_status == False):
    st.header("Please go to ***Home Page and login***!")

if(st.session_state.authentication_status == True):
    st.markdown("# Log Analysis")
    #st.markdown("## Try it :smile:")
    
    sql = "SELECT "
    # sql_lmit = "LIMIT 10"
    for item in options:
        if(item == options[-1]):
            sql = sql + "lt." + str(item)
        else:
            if(item == "username"):
                sql = sql + "ut."+str(item) + ", "
            else:
                sql = sql + "lt." + str(item) + ", "
        
    sql = sql + " FROM log_table lt INNER JOIN user_table ut ON lt.userId = ut.userId WHERE ut.username = '" + st.session_state.username + "' LIMIT 10"
    #st.write(sql)
    c.execute(sql)
    result = c.fetchall()
    #st.write(result)
    df = pd.DataFrame(result, columns = options)
    st.table(df) 
    
    
    if("time" in options):
        log_start = st.date_input("Log Sart from",datetime.date(2022, 6, 29),key="log_start",on_change=modify_start_date_to_default)
        log_end = st.date_input("Log End",datetime.date(2022, 6, 29),key="log_end",on_change=modify_end_date_to_default)
        
        # Todo: start time -> end time log query (if have time)
        # time_start = st.time_input('Set an alarm for', datetime.time(0, 0),key="time_start")
        # time_end = st.time_input('Set an alarm for', datetime.time(0, 0),key="time_end")
 
        # st.write('Start time', time_start)
        # st.write('End time', time_end)
        
        # st.write('Log start from:', log_start)
        # st.write('Log start from:', log_end)
    
   
    if( st.session_state["username"] != "cheng" and st.session_state["username"] != "meihu" and st.session_state["username"] != "admin"):
        
       
        c.execute("SELECT COUNT(*) FROM log_table lt INNER JOIN user_table ut on lt.userId = ut.userId WHERE ut.username ='" + st.session_state.username + "'")
        count_current_user_log = c.fetchall()[0][0]
        
        c.execute("SELECT COUNT(*) FROM log_table lt INNER JOIN user_table ut on lt.userId = ut.userId WHERE ut.username ='" + st.session_state.username + "' AND lt.code_= 200")
        count_success_user_log = c.fetchall()[0][0]
        #st.write(count_success_user_log)
         #Creating the dataset
        keys = ["success","fail","all"]
        #keys.append(st.session_state.username)
        values = [count_success_user_log,count_current_user_log-count_success_user_log,count_current_user_log]
        #values.append(count_current_user_log)

        fig = plt.figure(figsize = (6, 3))

        plt.bar(keys, values)
        #plt.xlabel("Users")
        #plt.xlabel(st.session_state.username)
        plt.ylabel("Number of API functions calling")
        plt.title(st.session_state.username + "'s API Functions Call Bar Chart")
        st.pyplot(fig)
        
        ###########################################
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = 'pass', 'fail'
        sizes = [count_success_user_log, count_current_user_log-count_success_user_log]
        explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        ax1.set_title(st.session_state.username + "'s API functions Call Pie Chart")
        st.pyplot(fig1)
        
        
    
    #chart_data = pd.DataFrame(np.random.randn(10, 4),columns=["admin", "team1", "team3",'team4'])
    
    #st.bar_chart(chart_data)


    df1 = pd.DataFrame({
        'month': ["01 Jan","02 Feb","03 Mar","04 Apr","05 May","06 Jun","07 July","08 Aug","09 Sep","10 Oct","11 Nov","12 Dec"],
        'team1': [1, 7, 5, 2,4,6,7,5,9,2,12,4],
        'team3': [7, 2, 8, 4,5,1,9,4,7,8,5,1],
        'team4': [3, 6, 5, 7,9,1,8,6,7,5,6,9],
        'admin': [4, 6, 8, 1,5,3,6,6,4,1,10,2],
    })

    df1 = df1.rename(columns={'month':'index'}).set_index('index')

    st.line_chart(df1)
    

    st.bar_chart(df1)
    
    
    
    #st.write(log_result)  # value list  
    st.write(options) # title list

