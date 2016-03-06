# _*_ coding=utf-8 _*_
__author__ = 'patrick'
import requests

login_url = "http://192.168.3.129:8080/j_spring_security_check"
job_url = "http://192.168.3.129:8080"
get_cookie = requests.get(job_url)
cookie = get_cookie.cookies
user_data = {"j_username": "admin", "j_password": "admin", "remember_me": "", "from": ""}
r = requests.post(login_url, data=user_data, cookies=cookie);

# to do post to job url with cookie


