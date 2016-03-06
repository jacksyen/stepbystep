# _*_ coding=utf-8 _*_
from flask import Flask
from hello.controller import c

__author__ = 'patrick'

app = Flask(__name__)
app.register_blueprint(c)