# -*- coding:utf-8 -*-

'''
题目要求:
C++实现X进制转化为Y进制函数,其中X和Y为2到64之间的任意数.
不允许使用任何库函数,如果必须使用,请自己实现.
如果用C或Java实现，请自己修改函数声明。

CString convert(int input_mod, CString input_value, int output_mod)
举例:
convert(10, "2", 2)=="10"  //把十进制的"2"转换为二进制,为"10"
convert(64, "f",10)=="15"  //把六十四进制的"f"转换为十进制,为"15"

'''

# 参数说明:
# input_mod:input_value的进制
# input_value:需要转换的数据(字符串类型)
# output_mod:转换成什么进制
# 返回转换后的数
def convert(input_mod,input_value,output_mod):
    '''64进制，所用的字符是“0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/”'''
    # 所有字符字典
    # _base64 = ['0','1','2','3''4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','+','/']
    rv = _any_to_10Mod(input_value,input_mod)
    rv = _10Mod_to_any(rv,output_mod)
    return rv

# 十进制转换成任意进制
def _10Mod_to_any(input_value_of_10_mod,output_mod):
    _base64 = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/'
    rv = []
    while input_value_of_10_mod != 0:
        rv.append(_base64[input_value_of_10_mod % output_mod])
        input_value_of_10_mod = input_value_of_10_mod / output_mod
    rv.reverse()
    return ''.join(rv)

# 任意进制的数据转换成十进制
def _any_to_10Mod(input_value,input_mod):
    _base64 = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/'
    rv = 0
    # 位数(数的长度)
    length = len(input_value)
    for i in range(length):
        # 标记
        index = 0
        # 查找在十进制中的位置
        for j in range(len(_base64)):
            if input_value[i] == _base64[j]:
                index = j
                break
        # 相加
        rv += index*(input_mod)**(length-i-1)
    return rv


print convert(64,'f',10)
print convert(10,"2",2)