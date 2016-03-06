# _*_ coding=utf-8 _*_
__author__ = 'patrick'


def function(a, b):
    return a + b

# apply common use:构造函数参数从子类传递到基类
print apply(function, (2, 3))
print apply(function, (), {"a": 2, "b": 3})


class Fruit():
    def __init__(self, color="green", taste="good"):
        self.color = color
        self.taste = taste

    def color(self):
        print self.color

    def taste(self):
        print self.taste


# interesting **kw
class Apple(Fruit):
    def __init__(self, **kw):
        apply(Fruit.__init__, (self,), kw)

# function(*args,*kw)
# apply(function,*args,*kw)
fruit = Fruit(color="green", taste="bad")
apple = Apple(color="red", taste="good")
fruit.color
fruit.taste