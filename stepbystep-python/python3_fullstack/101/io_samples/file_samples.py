import pickle

file_name='test.txt'
with open(file_name, 'w') as f:
    f.write("1,2,3")

with open(file_name, 'r') as f:
    content = f.read()
    print(content)

with open(file_name,'r') as f:
    content=f.read(1)
    print(content)

with open(file_name,'r') as f:
    pickle.load(f)

## Read size 