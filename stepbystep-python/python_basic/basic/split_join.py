__author__ = 'patrick'

li= ['my','name','is','patrick']
print(' '.join(li))

print('_'.join(li))

b='\\'.join(li)
print(b)
t=b.split('\\')
print(t)
t=b.split('\\',1)
print(t)
t=b.split('\\',2)
print(t)
