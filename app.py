import requests,time,random
from user_agent import *
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

@app.route('/check/username=<username>', methods=['GET'])
def chk(username):
	io=requests.get("https://www.instagram.com/accounts/login/")
	csrf=(io.cookies.get_dict()['csrftoken'])
	url = "https://www.instagram.com/api/v1/web/accounts/web_create_ajax/"
	payload = {
		'enc_password':f'#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:132132132aa.je',
		'email':'find5zxz@gmail.com',
		'first_name':'Hasan',
		'username':f'{username}'
	}
	headers = {
	  'User-Agent':generate_user_agent(),
	  'Content-Type': "application/x-www-form-urlencoded",
	  'x-csrftoken': csrf,
	  'x-ig-www-claim': "0",
	  'Cookie': "csrftoken="+csrf
	}
	
	response = requests.post(url, data=payload, headers=headers)
	headers.update({'x-ig-www-claim':'0'})
	headers.update({'Cookie': "csrftoken="+csrf})
	headers.update({'x-csrftoken': csrf})
	return(response.text)


if __name__ == '__main__':
    app.run(debug=True)
