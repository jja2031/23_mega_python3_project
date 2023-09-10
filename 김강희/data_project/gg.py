import pygame, sys
import pygame.display as display
import math
import random

pygame.init()

screen = pygame.display.set_mode((1000,600), pygame.RESIZABLE)
infoObject = pygame.display.Info()
screenx, screeny = infoObject.current_w, infoObject.current_h

pygame.display.set_caption("DVD")
icon = pygame.image.load("data_project\DVD.png")
pygame.display.set_icon(icon)

surface = pygame.draw.circle()
DVDheight, DVDwidth = 46,120
print(DVDwidth,DVDheight)
DVDx = random.randint(0,screenx - DVDwidth - 50)
DVDy = random.randint(0,screeny - DVDheight - 20)
DVDchangeX = 0
DVDchangeY = 0
DVDspeed = 0.2
DVDbounce = 0
DVD_NewColor = (0,0,0)
DVD_OldColor = (255,255,255)

RightUp = False
RightDown = False
LeftUp = False
LeftDown = False
way = random.randint(0,3)
if(way == 0):
    RightUp = True
elif(way == 1):
    RightDown = True
elif(way == 2):
    LeftUp = True
elif(way == 3):
    LeftDown = True


def dvd(x,y):
    screen.blit(DVDIMG,(x,y))

def palette_swap(surf, old_c, new_c):
    global DVD_NewColor, DVD_OldColor
    img_copy = pygame.Surface(DVDIMG.get_size())
    img_copy.fill(new_c)
    surf.set_colorkey(old_c)
    img_copy.blit(surf, (0,0))
    DVD_OldColor = DVD_NewColor
    return img_copy

def bounce():
    global DVDIMG, DVD_OldColor, DVD_NewColor
    DVD_NewColor = (random.randint(0,255),random.randint(0,255),random.randint(0,254))
    DVDIMG = palette_swap(DVDIMG, DVD_OldColor,DVD_NewColor)
    

def getScreen():
    global infoObject, screenx, screeny
    infoObject = pygame.display.Info()
    screenx, screeny = infoObject.current_w, infoObject.current_h

running = True
while running:
    #background rgb
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                getScreen()
            elif event.key == pygame.K_i:
                pygame.display.set_mode((1000, 600),pygame.RESIZABLE)
                getScreen()
            elif event.key == pygame.K_ESCAPE:
                 pygame.exit()
            elif event.key == pygame.K_EQUALS or event.key == pygame.K_PLUS:
                 DVDspeed += 0.05
            elif event.key == pygame.K_MINUS:
                DVDspeed -= 0.05
            if DVDspeed <= 0:
                DVDspeed = 0 
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            getScreen()

    if DVDy >= screeny - DVDheight - 20 and RightDown:
        RightUp = True
        RightDown = False
        bounce()
    if DVDx >= screenx - DVDwidth - 50 and RightUp:
        LeftUp = True
        RightUp = False
        bounce()
    if DVDy >= screeny - DVDheight - 20 and LeftDown:
        LeftUp = True
        LeftDown = False
        bounce()
    if DVDx >= screenx - DVDwidth - 50 and RightDown:
        LeftDown = True
        RightDown = False
        bounce()
    if DVDy <= 0 and LeftUp:
        LeftDown = True        
        LeftUp = False
        bounce()
    if DVDx <= 0 and LeftDown:
        RightDown = True
        LeftDown = False
        bounce()
    if DVDx <= 0 and LeftUp:
        RightUp = True
        LeftUp = False
        bounce()
    if DVDy <= 0 and RightUp:
        RightDown = True        
        RightUp = False
        bounce()

    if RightDown:
        DVDchangeX = DVDspeed
        DVDchangeY = DVDspeed
    if RightUp:
        DVDchangeX = DVDspeed
        DVDchangeY = -DVDspeed
    if LeftDown:
        DVDchangeX = -DVDspeed
        DVDchangeY = DVDspeed
    if LeftUp:
        DVDchangeX = -DVDspeed
        DVDchangeY = -DVDspeed
        
    DVDx += DVDchangeX
    DVDy += DVDchangeY
    dvd(DVDx, DVDy)
    pygame.display.update()
