import random

class Ball:
    def __init__(self, x, y, xspeed, yspeed, rad, color):
        self.x = x
        self.y = y
        self.xspeed = xspeed
        self.yspeed = yspeed

        self.xdir = random.randrange(0, 10)
        if self.xdir % 2 == 0:
            self.xdir = -1
        else:
            self.xdir = 1

        self.ydir = random.randrange(0, 10)
        if self.ydir % 2 == 0:
            self.ydir = -1
        else:
            self.ydir = 1

        self.rad = rad
        self.color = color

    def update(self):
        self.color[0] += 0.00005
        self.x += (self.xspeed * self.xdir)
        self.y += (self.yspeed * self.ydir)

    def getColor(self):
        return (self.color[0], self.color[1], self.color[2])

    def checkCollision(self, width, height):
        if self.x < self.rad:
            self.x = self.rad
            self.xdir *= -1
            self.lifeDown()
        
        if self.x > width - self.rad:
            self.x = width - self.rad
            self.xdir *= -1
            self.lifeDown()
        
        if self.y < self.rad:
            self.y = self.rad
            self.ydir *= -1
            self.lifeDown()
        
        if self.y > height - self.rad:
            self.y = height - self.rad
            self.ydir *= -1
            self.lifeDown()

        
    def lifeDown(self):
        self.color[1] -= 12
        if self.color[1] <= 0:
            self.color[1] = 0

    def isDead(self):
        if self.color[1] <= 0:
            return True
        return False