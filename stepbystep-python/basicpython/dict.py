# _*_ coding=utf-8 _*_
d = {
    95: 'Adam',
    85: 'Lisa',
    59: 'Bart'
}

d[72]='Paul'
d[73]="Paul"

print d

for key in d:
    print key,":",d[key]
    print key,":",d.get(key)


