# -*- coding: utf-8 -*-

from jinja2 import Template

"""
so called context: name='simon patrick'

"""
__author__ = 'patrick'

template = Template('Hello {{name}}')
print(template.render(name='Simon Patrick'))

