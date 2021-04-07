import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (220, 220, 220)

size = (550, 550)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Virus Fighter")

run = True
clock = pygame.time.Clock()

box_startgame_x = 110 
box_startgame_y = 140
box_help_x = 110
box_help_y = 230
box_powers_x = 110
box_powers_y = 320
box_back_x = 100
box_back_y = 100
box_width = 350
box_height = 60

button_startgame = False
button_help = False
button_back = False
button_powers = False
title_screen = True
begin_game = False
mouse_click_position = [0,0]

font = pygame.font.SysFont('Calibri', 45, True, False)
while run:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        run = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
      mouse_click_position = pygame.mouse.get_pos()
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_A:
        x_change = -5
      if event.key == pygame.K_D:
        x_change = 5
      if event.key == pygame.K_W:
        y_change = 5
      if event.key == pygame.K_S:
        y_change = -5
    elif event.type == pygame.KEYUP:
      if event.key == pygame.K_W or event.key == pygame.K_A or event.key == pygame.K_S or event.key == pygame.K_D:
        x_change = 0
  screen.fill(WHITE)

  if (box_startgame_x <= mouse_click_position[0] and mouse_click_position[0] <= box_startgame_x + box_width) and (box_startgame_y <= mouse_click_position[1] and mouse_click_position[1] <= box_startgame_y + box_height):
      button_startgame = True
      title_screen = False
  else:
      button_startgame = False

  if (box_help_x <= mouse_click_position[0] and mouse_click_position[0] <= box_help_x + box_width) and (box_help_y <= mouse_click_position[1] and mouse_click_position[1] <= box_help_y + box_height):
      button_help = True
      title_screen = False
  else:
      button_help = False

  if (box_powers_x <= mouse_click_position[0] and mouse_click_position[0] <= box_powers_x + box_width) and (box_powers_y <= mouse_click_position[1] and mouse_click_position[1] <= box_powers_y + box_height):
      button_powers = True
      title_screen = False
  else:
      button_powers = False

  if button_startgame and not title_screen:
    screen.fill(WHITE)
    begin_game = True
    while begin_game:
    
  elif button_help and not title_screen:
    screen.fill(WHITE)
    control_text_w = font.render("Press 'W' to move up", True, BLACK)
    screen.blit(control_text_w, [135, 60])
    control_text_a = font.render("Press 'a' to move left", True, BLACK)
    screen.blit(control_text_a, [135, 60])
    control_text_s = font.render("Press 's' to move down", True, BLACK)
    screen.blit(control_text_s, [135, 60])
    control_text_d = font.render("Press 'd' to move right", True, BLACK)
    screen.blit(control_text_d, [135, 60])
    
  elif button_powers and not title_screen:
    screen.fill(WHITE)
    
  
  else:
    text_title = font.render("Virus Fighter", True, BLACK)
  screen.blit(text_title, [135, 60])
  pygame.draw.rect(screen, GREY, [box_startgame_x, box_startgame_y, box_width, box_height])
  pygame.draw.rect(screen, GREY, [box_help_x, box_help_y, box_width, box_height])
  pygame.draw.rect(screen, GREY, [box_powers_x, box_powers_y, box_width, box_height])

  text_startgame = font.render("Start Game", True, BLACK)
  screen.blit(text_startgame, [160, 145])

  text_help = font.render("Controls", True, BLACK)
  screen.blit(text_help, [190, 235])

  text_powers  = font.render("Powers", True, BLACK)
  screen.blit(text_powers, [200, 325])
  
  pygame.display.update()

clock.tick(60)
pygame.quit()
