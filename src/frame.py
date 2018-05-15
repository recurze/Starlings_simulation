from math import pi, sqrt
from random import uniform
from constants import COHESE_RADIUS, MAX_SPEED, MIN_SPEED
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

    def unit(self, x, y):
        mag = self.dist(0, 0, x, y)
        if mag == 0:
            mag = 1
        return (x/mag, y/mag)

    def addBoid(self, x, y):
        self.n += 1
        vx, vy = uniform(-1, 1), uniform(-1, 1)
        #s = self.dist(0, 0, vx, vy)
        #if s>MAX_SPEED or s<MIN_SPEED:
        #    vx, vy = self.unit(vx, vy)
        #    vx *= MAX_SPEED
        #    vy *= MAX_SPEED
        self.boids.append(boid.Boid(x, y, vx, vy))

    def killem(self):
        self.n -= 1

    def run(self):
        energyx = 0.0
        energyy = 0.0
        momentumx = 0.0
        momentumy = 0.0

        vel = []

        for i in xrange(self.n):
            ne = self.findNeighbors(i)
            b = self.boids[i]
            b.setNeighbors(ne)
            a, c, s, bound= b.go()

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

            x, y = bound
            vx += x
            vy += y

            vel.append((vx, vy))

        for i in xrange(self.n):
            vx, vy = vel[i]
            self.boids[i].updateInfo(vx, vy)

