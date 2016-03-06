# _*_ coding=utf-8 _*_
import random
__author__ = 'patrick'
'''
这是python中基本的查找方法，虽然简单，但是，如果由于其时间复杂度为O(n)，对于大规模的查询恐怕是不足以胜任的。二分查找就是一种替代方法。

二分查找的对象是：有序数组。这点特别需要注意。要把数组排好序先。怎么排序，可以参看我这里多篇排序问题的文章。

基本步骤：

从数组的中间元素开始，如果中间元素正好是要查找的元素，则搜素过程结束；
如果某一特定元素大于或者小于中间元素，则在数组大于或小于中间元素的那一半中查找，而且跟开始一样从中间元素开始比较。
如果在某一步骤数组为空，则代表找不到。
这种搜索算法每一次比较都使搜索范围缩小一半。时间复杂度：O(logn)
'''
a = [random.randint(1,10000) for i in range(100)]

print(a)

a=sorted(a, reverse=True)
print(a)

def binarySearch(a,low,high,key):
     if high<low:
         return -1
     else:
         mid = low/2+high-high/2
         if key == a[mid]:
             return mid
         elif key > a[mid] :
            return binarySearch(a,mid+1,high,key)
         else:
             return binarySearch(a,low,mid-1,key)

def binary_search_no_recusive(a,value):
    low,high=0,len(a)-1
    while low<high:
        mid = (low+high)/2
        if(a[mid]==value):
            return mid
        elif a[mid]>value:
            high =mid-1
        else:
            low=mid+1

    return -1

print(binarySearch(a,0,len(a)-1,1000))
print(binary_search_no_recusive(a,1000))
