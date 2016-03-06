# _*_ coding=utf-8 _*_
__author__ = 'patrick'
number_list=[1,2,3,4]
string_list=['a','b','c']
ages={'jone':24,'sarah':45}

print number_list[2]
print ages['jone']

# 列表式推导
ll=[1,2,3,4,5,6,7]
print [v*10 for v in ll]

timesten=dict([(v,v*10) for v in ll])
print timesten