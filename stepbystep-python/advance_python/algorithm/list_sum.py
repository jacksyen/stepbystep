# _*_ coding=utf-8 _*_
__author__ = 'patrick'

def list_sum(numbers):
    if not numbers:
        return 0
    else:
        (f,rest)=numbers
        return f+list_sum(rest)

my_list = (1,(2,(3,None)))
print(type(my_list))

print(list_sum(my_list))
