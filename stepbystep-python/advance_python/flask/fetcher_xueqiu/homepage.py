# _*_ coding=utf-8 _*_
import json
import requests

__author__ = 'patrick'

url = "http://www.xueqiu.com/p/ZH176890"
headers ={"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36",\
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
        }

 # r = requests.get(url,headers=headers)
# print r.headers
# print r.text

json.dumps({'public':'true'})
r=requests.post(url,headers=headers)
print r.status_code

