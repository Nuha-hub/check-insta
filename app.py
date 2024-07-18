from flask import Flask, jsonify, request
import secrets,user_agent,requests,os
from threading import Lock
import requests
from secrets import token_hex
import uuid
from user_agent import generate_user_agent
from requests import post
from requests import get
import json


app = Flask(__name__)

@app.route('/change_username/session=<sess>/username=<username>', methods=['GET'])
def cohange(username,sess):
	def getMe(sessionid):
			re = requests.get('https://i.instagram.com/api/v1/accounts/current_user/?edit=true', headers={'User-Agent': 'Instagram 136.0.0.34.124 Android (23/6.0.1; 640dpi; 1440x2560; samsung; SM-G935; hero2lte; samsungexynos8890; en_US; 208061712)', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'x-ig-app-id': '936619743392459'}, cookies={"sessionid": (sessionid)},timeout=6).text
			if 'message' in re: print('- error sessionid')
			re = json.loads(re)
			return re['user']['email'],re['user']['phone_number'],re['user']['full_name']
	
	
	def change(username=str,email=str,sess=str,phone=str,name=str):
		url = "https://www.instagram.com/api/v1/web/accounts/edit/"
		payload = {
		    "biography": f"telegram : @cc_02",
		    "chaining_enabled": "",
		    "email": f"{email}",
		    "external_url": "",
		    "first_name": f"{name}",
		    "phone_number": phone,
		    "username": f"{username}"
		}	
		headers = {
		  'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
		  'Content-Type': "application/x-www-form-urlencoded",
		  'referer': "https://www.instagram.com/accounts/edit/",
		  'x-requested-with': "XMLHttpRequest",
		  'x-ig-app-id': "1217981644879628",
		  'x-asbd-id': "129477",
		  'x-csrftoken': "k1p6uVvQPg1AotcLDBA1j6ZcVy6Av21r",
		  'origin': "https://www.instagram.com",
		  'sec-fetch-dest': "empty",
		  'sec-fetch-site': "same-origin",
		  'x-instagram-ajax': "1013407291",
		  'x-ig-www-claim': "hmac.AR1LQ3DDGLQ2vgXtK9fYa1v6YN-R3qDBG0fbdCTeV5lXVfg4",
		  'accept-language': "ar",
		  'sec-fetch-mode': "cors",
		  'Cookie': f"csrftoken=k1p6uVvQPg1AotcLDBA1j6ZcVy6Av21r; ds_user_id=3274566085; rur=\"CLN\\0543274566085\\0541746837782:01f7fc53dde0e7a13a3db0ac87debc934ed959b1c2f8b4b2ee36a9800f5f2c997bcee2e1\"; sessionid={sess}; shbid=\"13497\\0543274566085\\0541746739892:01f73f1ca5762f89b744b61ee0dd9afd5fca002076bfa3d67dda11a987783bb188712a8e\"; shbts=\"1715203892\\0543274566085\\0541746739892:01f71d73c950f9380081ca4fe8c61198932b53dfa00ec8fdc685ad9109616c05bab7a956\"; dpr=2; ps_l=1; ps_n=1; ig_did=4AF63F23-BB45-45B2-A81B-B7F9158258E0; ig_nrcb=1; mid=ZNslaAAAAAECVYMQxCk4LEmZ3BAN; datr=ZCXbZGzqtYWhCkRH-23IiH9A"
		}
		
		response = requests.post(url, data=payload, headers=headers)
		print(response.text)
		if '''{"status":"ok"}''' in response.text:
			return ({'username':username,'status':'Done','By':'@cc_02'})
		else:
			return ({'username':username,'status':'bad','By':'@cc_02'})
	try:
		getMe(sess)
		email,phone,name=getMe(sess)
		return change(email=email,sess=sess,username=username,phone=phone,name=name)
	except:
		return ({'username':username,'status':'bad session','By':'@cc_02'})
	

if __name__ == '__main__':
    app.run(debug=True)
