"""
python everything is object,
object is the base class in new style class.
But how is the object, type and class?
"""


class A:
    pass


class B(object):
    pass


class C(type):
    pass


class D(dict):
    pass


a = A()
b = B()
d = D()
instance_list = a, b, d
print(object)
print(type)

for instance in instance_list:
    print(type(instance))
    print(instance.__class__)
    print(instance
          , isinstance(instance, object)
          , isinstance(instance, type))
