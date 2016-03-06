__author__ = 'patrick'

dict_sample = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}

result = filter(lambda t: t['Alice'] == '2341', dict_sample)
print(result)
# error
# for i in result:
#     print(i)

list_sample = [{"name": "alice"}, {"name": "patrick"}]
result = filter(lambda t: t["name"] == "alice", list_sample)
print(result)

for i in result:
    print(i)
