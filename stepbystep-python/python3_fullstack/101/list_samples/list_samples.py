int_list = [10, 20, 30, 40]
str_list = ["spam", "bungee", "swallow"]
int_list.sort(reverse=True)
print(int_list)
print(str_list)

## nested_list
nested_list = ["hello", 2.0, 5, [10, 20]]
for item in nested_list:
    if (isinstance(item, list)):
        for sub_item in item:
            print(sub_item)
    else:
        print(item)

# list deletion

print(nested_list)

# metrics
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for item1 in matrix:
    for item in item1:
        print(item)

# string is list
for item in "test string":
    print(item)