from _ctypes import Structure
from ctypes import CDLL, c_int

# Shared Object of Linux, same as DLL
libc = CDLL('libc.so.6')
message_str = 'Hello World'
libc.printf("Test %s", message_str)


# Structure,Union
class BearRecipe(Structure):
    _fields = [
        ("amt_barley", c_int),
        ("amt_water", c_int)
    ]
