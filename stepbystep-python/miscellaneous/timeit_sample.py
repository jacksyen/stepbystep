# _*_ coding=utf-8 _*_
import timeit
import unittest
import types

__author__ = 'patrick'

# Timeit
# =================================

# Two basic examples to show how to use the bascis of timeit.


timeit.timeit("obj.method()", """
class SomeClass:
    def method(self):
        pass
obj=SomeClass()
""")

timeit.timeit("f()", """
def f():
    pass
""")

## Unit Testing
# ==================

class EmptyClass():
    pass


class TestAccess(unittest.TestCase):
    def test_should_add_and_get_attribute(self):
        self.object=object()
        self.object.new_attribute = True
        self.assertTrue(self.object.new_attribute)

    def test_should_fail_on_missing(self):
        self.assertRaises(AttributeError, lambda: self.object.undefined)


# Concrete subclass

class Test_EmptyClass(TestAccess):
    def setUp(self):
        self.object = EmptyClass()


class Test_NameSpace(TestAccess):
    def setUp(self):
        self.object = types.SimpleNamespace()


class Test_Object(TestAccess):
    def setUp(self):
        self.object = object()


def suite():
    s = unittest.TestSuite()
    s.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Test_EmptyClass))
    s.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Test_NameSpace))
    s.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Test_Object))
    return s


if __name__ == '__main__':
    t = unittest.TextTestRunner()
    t.run(suite())


def factorial(n):
    if n == 0: return 1
    return n * factorial(n - 1)


print ("5!==", factorial(5))