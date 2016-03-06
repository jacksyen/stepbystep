__author__ = 'simon'
# _*_ coding:utf-8 _*_
# List
hairs = ["brown", "blond", "red"]
eyes = ['brown', 'blue', 'black']
eyes = [1, 'brown', 3, 'blue', 'black']

for hair in hairs:
    print hair

for eye in eyes:
    print eye

for i in range(1, 6, 2):
    print i

# two dimension
two_dimension = [[1, 2, 3], [4, 5, 6], 123]
for result in two_dimension:
    if isinstance(result, tuple):
        print result
    else:
        print result, "single"

two_dimension.append([3, 4, 5, 6, 7])

print two_dimension

#orinal number/cardinal number

# dictionary hash  map
stuff ={'name': 'zed', 'key': 'value'}
print stuff['name']
print stuff["key"]


class Song(object):
    def __init__(self, lyrics):
        self.lyrices = lyrics

    def sing_me_a_song(self):
        for line in self.lyrices:
            print line

happy = Song(["this is test", "t", "test"])
happy.sing_me_a_song()

