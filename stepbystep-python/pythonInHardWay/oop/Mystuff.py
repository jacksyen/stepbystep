__author__ = 'simon'
# _*_ coding:utf-8 _*_

# 定义类
class MyStuff(object):
    def __init__(self):  # 初始化类，构造器
        self.target = "Andriod"
# self 就是 this
    def apple(self):
        print self.target
        print "test apple"

# 实例化
myStuff = MyStuff()
myStuff.apple()

class Song(object):
    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_song = Song(["this is first","this is second"])
happy_song.sing_me_a_song()

print happy_song.__dict__
print happy_song.__hash__()
print happy_song.__module__;