# _*_ coding=utf-8 _*_
__author__ = 'patrick'

# 内置高阶函数
print (lambda x:x>2)(3) #=>true

# map filter 高阶函数

# python 一等函数
def create_adder(x):
    print x

    def adder(y):
        print y
        return x + y

    return adder

add_10 = create_adder(10)

print map(add_10,[1,2,3])
print [add_10(i) for i in [5,6,4,34]]

print filter(lambda x:x>5,[4,5,6,7,2,1])
print [x for x in [3,4,5,6,7,9] if x>5]

##############################################
## 5. class
##############################################
# 创建一个子类继承object来得到一个类
class Human(object):
    # 类属性
    species = "H. sapiens"

    def __init__(self,name):
        self.name=name

    def say(self,msg):
        return "%s:%s" %(self.name,msg)

    # 类方法所有实例共享
    @classmethod
    def get_species(cls):
        return cls.species

    # 静态方法的调用不需要一个类或实例的引用
    @staticmethod
    def grunt():
        return "***grunt***"

print Human.grunt()
i = Human(name="Ian")
print i.say("test")
print i.get_species()
j = Human(name="Joel")
print j.get_species()
print j.say("test2")