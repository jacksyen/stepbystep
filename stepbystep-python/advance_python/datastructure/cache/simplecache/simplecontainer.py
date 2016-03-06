# _*_ coding=utf-8 _*_
import sys

from advance_python.datastructure.cache import Container


__author__ = 'patrick'

class SimpleContainer(Container):



    # init
    def __init__(self,max_cache_size):
        self.max_cache_size=max_cache_size
        self._HOLDER=[]

    # PUT
    def set(self,k,v):
        tmp={}
        if self._size()<self.max_cache_size:
            tmp[k]=v
            self._HOLDER.append(tmp)
            del tmp
        else:
            self.delete()
        print self._HOLDER

    def _size(self):
        sys.getsizeof(self._HOLDER)

    def delete(self):
        self._HOLDER.pop(0)

    def clear(self):
        del self._HOLDER[:]

    def get(self, k):
        for cache in self._HOLDER:
            for c in cache:
                if cmp(c,k)==0:
                   return cache[k]
        else:
            return None

    def save(self):
        try:
            _f=open('_cache.dat','w+')
            _f.writelines(str(self._HOLDER))
        except Exception,e:
            print e
        finally:
            _f.close()
