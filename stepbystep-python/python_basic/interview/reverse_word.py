__author__ = 'patrick'

words = "this is test!"
print(type(words.split(" ")[::-1]))
print(" ".join(reversed(words)))
print(" ".join(words.split(" ")[::-1]))


## print 1,1,2,3,5,8...

def f(n):
    if n <= 0:
        return 0
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    nums = [1, 1]
    temp1 = 1
    temp2 = 1
    for i in range(n - 2):
        append_num = temp1 + temp2
        nums.append(append_num)
        temp1 = temp2
        temp2 = append_num

    return nums



def fr(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1

print(type(f(3)))
print(f(3))
print(f(5))
print(f(10))
a = [1, 2, 4]
print(type(a))

print(f(100))
