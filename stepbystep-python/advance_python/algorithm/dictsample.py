# _*_ coding=utf-8 _*_
__author__ = 'patrick'

person = {"name":"patrick","site":"www.baidu.com"}
print(person)
print person["name"]
print person["site"]

# put to a dict
name  = (["first","google"],["second","yahoo"])
print dict(name)

for key in person:
    print key+person[key]

