# _*_ coding=utf-8 _*_
__author__ = 'patrick'

# explicit code

# bad
def make_complex(*args):
    x,y = args
    return dict(**locals())

print make_complex(1,1)

# good
def another_make_complex(x,y):
    return {'x':x,'y':y}

print another_make_complex(1,1)


for index,item in enumerate(range(10)):
    print index,item

file_name="foobar.txt"
base_name,_,ext = file_name.rpartition('.')
print _

# create length-N list of same things
four_nones = [None] * 4
print four_nones

four_lists = [[] for __ in xrange(4)]
print four_lists

d = {'s': [], 'p': [], 'a': [], 'm': []}
l = ['s', 'p', 'a', 'm']
def lookup_dict(d): return 's' in d
def lookup_list(l): return 's' in l

print(lookup_dict(d))  # hash table o(n)

# convention
attr='ddf'
if attr:
    print 'attr is truthy'

if not attr:
    print 'attr is falsey'

if attr ==None:
    print 'attr is NONE'

d ={'hello':'world'}
print d.get('hello1','default_value')
if 'hello' in d:
  print d['hello']

# short ways to manipulate the lists
a =[2,3,4,5]
b = [i for i in a if i>4]
print b

b = filter(lambda x:x >3,a)
print b

