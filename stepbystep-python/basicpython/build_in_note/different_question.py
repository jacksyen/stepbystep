# -*- coding:utf-8 -*-

# 华为python笔试题
'''
有两个序列a、b,大小都为n,序列元素的值任意整形数,无序;
要求:通过交换a、b中的元素，使[序列a元素的和]与[序列b元素的和]之间的差最小
'''

'''
思路：
1. 将两序列合并为一个序列，并排序，为序列Source
2. 拿出最大元素Big，次大的元素Small
3. 在余下的序列S[:-2]进行平分，得到序列max，min
4. 将Small加到max序列，将Big加大min序列，重新计算新序列和，和大的为max，小的为min。
'''
_list1 = [11,2,95,31,1,8]
_list2 = [4,5,99,62,3,2]
def huawei(list1,list2):
    megre_list = sorted(list1 + list2)
    big = megre_list.pop()
    small = megre_list.pop()
    l1_big = megre_list[::-2]
    l2_small = megre_list[-2::-2]
    l1_big.append(small)
    l2_small.append(big)
    print "交换前的两个序列为:",list1,list2,",差为:",abs(sum(list1)-sum(list2))
    print "交换后的两个序列为:",l1_big,l2_small,",差为:",abs(sum(l1_big)-sum(l2_small))
huawei(_list1,_list2)  # 这个我呵呵了,交换前差为27,交换后变成33了,呵呵呵呵呵。。。。。



# 兔子问题
'''
有一对兔子，从出生后第三个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，如果兔子都不死，问每个月的兔子总数为多少？
思路：分析每个月的兔子：
第一个月-----------------1
第二个月-----------------1
第三个月-----------------2
第四个月-----------------3
第五个月-----------------5
第六个月-----------------8
第七个月-----------------13
从中发现，从第三个月开始，前两个月兔子数之后为第三个兔子总数
'''
def tuzi(month):
    tuzi = []
    tuzi.append(1)
    tuzi.append(1)
    for i in range(month):
        if i == 0 or i == 1:
            print "第%d个月兔子数量为:1对"%(i+1)
        else:
            tuzi.append(tuzi[i-1]+tuzi[i-2])
            print "第%d个月兔子数量为:%d对"%(i+1,tuzi[i])

def tuzi_youhua(month):
    result = []
    a,b = 1,1
    for i in range(month):
        # yield a
        result.append(a)
        a,b = b,a+b
    return result

def tuzi_digui(month):
    if month == 0 or month == 1:
        return 1
    else:
        return tuzi_digui(month-1) + tuzi_digui(month - 2)

print tuzi_youhua(10)



# 轩辕互动面试题
'''
1.平衡点问题
平衡点：比如int[] numbers = {1,3,5,7,8,25,4,20}; 25前面的总和为24，25后面的总和也是24，25这个点就是平衡点；假如一个数组中的元素，其前面的部分等于后面的部分，那么这个点的位序就是平衡点
要求：返回任何一个平衡点
2.支配点问题：
支配数：数组中某个元素出现的次数大于数组总数的一半时就成为支配数，其所在位序成为支配点；比如int[] a = {3,3,1,2,3};3为支配数，0，1，4分别为支配点；
要求：返回任何一个支配点
'''
def balance_point():
    pass
def dominant_point():
    pass