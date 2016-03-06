# _*_ coding=utf-8 _*_
__author__ = 'patrick'

class Other(object):
    def overrider(self):
        print "override"

    def altered(self):
        print "other alter!"

class Child(object):
    def __init__(self):
        self.other =Other()

    def override(self):
        self.other.overrider()

    def altered(self):
        self.other.altered()


child = Child()
child.altered()
child.override()