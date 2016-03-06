import string

file_name = input('Enter the file name :')
counts = dict()
with open(file_name, 'r') as f:
    for line in f:
        line = line.translate(string.punctuation)
        print(line)
        words = line.lower().split()
        for word in words:
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1

print(counts)

lst = list()
for key, value in counts.items():
    lst.append((value, key))

lst.sort(reverse=True)
for key, value in lst:
    print(key, value)
print(lst)
