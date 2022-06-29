import streamlit as st
import streamlit_authenticator as stauth
import yaml
import datetime
import numpy as np
import pandas as pd
st.session_state

def modify_start_date_to_default():
    if(st.session_state.log_start > st.session_state.log_end):
        st.session_state.log_start = datetime.date(2022, 6, 29)    
        st.error("Start date should be earlier than or equal to end date")
    
def modify_end_date_to_default():
    if(st.session_state.log_end < st.session_state.log_start):
        st.session_state.log_end = datetime.date(2022, 6, 29)    
        st.error("End date should be later than or rqual to start date")

with open('./config.yaml') as file:
        config = yaml.safe_load(file)
        
authenticator = stauth.Authenticate(
config['credentials'],
config['cookie']['name'],
config['cookie']['key'],
config['cookie']['expiry_days']
)

with st.sidebar:
    if(st.session_state.authentication_status == True):
        st.info("User: %s" % st.session_state.username)
        authenticator.logout('Logout')
        
        options = st.multiselect(
            'What log info you want to get?',
            ['request URL', 'response', 'time', 'status code', 'username'],
            ['username','request URL', 'status code'],key="log_output_selection")
    
if(st.session_state.authentication_status == None or st.session_state.authentication_status == False):
    st.header("Please go to ***Home Page and login***!")

if(st.session_state.authentication_status == True):
    st.markdown("# Log Analysis")
    #st.markdown("## Try it :smile:")
    log_result = [['admin','127.0.0.1:8000/','200']]
   # print ( "Elephant" in simpDict.values() ) # check if item in dict values
    
    if("time" in options):
        log_start = st.date_input("Log Sart from",datetime.date(2022, 6, 29),key="log_start",on_change=modify_start_date_to_default)
        log_end = st.date_input("Log End",datetime.date(2022, 6, 29),key="log_end",on_change=modify_end_date_to_default)
        log_result[0].append('2022-6-29')
        log_result[0].append('2022-6-30')
        options.remove('time')
        options.append('start_time')
        options.append('end_time')
        # Todo: start time -> end time log query (if have time)
        # time_start = st.time_input('Set an alarm for', datetime.time(0, 0),key="time_start")
        # time_end = st.time_input('Set an alarm for', datetime.time(0, 0),key="time_end")
 
        # st.write('Start time', time_start)
        # st.write('End time', time_end)
        
        # st.write('Log start from:', log_start)
        # st.write('Log start from:', log_end)
     
    #df = pd.DataFrame(np.random.randn(10, 5),columns=('col %d' % i for i in range(5)))

    if('response' in options):
        log_result[0].append("{'error':'404 not found'}")
    
    
    df = pd.DataFrame(log_result, columns = options)
    st.table(df) 
    
    
    
    
    
    chart_data = pd.DataFrame(np.random.randn(10, 4),columns=["admin", "team1", "team3",'team4'])
    
    st.bar_chart(chart_data)


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
    
    
    
    st.write(log_result)  # value list  
    st.write(options) # title list

