class PropClass(object):
    def __init__(self, x):
        self.x = x

    # def __getattribute__(self, item):
    #     val = super(PropClass, self).__getattribute__(item)
    #     if callable(val):
    #         arg_count = len(inspect.getargspec(val).args)
    #         if arg_count == 1:
    #             return val()
    #         else:
    #             return val
    #     else:
    #         return val

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x


pro_class = PropClass(1023)
print(pro_class.x)
