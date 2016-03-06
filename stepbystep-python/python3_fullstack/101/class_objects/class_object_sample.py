class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getattr__(self, item):
        return "this is " + item

    def get_position(self):
        return self.x, self.y


point = Point(1, 3)
print(point.x)
print(point.y)
print(point.e)
print(point.get_position())
print(point.get_position()[0])
print(point.get_position()[1])
