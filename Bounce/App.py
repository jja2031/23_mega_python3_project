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

pygame.display.set_caption("Bounce")

x = screen_width/2
y = screen_height/2

(h, s, v) = (90/360.0, 1.0, 1.0)

running = True
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False

    x += xspeed
    y += yspeed

    if x < r or x > screen_width - r:
        xspeed *= -1

    if y < r or y > screen_height - r:
        yspeed *= -1

    h += 1
    
    screen.fill(color)
    pygame.draw.circle(screen, colorsys.hsv_to_rgb(h, s, v), (x, y), r)
    pygame.display.flip()


#pygame 종료s
pygame.quit()