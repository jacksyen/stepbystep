__author__ = 'patrick'

missing = object()


class cached_property(object):
    def __init__(self, func):
        self.func = func
        self.__name__ = func.__name__
        self.__doc__ = func.__doc__
        self.__module__ = func.__module__

    def __get__(self, instance, type=None):
        if instance is None:
            return self
        value = instance.__dict__.get(self.__name__, missing)
        if value is missing:
            value = self.func(instance)
            instance.__dict__[self.__name__] = value
        return value


class Post(object):
    def __init__(self, text):
        self.text = text

    @cached_property
    def rendered_text(self):
        return self.text

Post('test').rendered_text()
