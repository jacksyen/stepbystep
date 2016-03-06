# _*_ coding=utf-8 _*_
__author__ = 'patrick'

'''
understand lambda
'''
add = lambda x,y:x+y
print add(1,2)

'''
understand filter(),map() and reduce()
'''
# filter内建的python实现
def modified_filter(function_or_none,sequence):
    filtered_seq=[]
    for item in sequence:
        if function_or_none(item):
            filtered_seq.append(item)
    return filtered_seq

function_or_none=lambda x:x%2==0
sequence =[1,2,3,4,5,6,7,8]
print filter(function_or_none,sequence)
print modified_filter(function_or_none,sequence)

# map 内建的python实现
def modified_map(function,sequence):
    mapped_seq=[]
    for item in sequence:
        mapped_seq.append(function(item))
    return mapped_seq

print map(lambda x:x*2,sequence)
print modified_map(lambda x:x*2,sequence)

# reduce 内建的python实现
def modified_reduce(function,sequence,initial=None):
    lseq=list(sequence)
    if initial is None:
        res=lseq.pop(0)
    else:
        res=initial
    for item in lseq:
        res=function(res,item)
    return res

print reduce(lambda x,y:x+y,sequence)
print modified_reduce(lambda x,y:x+y,sequence)