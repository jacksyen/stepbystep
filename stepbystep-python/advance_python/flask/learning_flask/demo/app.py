# _*_ coding=utf-8 _*_
from flask import Flask

__author__ = 'patrick'

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello Flask World!"

if __name__ =='__main__':
    app.run(debug=True)