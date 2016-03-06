import ast

__author__ = 'patrick'


class AwesomeRegistry(type):
    registry = {}

    def __new__( mcs, name, bases, d):
        rv = type.__new__(mcs, name, bases, d)
        registry[name] = rv

    def __getitem__(self, name):
        return self.registry[name]

class AwesomeBase(object):
    __metaclass__= registry


## exec compile

def func_from_file(filename,function):
    namespace={}
    execfile(filename,namespace)

func = func_from_file('hello.cfg','main')
func()


