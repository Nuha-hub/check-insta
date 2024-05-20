from flask import Flask, jsonify, request
import secrets,user_agent,requests,os
import requests
from user_agent import generate_user_agent
from requests import post
from requests import get
import requests,re,random,time
from user_agent import *
from hashlib import md5

app = Flask(__name__)

@app.route('/login/username=<email>/password=<password>/by/cc_02', methods=['GET'])
def login(email,password):
	ma = requests.Session()
	passwor = f"#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{password}"
	s3 = ma.get('https://www.instagram.com/accounts/login/')
	rs3 = ma.get('https://www.instagram.com/accounts/login/')
	ctk = rs3.text.replace("\\", "").split('csrf_token\":\"')[1].split('"')[0]
	headers = {
	            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
	            "x-csrftoken": ctk,
	            "x-ig-www-claim": "0",
	        }
	rs3 = ma.post(
	            "https://www.instagram.com/api/v1/web/accounts/login/ajax/",
	            headers=headers,
	data={
	                "enc_password": passwor,
	                "username": email,
	                "queryParams": "{}",
	                "optIntoOneTap": "false",
	                "trustedDeviceRecords": "{}"
	            },
	        )
	
	headers.update({"x-ig-set-www-claim":"0"})
	headers.update({"x-csrftoken": ctk})
	print(rs3.text)
	if "userId" in rs3.text:
		return f'Good Login✅ : {email}:{password}\nReq:{rs3.text}'
	elif "checkpoint_required" in rs3.text:
		return(f"CP ➗ :{email}:{password}\nReq:{rs3.tsxt}")
	else:
		return(f"bad❌ : {email}:{password}")

if __name__ == '__main__':
    app.run(debug=True)
