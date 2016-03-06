# _*_ coding=utf-8 _*_
from advance_python.datastructure.cache import SimpleContainer

__author__ = 'patrick'

my_cache = SimpleContainer(1000)
for i in xrange(20):
    my_cache.set('test'+str(i),'value'+str(i))


print my_cache.get("test1")
print my_cache
my_cache.clear()
my_cache.save()