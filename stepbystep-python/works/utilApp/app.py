# _*_ coding=utf-8 _*_
import json
import requests

__author__ = 'patrick'

from flask import Flask, render_template

app = Flask(__name__)

username = "******"
password = "******"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/getPassword")
def get_integration_password():
    s = requests.Session()
    login_url = "http://login.****.org/login?usercode=%s&password=%s&companyId=1&encrypt=false" % (username, password)
    r = s.post(login_url, verify=False)
    get_password_url = "https://login.dooioo.org/rootPassword/get"
    login_cookie = r.cookies
    r = s.get(get_password_url, cookies=login_cookie, verify=False)
    data = json.dumps(r.content)
    return data['password']


@app.route("/setUserCode/<user_code>")
def set_user_code(user_code):
    username = user_code
    return "set user code successfully "


@app.route("/setpw/<pwd>")
def set_password(pwd):
    password = pwd
    return password


@app.route("/init/usercode/<user_code>/password/<pwd>")
def init(user_code, pwd):
    username = user_code
    password = pwd
    return username + ":" + password


if __name__ == '__main__':
    app.run(debug=True)
