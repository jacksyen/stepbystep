__author__ = 'patrick'

code =compile('a=1+2','<string>','exec')
ns={}
exec(code in ns)
ns['a']
print(code)