# _*_ coding=utf-8 _*_
import bisect
import heapq
import pprint
import re
import array
import weakref

__author__ = 'patrick'
import collections as cl
# from http://blog.jobbole.com/65218/
# count the number of times an element occurs
def test_counter():
    li = ["Dog", "Cat", "Mouse", 42, 42, "Cat", "Dog"]
    a = cl.Counter(li)
    print a
    print a.most_common()  # get all the duplicated words
    print len(set(li))  # group duplicated
    # group different words
    print "{0}:{1}".format(a.values(), a.keys())


def test_word_frequence():
    word_beds = """   Lorem ipsum dolor sit amet, consectetur
    adipiscing elit. Nunc ut elit id mi ultricies
    adipiscing. Nulla facilisi. Praesent pulvinar,
    sapien vel feugiat vestibulum, nulla dui pretium orci,
    non ultricies elit lacus quis ante. Lorem ipsum dolor
    sit amet, consectetur adipiscing elit. Aliquam
    pretium ullamcorper urna quis iaculis. Etiam ac massa
    sed turpis tempor luctus. Curabitur sed nibh eu elit
    mollis congue. Praesent ipsum diam, consectetur vitae
    ornare a, aliquam a nunc. In id magna pellentesque
    tellus posuere adipiscing. Sed non mi metus, at lacinia
    augue. Sed magna nisi, ornare in mollis in, mollis
    sed nunc. Etiam at justo in leo congue mollis.
    Nullam in neque eget metus hendrerit scelerisque
    eu non enim. Ut malesuada lacus eu nulla bibendum
    id euismod urna sodales.  """

    words = re.findall(r'\w+', word_beds)
    lower_words = [word.lower() for word in words]
    print lower_words

    word_count = cl.Counter(lower_words)
    print word_count
    # todo how to get the most frequent words


test_counter()
test_word_frequence()

# Deque
'''
 deque 是队列结构扩展的双端队列(double-ended queue)
 元素可以在两端添加或者删除,头尾连接队列head-tail linked list
 deque 线程安全的，经过优化的append,pop操作
'''


def test_deque():
    q = cl.deque(range(5))
    print q
    q.append(13)
    q.appendleft(22)
    print q
    print q.pop()
    print q
    print q.popleft()
    print q
    q.rotate(2)
    print(q)


test_deque()

# Default dict,almost same as dict,except when the key not exists
def test_default_dict():
    s = "the quick brown fox jump over"
    words = s.split()
    l = cl.defaultdict(list)
    for k, v in enumerate(words):
        l[v].append(k)
    print l

    d = {}
    for k, v in enumerate(words):
        d.setdefault(k, []).append(v)
    print d

    # same as Counter
    li = ["Dog", "Cat", "Mouse", 42, 42, "Cat", "Dog"]
    dd = cl.defaultdict(int)
    for k in li:
        dd[k] += 1
    print(dd)


test_default_dict()

# Array
def test_array():
    a = array.array('i', range(5))
    print a
    b = array.array(a.typecode, [x * 2 for x in a])
    print b
    for i, x in enumerate(a):
        a[i] = x * 2
    print a


test_array()

# heapq
def test_heapq():
    heap=[]
    for v in range(5):
        heapq.heappush(heap,v)
    print heap
    print heapq.heappop(heap)
    print heapq.nlargest(3,heap)

test_heapq()

# biset
def test_bisect():
    a=[1,2,6,89]
    bisect.insort_right(a,4)
    print a
    print bisect.bisect(a,3)

test_bisect()

# weakref
# todo understand this
def test_weakref():
    a=2
    b=a
    del b
    print "a:=",a

    class Foo():
        a=1

    f=Foo
    print "f=",f
    d=weakref.ref(f)
    del f
    print "d=",d

test_weakref()

### pprint
# beautiful print
def test_pprint():
    matrix = [ [1,2,3], [4,5,6], [7,8,9] ]
    a = pprint.PrettyPrinter(width = 20)
    a.pprint(matrix)

test_pprint()

if __name__ == '__main__':
    test_default_dict()
    test_pprint()
    test_deque()
    test_weakref()
    test_counter()
    test_heapq()
    test_array()
    test_bisect()
    test_word_frequence()