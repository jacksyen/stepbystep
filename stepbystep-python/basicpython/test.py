__author__ = 'patrick'

# coding: utf-8
import sys  # 导入sys模块
import random  # 导入内置随机模块

N = 10  # 样本个数   后面改为N=1000000
Number = []
encryptedNumber = []
decryptedNumber = []
encryptedSuccess = 0
decryptedSuccess = 0
success = 0
error = 0

for i in range(0, N):
    num=random.randint(1, 1000)
    n = random.randint(0, len(str(num)))
    num = str(num)[:n] + '*' + str(num)[n:]
    # a = '#*,+'
    # num = a.join(str(num))
    Number.append(num)
    print(Number[i])
