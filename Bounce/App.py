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

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            balls.append(ball)

    for ball in balls:
        pygame.draw.circle(screen, colorsys.hls_to_rgb(
            ball.color[0], ball.color[1], ball.color[2]), (ball.x, ball.y), ball.rad)

    pygame.display.flip()

pygame.quit()
