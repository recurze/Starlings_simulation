from math import sqrt
from constants import WIDTH, HEIGHT, SPEED

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
        self.posx = (self.posx + WIDTH) % WIDTH
        self.posy = (self.posy + WIDTH) % WIDTH

    def updateInfo(self, vx, vy):
        vx, vy = self.unit(vx, vy)
        self.velx = vx*SPEED
        self.vely = vy*SPEED

        self.posx += self.velx
        self.posy += self.vely
        self.wrapAround()

    def setNeighbors(self, n):
        self.neighbors = n

    def go(self):
        a = self.alignment()
        c = self.cohesion()
        s = self.separation()

        return (a, c, s)

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

