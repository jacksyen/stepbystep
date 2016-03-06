# _*_ coding=utf-8 _*_
__author__ = 'patrick'

print dir(dict)

print help(dict.values)

person = {"name":"qiwsir","site":"qiwsir.github.io","language":"python"}
print person["name"]

mydict = {}
mydict["city"] = "New York"
mydict["Country"] = "USA"
print mydict

# tuple
name =(["name" ,"simon"] ,["firstname" ,"simon"])
name = dict(name)
print name

# fromkeys
website = {}
website = {}.fromkeys(("one","two"),["google","facebook"])
print website
for key in website:
    print key+":"+str(website[key])

# for k, v in website:
#    print k
#    print v

# HashTable/HashMap/dict/Map
website = {1:"google","second":"baidu",3:"facebook","twitter":4}
print website.keys()
print website.values()
print website.items()
print website.iteritems().__iter__
for k in website:
    print k, website[k]

for v in website:
    print v

copied_web = {"name":"test","test":"redhat","kevin":"smith"}
print copied_web
try:
    print copied_web.pop(1) # mutable
except KeyError,e:
    print e.args
print copied_web
website.update(copied_web)
print website
