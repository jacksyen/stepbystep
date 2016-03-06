# _*_ coding=utf-8 _*_
__author__ = 'patrick'

import glob
import os

modules = []
print globals()
print glob.glob("*-plugin.py")

for module_file in glob.glob("*-plugin.py"):
    module_name, ext_name = os.path.splitext(os.path.basename(module_file))
    module = __import__(module_name)
    modules.append(module)

for module in modules:
    module.hello(module)


def get_function_by_name(module_name, function_name):
    module = __import__(module_name)
    return getattr(module, function_name)


try:
    print(repr(get_function_by_name("dumbdbm", "open")))
except:
    print("get error")


# lazy import
class LazyImport:
    def __init__(self, module_name):
        self.module_name = module_name
        self.module = None

    def __getattr__(self, name):
        if self.module is None:
            self.module = __import__(self.module_name)
        return getattr(self.module, name)

string = LazyImport("string")
print string.__getattr__("lowercase")
print string.lowercase
#todo to understand why

from basicpython.build_in_note.buildin import hello

reload(hello)



