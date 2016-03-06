# _*_ coding=utf-8 _*_
from flask import json

__author__ = 'patrick'

json_string='{"key":"value"}'

parsed_json = json.loads(json_string)
print parsed_json["key"]