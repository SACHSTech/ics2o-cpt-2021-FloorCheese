import pygame
pygame.init()
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
box_speed_x = 0.1
box_speed_y = 0.1

bounce_height = 55
bounce_width = 10
bounce_1_x = 30
bounce_1_y =0
bounce_2_x = 520
bounce_2_y = 0
movespeed = 0.2

block_1 = pygame.Rect(bounce_width, bounce_height, bounce_1_x, bounce_1_y)
block_2 = pygame.Rect(bounce_width, bounce_height, bounce_2_x, bounce_2_y)
full_box = pygame.Rect(box_x, box_y, box_width, box_height)

player_1_score = 0
player_2_score = 0
clock = pygame.time.Clock()
font = pygame.font.SysFont('Calibri', 45, True, False)
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

  if (box_x < bounce_1_x + bounce_width and box_x + box_width > bounce_1_x and box_y < bounce_1_y + bounce_height and box_y + box_y > bounce_1_y):
    box_speed_x = box_speed_x * -1

  if (box_x < bounce_2_x + bounce_width and box_x + box_width > bounce_2_x and box_y < bounce_2_y + bounce_height and box_y + box_height > bounce_2_y):
    box_speed_x = box_speed_x * -1

  if box_y + box_height >= screen_height or box_y <= 0:
    box_speed_y = box_speed_y * -1

  box_x += box_speed_x
  box_y += box_speed_y

  if box_x + box_width >= screen_width:
    player_1_score = player_1_score + 1

  if box_x <= 0:
    player_2_score = player_2_score + 1
  
  screen.fill(BLACK)

  pygame.draw.rect(screen, (WHITE), (bounce_1_x, bounce_1_y, bounce_width, bounce_height))
  pygame.draw.rect(screen, (WHITE), (bounce_2_x, bounce_2_y, bounce_width, bounce_height))
  pygame.draw.circle(screen, WHITE, (box_x, box_y), box_width, box_height)

  if player_1_score > 0:
    points_1 = font.render("Player 1 wins!", True, WHITE)
    screen.blit(points_1, [140,10])
  elif player_2_score > 0:
    points_2 = font.render("Player 2 wins", True, WHITE)
    screen.blit(points_2, [140,10])
  else:
    pass
  pygame.display.update()

clock.tick(60)
pygame.quit()