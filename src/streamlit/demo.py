import os
import yaml
import requests
import json

headers = {'accept': 'application/json','Content-Type': 'application/x-www-form-urlencoded',}
url = 'http://127.0.0.1:8000/token/'
            
data = {'grant_type':'','username': "cheng","password":"cheng",'scope':'','client_id':'','client_secret':''}
            
#res = requests.post(url=url,params=data,headers=headers)
res = requests.post(url=url,data=data,headers=headers)
token = res.json()["access_token"]
print(res.text)

token_str = 'bearer ' + token
print(token_str)

#############################################################################


headers1 = {'accept': 'application/json','authorization': str(token_str)}
url1 = 'http://127.0.0.1:8000/api/get/fileNameAndClass'
data1 = {'className':'F22','current_user':'cheng'}
res1 = requests.get(url=url1,params=data1,headers=headers1)

print(type(res1.json()))