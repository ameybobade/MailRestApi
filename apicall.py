import requests as rq
from datetime import datetime
# BASE_URL = 'http://127.0.0.1:5000/'
BASE_URL = 'http://mailhelp.pythonanywhere.com/'
payLoad = {'emailid':'ameybobade@gmail.com','cc':"amey.21810866@viit.ac.in,pmacoe.it@gmail.com",'bcc':"ameybobade1103@gmail.com",'subject':'Testing Mail','message':'Testing Mail Mail Mail!!!!!!!!!!!!!!'}

response = rq.post(BASE_URL,params=payLoad)
print(response.json())
    