__author__ = 'patrick'

li = ['my', 'name', 'is', 'patrick', 778, 0, 8]

print(li[0])
del li[2]
print(li)

li[2] = 'is'
print(li)

li[0:2] = ['test', 23, 45]
print(li)

for element in li:
    print(element)

# range
nums = range(30)
print(nums)
for num in nums:
    print(num)

initial_value = 2
# fix value
num_with_init = [initial_value for i in range(30)]
print(num_with_init)
# fix value
num_with_init = [initial_value] * 30
print(num_with_init)

# list => 动态数组 vector
l = list(range(1,5))
for t in l:
    print(t)

l_step=range(1,30,3)
for t in l_step:
    print(t)

l.append('test')
print(l)

l.insert(1,'test')
print(l)
print(l.pop())
print(l.remove(2))
print(l)