# -*- coding:utf-8 -*-
import pymongo

connection = pymongo.Connection('localhost',27017)
#选择MyFirstMongoDB库
db = connection.MyFirstMongoDB

# 使用user集合
collection = db.user

# 添加单条数据到集合中
# user = {"name":"kiven","age":25}
# collection.insert(user)

#同时添加多条数据到集合中
# users=[{"name":"cui","age":"9"},{"name":"cui","age":"11"}]
# collection.insert(users)

#查询单条记录
print collection.find_one()

#查询所有记录
for data in collection.find():
    print data

#查询此集合中数据条数
print collection.count()

# 查看db下的所有集合
print db.collection_names()

#简单参数查询
for data in collection.find({"name":"kiven"}):
    print data

#使用find_one获取一条记录
print collection.find_one({"name":"kiven"})

#高级查询
print "__________________________________________"
print '''''collection.find({"age":{"$gt":"25"}})'''
print "__________________________________________"
for data in collection.find({"age":{"$gt":"25"}}).sort("age"):
    print data