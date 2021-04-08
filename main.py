import pygame
import random as ra

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen_width = 550
screen_height = 300
size = [screen_width, screen_height]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Pong")

box_x = 250
box_y = 140
box_width = 10
box_height = 10
box_speed_x = 0.05
box_speed_y = 0.05

bounce_height = 55
bounce_width = 10
bounce_1_x = 30
bounce_1_y =0
bounce_2_x = 520
bounce_2_y = 0
movespeed = 0.2

clock = pygame.time.Clock()

run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        run = False

  keys = pygame.key.get_pressed()

  if keys[pygame.K_w] and bounce_1_y > movespeed:
    bounce_1_y -= movespeed
  if keys[pygame.K_s] and bounce_1_y < screen_height - bounce_height - movespeed:
    bounce_1_y += movespeed
  if keys[pygame.K_UP] and bounce_2_y > movespeed:
    bounce_2_y -= movespeed
  if keys[pygame.K_DOWN] and bounce_2_y < screen_height - bounce_height - movespeed:
    bounce_2_y += movespeed

#add code for hitbox on bouncies
  if box_x + box_width 
    box_speed_x = box_speed_x + ra.uniform(0.01, 0.05)
    box_speed_x = box_speed_x * -1
 
  if box_y + box_height >= screen_height or box_y <= 0:
    box_speed_y = box_speed_y + ra.uniform(0.01, 0.05)
    box_speed_y = box_speed_y * -1

  box_x += box_speed_x
  box_y += box_speed_y

  screen.fill(WHITE)

  pygame.draw.rect(screen, (0, 0, 0), (bounce_1_x, bounce_1_y, bounce_width, bounce_height))
  pygame.draw.rect(screen, (0, 0, 0), (bounce_2_x, bounce_2_y, bounce_width, bounce_height))

  pygame.draw.rect(screen, BLACK, [box_x, box_y, box_width, box_height])

  pygame.display.update()

clock.tick(60)
pygame.quit()