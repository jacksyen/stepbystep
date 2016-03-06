from jinja2 import Environment, PackageLoader
from jinjia2_usage.java_bean import JavaBean

__author__ = 'patrick'

if __name__ == '__main__':
    bean = JavaBean()
    bean.name_class('Test')
    bean.member('name').member('age')
    env = Environment(loader=PackageLoader('jinjia2_usage', 'templates'))
    env.get_template('JavaBean.java')\
        .stream(bean.to_json()).dump(bean.class_name+".java")