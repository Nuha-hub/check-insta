from flask import Flask, jsonify, request
import secrets,user_agent,requests,os
from threading import Lock
import rich
import concurrent.futures
import requests
from secrets import token_hex
import uuid
from user_agent import generate_user_agent
from requests import post
from requests import get
from AegosPy import GetInfoInsta


app = Flask(__name__)

@app.route('/check_email/<email>', methods=['GET'])
def chk(email):
	mm=requests.post(url="https://www.instagram.com/api/v1/web/accounts/account_recovery_ajax/", headers={"X-Csrftoken": "d98HmasrM5VNPmA6jl6lwBmsyk8kkk0n"}, data={"query": f"{email}"}).text 
	return jsonify(mm)	
if __name__ == '__main__':
    app.run(debug=True)
