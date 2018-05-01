from math import sqrt
class vector(object):
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def getx(self):
        return self.x
    def gety(self):
        return self.y

    def add(self, other):
        return vector(self.x+other.x, self.y+other.y)

    def sub(self, other):
        return vector(self.x-other.x, self.y-other.y)

    def mul(self, other):
        return vector(self.x*other, self.y*other)

    def div(self, other):
        return vector(self.x/float(other), self.y/float(other))

    def dot(self, other):
        return self.x*other.x + self.y*other.y

    def dist(self, other):
        return sqrt((self.x-other.x)**2+(self.y-other.y)**2)

    def mag(self):
        return sqrt(self.x**2 + self.y**2)

