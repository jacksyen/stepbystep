dict_sample = {
    'key': 'test',
    'key1': 'test1'
}
dict_sample2 = dict_sample
dict_copy = dict_sample.copy()
print(id(dict_sample))
print(id(dict_sample2))
print(id(dict_copy))

matrix = {(0, 0, 0, 1, 0): 1,
          (0, 0, 0, 0, 0): 2,
          (0, 2, 0, 0, 0): 3,
          (0, 0, 0, 0, 0): 4,
          (0, 0, 0, 3, 0): 5}

for item in matrix:
    print(item)
    for sub_item in item:
        print(sub_item)
    print(matrix[item])

print(matrix.get((0, 0, 0, 2, 0), 2))

previous = {0: 0, 1: 1}


def fibonacci(n):
    if n in previous:
        return previous[n]
    else:
        new_value = fibonacci(n - 1) + fibonacci(n - 2)
        previous[n] = new_value
        return new_value


print(fibonacci(10))
print(previous)

letter_counter = {}
for letter in 'MIssissippi':
    letter_counter[letter] = letter_counter.get(letter, 0) + 1

print(letter_counter)
