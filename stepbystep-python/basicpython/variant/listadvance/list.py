# _*_ coding=utf-8 _*_
__author__ = 'patrick'

# functional

# just like guava use preconditon or function in java
square = [x**2 for x in range(10)]
print square

aliqueto =[n for n in range(100) if n%3==0]
print aliqueto

print range(3,100,3)

print [one.strip() for one in ["1232","  345  ","  33 445"]]

# enumerate
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print list(enumerate(seasons))

# enumerate with function
def beatify(pos, element):
    return "%d:%s"%(pos,element)

print [beatify(i,element) for i,element in enumerate(seasons)]
# enumerate with lamba
func= lambda i,element:"%d:%s"%(i,element)
print [func(i,element) for i,element in enumerate(seasons)]
