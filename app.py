from flask import Flask, jsonify, request
import requests
from secrets import token_hex
import uuid
from user_agent import generate_user_agent
from requests import post
from requests import get
import random , hashlib , time

app = Flask(__name__)
def get_proxs():
	o=requests.get("https://github.com/Nuha-hub/check-insta/blob/main/proxies.txt").text
	oo='"]'
	m="["+o.split("['27.147.24.205:8080',")[1].split(f"'117.93.115.31:28643']{oo}")[0].strip()+"]"
	m = m.strip('[]').replace("'", "")
	my_list = m.split(',')
	proxy=random.choice(my_list)
	proxs= {'http': f'socks4://{proxy}'}
	return proxs

@app.route('/check_email/<email>', methods=['GET'])
def chk(email):
  ma = requests.Session()
  g = str(''.join(random.choice('qwertyuiopasdfghjklzxcvbnm') for i in range(8)))
  password = f"#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{g}"
  s3 = ma.get('https://www.instagram.com/accounts/login/')
  rs3 = ma.get('https://www.instagram.com/accounts/login/')
  ctk = rs3.text.replace("\\", "").split('csrf_token\":\"')[1].split('"')[0]
  headers = {
              "user-agent":generate_user_agent(),
              "x-csrftoken": ctk,
              "x-ig-www-claim": "0",
          }
  r=get_proxs()
  rs3 = ma.post("https://www.instagram.com/api/v1/web/accounts/login/ajax/",headers=headers,data={"enc_password": password,"username": email,"queryParams": "{}","optIntoOneTap": "false","trustedDeviceRecords": "{}"},proxies=r)

  headers.update({"x-ig-set-www-claim":"0"})
  headers.update({"x-csrftoken": ctk})
  return  jsonify(rs3.text)
if __name__ == '__main__':
    app.run(debug=True)
