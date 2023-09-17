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
        self.color[1] -= 0.001
        if self.color[1] <= 0:
            self.color[1] = 0
        self.x += self.xspeed
        self.y += self.yspeed

    def getColor(self):
        return (self.color[0], self.color[1], self.color[2])
