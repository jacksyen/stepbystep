#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Filename = seay.py
import os,sys

# 特征 可任意修改,满足需求即可
# 亦可采用字典文件方式
_tezheng = ['test','select','fuck']

def CheckFile(_path):
    # 只读方式打开需要分析的日志文件
    _f = open(_path,'r')
    # 将日志以行方式全部放入列表中
    _All_Line = _f.readlines()
    # 关闭文件
    _f.close()

    # 从第一行开始读取
    _Conut_Line = 0
    # 列表的长度(也就是日志总行数)
    _Len_Line = len(_All_Line)

    # 存在的特征(字典中定义)
    _Ex_Str = ''

    print 'Read Over --'

    # 循环读取每一行
    while _Conut_Line < _Len_Line:
        # 第_Conut_Line行的所有字符
        _Str = _All_Line[_Conut_Line]
        # 遍历特征字典
        for _tz_Str in _tezheng:
            # 如果字典中的特征在第_Conut_Line行的字符串中出现
            if _tz_Str in _Str: # 可以加and条件
                # 记录特征
                _Ex_Str += _tz_Str + _Str + '\r\n'
            _Conut_Line += 1

    # 将文件保存在脚本所在目录
    _f1 = open(_path.split('/')[-1] + '.seay.txt','w')
    # 将存在的特征写入文件
    _f1.write(_Ex_Str)
    _f1.close()
    print 'Find Over --'

if len(sys.argv) == 2:
    # 参数为日志文件
    _File = sys.argv[1]
    if os.path.lexists(_File):
        CheckFile(_File)
    else:
        print 'File does not exist!'
else:
    print 'Parameter error'
    print 'FilePath ' + sys.argv[0]
    print 'usage:python seay.py yourlogpath'
