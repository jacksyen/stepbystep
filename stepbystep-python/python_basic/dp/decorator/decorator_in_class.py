from functools import wraps

__author__ = 'patrick'


def p_decorate(func):
    @wraps(func)
    def func_wrapper(self):
        return "<decorator>{0}</decorator>".format(func(self))

    return func_wrapper


def tags(tag_name):
    def tags_decorator(func):
        @wraps(func)
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))

        return func_wrapper

    return tags_decorator


class Person(object):
    def __init__(self):
        self.name = "simon"
        self.family = "patrick"

    @p_decorate
    def get_fullname(self):
        return self.family + self.name

    @tags('ppp')
    def get_tag(self):
        return self.family


my_person = Person()
print(my_person.get_fullname())
print(my_person.get_tag())
print(my_person.get_fullname.__name__)
