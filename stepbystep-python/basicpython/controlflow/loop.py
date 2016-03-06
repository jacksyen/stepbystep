# _*_ coding=utf-8 _*_
__author__ = 'patrick'

a= "this is test"
b =["this","is","test"]
print a

for s in a:
    print s

for iterm in b:
    print iterm

for i in range(len(a)):
    print str(i)+":"+a[i]

# 找到1000被3整除的数
aliquot =[]
for i in range(100):
    if i%3==0:
        aliquot.append(i)
        print i
    else:
        # do nothing
        pass

print aliquot
