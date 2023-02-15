import time
import pygame
import random

pygame.init()
screen_width=800
screen_height=600
screen=pygame.display.set_mode((screen_width,screen_height))
clock =pygame.time.Clock()
cord_x=40
cord_y=40
SPEED=10
facing_left=True
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    screen.fill((255, 255, 255))
    if facing_left and cord_x<=760:
        cord_x+=SPEED
    elif facing_left and cord_x>760:
        facing_left=False
        cord_x=759
    elif not facing_left and cord_x >=40:
        cord_x-=SPEED
    elif not facing_left and cord_x<40:
        facing_left=True
    pygame.draw.rect(screen,(0,0,0),(cord_x,cord_y,20,20))
    pygame.display.update()
    clock.tick(60)

pygame.display.update()
pygame.quit()