from flask import Flask, jsonify, request
import requests
from user_agent import generate_user_agent
import re
import time

app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login():
    email = request.args.get('username')
    password = request.args.get('password')
    
    if not email or not password:
        return jsonify({"error": "username and password required"}), 400

    session = requests.Session()
    passwor = f"#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{password}"
    rs3 = session.get('https://www.instagram.com/accounts/login/')
    ctk = re.search(r'csrf_token":"(.*?)"', rs3.text).group(1)

    headers = {
        "user-agent": generate_user_agent(),
        "x-csrftoken": ctk,
        "x-ig-www-claim": "0",
    }
    
    response = session.post(
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
    
    if "userId" in response.text:
        return jsonify({"status": "Good Login", "email": email, "password": password, "response": response.text})
    elif "checkpoint_required" in response.text:
        return jsonify({"status": "Checkpoint Required", "email": email, "password": password, "response": response.text})
    else:
        return jsonify({"status": "Bad Login", "email": email, "password": password, "response": response.text})

if __name__ == '__main__':
    app.run(debug=True)
