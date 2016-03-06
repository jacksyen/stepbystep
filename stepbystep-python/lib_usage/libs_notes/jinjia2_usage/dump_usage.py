from jinja2 import Environment, PackageLoader

__author__ = 'patrick'

env = Environment(loader=PackageLoader('jinjia2_usage', 'templates'))
template = env.get_template('template.txt')

template.stream({"name":"simon patrick"}).dump('hello_name.txt','utf-8')