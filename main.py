import pygame
pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (220, 220, 220)

size = (550, 550)
win = pygame.display.set_mode(size)

pygame.display.set_caption("Virus Fighter")

box_x = 50
box_y = 50
box_width = 10
box_height = 10
speed = 1
clock = pygame.time.Clock()

run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        run = False

  keys = pygame.key.get_pressed()

  if keys[pygame.K_LEFT] and box_x > speed:
    box_x -= speed
  if keys[pygame.K_RIGHT] and box_x < 550 - box_width - speed:
    box_x += speed
  if keys[pygame.K_UP] and box_y > speed:
    box_y -= speed
  if keys[pygame.K_DOWN] and box_y < 550 - box_height - speed:
    box_y += speed

  win.fill((255,255,255))
  pygame.draw.rect(win, (0, 0, 0), (box_x, box_y, box_width, box_height))
  pygame.display.update()

clock.tick(60)
pygame.quit()