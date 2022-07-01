import pymysql


con = pymysql.connect(host="localhost", user="root", password="lemon@123", database="damg7245", charset="utf8")
c = con.cursor()

def create_log_table():
    c.execute('CREATE TABLE IF NOT EXISTS log_table(logId varchar(255), userId int, level varchar(255), requestUrl varchar(255),code varchar(255),response varchar(255),logTime datetime,processTime double)') #数据格式问题

def create_user_table():
    c.execute('CREATE TABLE IF NOT EXISTS user_table(userId int, userName varchar(255), password varchar(255), full_name varchar(255), email varchar(255))')   
 
def insert_log_info(logId,userId, level, requestUrl, code, response, logTime, processTime):

    sql = "INSERT INTO log_table(logId,userId,level,requestUrl,code,response,logTime,processTime) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (0,0,0,0,0,0,0,0)
    c.execute(sql, val)
    con.commit()

def create_user_account(username:str,password=str,fullname="",email=""):
    
    sql = "INSERT INTO user_table(username,password,fullname,email) VALUES(%s,%s,%s,%s)"
    val = (username,password,fullname,email)
    con.commit()

def modify_user_account_info(username:str,password:str,fullname="",email=""):
    pass
# create_user_table()
