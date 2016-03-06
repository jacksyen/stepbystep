# if-else
some_flag = True

if some_flag:
    print("flag is true")
else:
    print('flag is false')

# if-else-if
some_flag = False
if some_flag:
    print("flag is true")
elif some_flag is None:
    print('flag is None')
else:
    print('flag is False')

# inline if-else
print("this is" if some_flag else "this is not")

# FOR
list_sample = ('list1', 'list2', 'list3')
for item in list_sample:
    print(item)

print(item for item in list_sample)
for i in range(5):
    print(i)

# WHILE
while some_flag:
    print(list_sample)
    some_flag = False

# Break Continue
while True:
    if some_flag:
        break
    else:
        some_flag = True
