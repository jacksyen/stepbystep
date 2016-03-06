#_*_ coding:utf-8 _*_
__author__ = 'patrick'

hairs = ["brown", "blue", "green"]

for hair in hairs:
    print hair

## 二维列表
data = [[1, 2, 3],[4 ,4 ,5, 6]]

for data in data:
    print data
    print data.__class__
    print isinstance(data, type)
    ### how to find the type of variable
    for i in data:
        print i

data.append("234")
print data

print exit(0)

