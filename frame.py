import boids
import pygame
class frame(object):
    def __init__(self):
        self.n=10
        self.speed=2
        self.boids=[]

        self.option_separation = True
        self.option_cohesion = True
        self.option_alignment = True
        self.width = self.height = 800

    def findNeighbors(self, nboid):
        boid = self.boids[nboid]
        neighbor = []
        for i in xrange(self.n):
            if i == nboid:
                continue
            if boid.dist(self.boids[i]) <= r:
                neighbor.append(self.boids[i])
        return neighbor

    def addBoids(self):
        self.n += 1
        self.boids.append(boid(0, 0, 0))

    def killem(self):
        self.n -= 1

    def switch(s):
        if s == 'separation':
           self.option_separation = 1-self.option_separation
        if s =='cohesion':
           self.option_cohesion = 1-self.option_cohesion
        if s =='alignment':
           self.option_alignment = 1-self.option_alignment

    def run(self):
        count = 0
        while 1:
            count += (count+1)%5
            self.clear()
            theta=[]
            for i in xrange(self.n):
                if count == 0:
                    neighbors = self.findNeighbors(i)
                    self.boids[i].updateNeighbors(neighbors)
                if self.option_separation:
                    v1 = self.boids[i].separation();
                if self.option_cohesion:
                    v2 = self.boids[i].cohesion();
                if self.option_alignment:
                    theta1 = self.boids[i].alignment();
                # theta[i] = combination of v1, v2, theta1
            for i in xrange(self.n):
                self.boids[i].updateAlign(theta[i])
                self.boids[i].updatePos(self.speed,width,height)
                boid = self.boids[i]
                p = boid.position
                self.draw(p.x, p.y, boid.theta)

    def draw(x, y, angle):
        pass
if __name__ == "__main__":
    frame = frame()
    pygame.init()
    fpsClock = pygame.time.Clock()
    screen = pygame.display.set_mode([1920, 1080])
    image = pygame.image.load("boid1.jpg")
    done = 0
    x=0
    y=0
    while not done:
        x+=1
        y+=1
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                done = 1
        screen.fill((0,0,0))
        screen.blit(image, (x, y))
        pygame.display.flip()
        fpsClock.tick(60)

