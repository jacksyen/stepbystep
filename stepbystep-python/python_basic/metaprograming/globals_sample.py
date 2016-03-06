import builtins

__author__ = 'patrick'


print( vars(globals()['__builtins__']) is vars(builtins))