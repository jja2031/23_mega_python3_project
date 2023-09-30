import pygame
import random
import colorsys
from modules.Ball import Ball

pygame.init()

screen_width = 320
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
color = (0, 0, 0)
img = pygame.image.load('Bounce\pngwingcom.png')
pygame.display.set_icon(img)

pygame.display.set_caption("Bounce")


balls = []

running = True
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_pos = int(pygame.mouse.get_pos()[0])
            y_pos = int(pygame.mouse.get_pos()[1])
            balls.append(Ball(x_pos, y_pos, random.uniform(0.0, 0.1), random.uniform(0.05, 0.1), random.randint(15,25), [0.0, 127.5, -1.007905138339921]))

    
    screen.fill(color)

    for ball in balls:
        ball.update()
        ball.checkCollision(screen_width, screen_height)
        (h, l, s) = ball.getColor()
        pygame.draw.circle(screen, colorsys.hls_to_rgb(h, l, s), (ball.x, ball.y), ball.rad)

    for ball in balls:
        if ball.isDead() == True:
            balls.remove(ball)

    pygame.display.flip()

pygame.quit()