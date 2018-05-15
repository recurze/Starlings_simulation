from random import uniform
from math import sqrt
from constants import *

class Boid(object):
    def __init__(self, x, y, vx, vy):
        self.posx = x
        self.posy = y

        self.velx = vx
        self.vely = vy

        self.neighbors = []

    def unit(self, x, y):
        mag = self.dist(0, 0, x, y)
        if mag == 0:
            mag = 1
        return (x/mag, y/mag)

    def wrapAround(self):
        w, h = WIDTH-59, HEIGHT-59
        self.posx = (self.posx + w) % w
        self.posy = (self.posy + h) % h

    def updateInfo(self, vx, vy):
        s = self.dist(0, 0, vx, vy)
        #if s>MAX_SPEED or s<MIN_SPEED:
        vx, vy = self.unit(vx, vy)
        #self.velx = vx*MAX_SPEED
        #self.vely = vy*MAX_SPEED
        s = uniform(0.3, 0.7)
        self.velx = vx*s
        self.vely = vy*s

        self.posx += self.velx
        self.posy += self.vely
        self.wrapAround()

    def setNeighbors(self, n):
        self.neighbors = n

    def go(self):
        a = self.alignment()
        c = self.cohesion()
        s = self.separation()
        b = self.bound()

        return (a, c, s, b)

    def dist(self, x1, y1, x2, y2):
        return sqrt((x1-x2)**2+(y1-y2)**2)

    # returns unit vector
    def unit(self, x, y):
        mag = self.dist(0, 0, x, y)
        if mag == 0:
            mag = 1
        return (x/mag, y/mag)

    def alignment(self):
        retx, rety = 0, 0
        for nboid in self.neighbors:
            x, y = self.posx, self.posy
            d = self.dist(x, y, nboid.posx, nboid.posy)
            vx, vy = self.unit(nboid.velx, nboid.vely)
            retx += vx/d
            rety += vy/d

        return retx, rety

    def separation(self):
        retx, rety = 0, 0
        for nboid in self.neighbors:
            x, y = self.posx, self.posy
            d = self.dist(x, y, nboid.posx, nboid.posy)
            dx = self.posx-nboid.posx
            dy = self.posy-nboid.posy
            dx, dy = self.unit(dx, dy)
            retx += dx/d
            rety += dy/d

        return retx, rety

    def cohesion(self):
        retx, rety = 0, 0
        for nboid in self.neighbors:
            x, y = self.posx, self.posy
            d = self.dist(x, y, nboid.posx, nboid.posy)
            retx += nboid.posx
            rety += nboid.posy

        if self.neighbors != []:
            retx -= self.posx
            rety -= self.posy
            retx, rety = self.unit(retx, rety)
            return (0.05*retx, 0.05*rety)

        return (0, 0)

    def bound(self):
        #if self.posx<10:
        #    return 3, 1
        #if self.posx>WIDTH-50:
        #    return -3, 1
        #if self.posy<10:
        #    return 1, 3
        #if self.posy>HEIGHT-40:
        #    return 1, -3
        return 0, 0


#    def bound(self):
#       retx, rety = 0, 0
#       #if self.posx>70 and self.posx<1700:
#       #    return retx, rety
#       #if self.posy>70 and self.posy<850:
#       #    return retx, rety

#       for i in xrange(5, WIDTH-50):
#           j=10
#           x, y = self.posx, self.posy
#           d = self.dist(x, y, i, j)
#           if d<= BOUND_RADIUS:
#               dx, dy = self.unit(x-i, y-j)
#               retx += dx/d
#               rety += dy/d

#           j=HEIGHT-50
#           d = self.dist(x, y, i, j)
#           if d<= BOUND_RADIUS:
#               dx, dy = self.unit(x-i, y-j)
#               retx += dx/d
#               rety += dy/d

#       for j in xrange(10, HEIGHT-50):
#           i=5
#           d = self.dist(x, y, i, j)
#           if d<= BOUND_RADIUS:
#               dx, dy = self.unit(x-i, y-j)
#               retx += dx/d
#               rety += dy/d

#           i=WIDTH-50
#           d = self.dist(x, y, i, j)
#           if d<= BOUND_RADIUS:
#               dx, dy = self.unit(x-i, y-j)
#               retx += dx/d
#               rety += dy/d

#       return 3*retx, 3*rety

