# _*_ coding=utf-8 _*_
__author__ = 'patrick'

class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go (self,direction):
        return self.paths.get(direction)

    def add_paths(self,paths):
        self.paths.update([paths])

