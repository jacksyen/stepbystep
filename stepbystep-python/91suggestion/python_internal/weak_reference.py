from weakref import WeakValueDictionary


class Counter:
    _instance = WeakValueDictionary()

    @property
    def Count(self):
        return len(self._instance)

    def __init__(self, name):
        self.name = name
        self._instance[id(self)] = self
        print(name, 'created')

    def __del__(self):
        print(self.name, 'deleted')
        if self.Count == 0:
            print('Last Counter Object deleted')
        else:
            print(self.Count, 'Counter objects remaining')


x = Counter('first')
y = Counter('second')
# while True:
#     print('deleting')
"""
Without the explicit call to del,
__del__ is only called at the end of the program,
Counter and/or Count may have already been GC-ed by the time __del__ is
called (the order in which objects are collected is not deterministic).
 The exception means that Counter has already been collected.
You can’t do anything particularly fancy with __del__.
"""
