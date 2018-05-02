from math import pi, sqrt
from random import uniform
from constants import COHESE_RADIUS
import boid

class Frame(object):
    def __init__(self):
        self.n=0
        self.boids=[]

        self.option_s = True
        self.option_c = True
        self.option_a = True

    def dist(self,x1, y1, x2, y2):
        return sqrt((x1-x2)**2+(y1-y2)**2)

    def findNeighbors(self, n):
        b = self.boids[n]
        neighbor = []
        for i in xrange(self.n):
            ib = self.boids[i]
            if i == n:
                continue
            d = self.dist(b.posx, b.posy, ib.posx, ib.posy)
            if d <= COHESE_RADIUS:
                neighbor.append(ib)
        return neighbor

    def addBoid(self, x, y):
        self.n += 1
        vx, vy = uniform(-1, 1), uniform(-1, 1)
        self.boids.append(boid.Boid(x, y, vx, vy))

    def killem(self):
        self.n -= 1

    def run(self):
        vel = []

        for i in xrange(self.n):
            ne = self.findNeighbors(i)
            b = self.boids[i]
            b.setNeighbors(ne)
            a, c, s = b.go()

            vx, vy = b.velx, b.vely
            if self.option_s:
                x, y = s
                vx += x
                vy += y
            if self.option_c:
                x, y = c
                vx += x
                vy += y
            if self.option_a:
                x, y = a
                vx += x
                vy += y

            vel.append((vx, vy))

        for i in xrange(self.n):
            vx, vy = vel[i]
            self.boids[i].updateInfo(vx, vy)
