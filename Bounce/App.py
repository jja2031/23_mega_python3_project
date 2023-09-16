import pygame
import colorsys

pygame.init()

screen_width = 320
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
color = (80, 188, 223)
r = 20
xspeed = 0.05
yspeed = 0.05
img = pygame.image.load('Bounce\pngwingcom.png')
pygame.display.set_icon(img)

pygame.display.set_caption("Bounce")

x = screen_width/2
y = screen_height/2

(h, l, s) = (0.0, 127.5, -1.007905138339921)

running = True
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_pos = int(pygame.mouse.get_pos()[0])
            y_pos = int(pygame.mouse.get_pos()[1]) 
            x = x_pos
            y = y_pos

    x += xspeed
    y += yspeed
    
    h += 0.00005

    if x < r or x > screen_width - r:
        xspeed *= -1

    if y < r or y > screen_height - r:
        yspeed *= -1

    h += 1
    
    screen.fill(color)
    pygame.draw.circle(screen, colorsys.hls_to_rgb(h, l, s), (x, y), r)
    pygame.display.flip()

pygame.quit()