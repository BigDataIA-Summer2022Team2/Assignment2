import pymysql


con = pymysql.connect(host="localhost", user="root", password="1207", database="damg7245", charset="utf8")
c = con.cursor()

def create_log_table():
    c.execute('CREATE TABLE IF NOT EXISTS log_table(logId varchar, userId int)') #数据格式问题
    
#def insert_log_info(logId level, request_url, code, response, logtime, processtime):

sql = "INSERT INTO log_table(logId,userId,level,requestUrl,code,response,logTime,processTime) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
val = (0,0,0,0,0,0,0,0)
c.execute(sql, val)
con.commit()












