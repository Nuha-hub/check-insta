from flask import Flask, jsonify, request
import requests
import time
from user_agent import generate_user_agent

app = Flask(__name__)

@app.route('/login/username=<email>/password=<password>/by/cc_02', methods=['GET'])
def login(email, password):
    ma = requests.Session()
    passwor = f"#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{password}"
    s3 = ma.get('https://www.instagram.com/accounts/login/')
    rs3 = ma.get('https://www.instagram.com/accounts/login/')
    ctk = rs3.text.replace("\\", "").split('csrf_token\":\"')[1].split('"')[0]
    
    user_agent = request.headers.get('User-Agent')
    headers = {
        "user-agent": user_agent,
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
        }
    )
    
    headers.update({"x-ig-set-www-claim": "0"})
    headers.update({"x-csrftoken": ctk})
    
    response_text = rs3.text
    if "userId" in response_text:
        return f'Good Login✅ : {email}:{password}\nUser-Agent: {user_agent}\nReq: {response_text}'
    elif "checkpoint_required" in response_text:
        return f"CP ➗ :{email}:{password}\nUser-Agent: {user_agent}\nReq: {response_text}"
    else:
        return f"bad❌ : {email}:{password}\nUser-Agent: {user_agent}\nReq: {response_text}"

if __name__ == '__main__':
    app.run(debug=True)
