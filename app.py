import requests
from user_agent import *
from flask import Flask, jsonify, request
from secrets import token_hex
import uuid


app = Flask(__name__)

@app.route('/check_email/email=<email>', methods=['GET'])
def insta(email):
	url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
	headers = {'accept': '*/*',
	                'accept-encoding': 'gzip, deflate, br',
	                'accept-language': 'ar,en-US;q=0.9,en;q=0.8,ar-SA;q=0.7',
	                'content-length': '61',
	                'content-type': 'application/x-www-form-urlencoded',
	                'cookie': 'ig_cb=2; ig_did=BB52B198-B05A-424E-BA07-B15F3D4C3893; mid=YAlcaQALAAHzmX6nvD8dWMRVYFCO; shbid=15012; rur=PRN; shbts=1612894029.7666144; csrftoken=CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
	                'origin': 'https://www.instagram.com',
	                'referer': 'https://www.instagram.com/accounts/emailsignup/',
	                'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
	                'sec-ch-ua-mobile': '?0',
	                'sec-fetch-dest': 'empty',
	                'sec-fetch-mode': 'cors',
	                'sec-fetch-site': 'same-origin',
	                'user-agent': generate_user_agent(),
	                'x-csrftoken': 'CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
	                'x-ig-app-id': '936619743392459',
	                'x-ig-www-claim': 'hmac.AR0Plwj5om112fwzrrYnMNjMLPnyWfFFq1tG7MCcMv5_vN9M',
	                'x-instagram-ajax': '72bda6b1d047',
	                'x-requested-with': 'XMLHttpRequest'} 
	data = {
	                'email' : f'{email}',
	                'username': 'jsjdkxbdgdjseidnj',
	                'first_name': 'AA',
	                'opt_into_one_tap': 'True',
	                }
	req = requests.post(url, headers=headers, data=data)
	print(req.json())
	if "email_is_taken" in req.text:
		return jsonify({
   'by':'@iiyiu',
   'email':f'{email}',
   'message':'Available iG',
   'status':True
  })
	elif "spam" in req.text:
		return jsonify({
   'by':'@iiyiu',
   'email':f'{email}',
   'message':'spam - Api blocked from instagram',
   'status':"Blocked"
  })
	else:
		return jsonify({
   'by':'@iiyiu',
   'email':f'{email}',
   'message':'unAvailable iG',
   'status':False,
  })
insta("hassanjejeh@hotmail.com")



if __name__ == '__main__':
    app.run(debug=True)
