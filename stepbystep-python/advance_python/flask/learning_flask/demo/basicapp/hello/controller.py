# _*_ coding=utf-8 _*_
from flask import Blueprint
from model import MESSAGES

__author__ = 'patrick'

c = Blueprint('basicapp',__name__)

@c.route('/')
def hello():
    return 'Hello Patrick'

@c.route('/default')
def default():
    return MESSAGES['default']

@c.route('/add/<key>/<value>')
def add(key,value):
    MESSAGES[key]=value
    return "Add Successfully!"