# _*_ coding=utf-8 _*_
__author__ = 'patrick'

"""
    list: 列表
    tuple ：元组
    dictionaries ：字典 hash table
    sets: 集合
"""

sample = [1, ["another", "list"], ("a", "tuple")]
mylist = ["List Item 1", 2, 3.14]
print mylist[0]
print mylist[-1]
mydict = {"Key 1": "Value 1", 2: 3, "pi": 3.14}
print mydict["pi"]
myfunction = len
print myfunction(mydict)

# list
print mylist[:3]
print mylist[-3:-1]

# tuple
myTuple=(1,2,3)
print myTuple[1]
print myTuple[0::2]