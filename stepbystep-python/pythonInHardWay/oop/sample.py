#_*_ coding=utf-8 _*_
__author__ = 'patrick'

#隐身继承
class Parent(object):
    def implicit(self):
     print("implicit class!")

class Child(Parent):
    pass

parent = Parent()
child = Child()

parent.implicit()
child.implicit()

##显示继承
class Test(object):
    def override(self):
        print "parent override"

class TestChild(Test):
    def override(self):
        print "child override"

test = Test()
testchild = TestChild()
test.override()
testchild.override()