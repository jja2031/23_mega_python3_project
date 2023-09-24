import random
import pygame
import colorsys
from modules.Ball import Ball

pygame.init()

# screen setting
screen_width = 320
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# logo setting
icon_img = pygame.image.load('Bounce\pngwingcom.png')
pygame.display.set_icon(icon_img)
pygame.display.set_caption("Bounce")

# Ball
balls = []
rad = 20


running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_pos = (pygame.mouse.get_pos()[0])
            y_pos = (pygame.mouse.get_pos()[1])
            x = x_pos
            y = y_pos
            newBall = Ball(x,y,0,0,rad,'#fff')
            balls.append(newBall)

    for ball in balls:
        pygame.draw.circle(screen, (255,0,0), (x,y), rad)

    pygame.display.flip()

pygame.quit()
