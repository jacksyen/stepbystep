class GetterAttr(object):
    def __init__(self):
        self.test_name = 'test_name'

    # fallback logic, called after __getattribute__ raise an exception
    def __getattr__(self, item):
        print(item)

    # care about recursions
    def __getattribute__(self, item):
        print("get Attribute is invoked", item)
        return super(GetterAttr, self).__getattribute__(item)
        # self.__dict__[item]=item
        # raise Exception('no attribute found')

    def __setitem__(self, key, value):
        print('setting item is invoked', key, value)
        super(GetterAttr, self).__setattr__(key, value)

    def __setattr__(self, key, value):
        print('setting attr is invoked')
        self.__dict__[key] = value


getter = GetterAttr()
print(getattr(getter, 'name'))
name = getter.name
test_name = getter.test_name
# should be none
print(name)
print(test_name)
getter.name = "name"
print(getter.name)
