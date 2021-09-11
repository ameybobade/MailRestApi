from flask import Flask 
from flask_restful import Resource, Api, request, reqparse, abort      
import smtplib
from email.message import EmailMessage
from datetime import datetime

app = Flask(__name__)

@app.route("/",methods=["GET", "POST"])
def hello_world():
    name ="amey"
    msg = EmailMessage()
    msg['Subject']=str(request.args.get('subject'))
    msg['From']="hackathonviit@gmail.com"
    msg['To']=str(request.args.get('emailid'))
    print(str(request.args.get('emailid')))
    #cc="ameybobade1103@gmail.com,pmacoe.it@gmail.com"
    msg['Cc'] = (str(request.args.get('cc'))).split(',')
    msg['Bcc'] = (str(request.args.get('bcc'))).split(',')
    # msg['Bcc'] = bcc.split(',')
    msg.set_content(str(request.args.get('message')))
    # if file:
    #     file_data = file.read()
    #     file_name = file.name
    #     print(file_name)
        
    #     msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login("hackathonviit@gmail.com", "viithackathon")             
        smtp.send_message(msg)
    return "Welcome"

if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=80)
    app.run(debug=True)

# file = open('sbc.txt', 'r')
# This will print every line one by one in the file
# for each in file:
#     print (each)