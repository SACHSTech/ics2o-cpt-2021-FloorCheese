import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (220, 220, 220)

size = (450, 450)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Virus Fighter")

run = True
clock = pygame.time.Clock()

box_1x = 5  #all numbers are placeholders
box_1y = 20
box_2x = 20
box_2y = 20
box_width = 10
box_height = 5

button_startgame = False
button_help = False
button_back = False
mouse_click_position = [0,0]

while run:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        run = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
      mouse_click_position = pygame.mouse.get_pos()

screen.fill(WHITE)

font = pygame.font.SysFont('Calibri', 25, True, False)
title = font.render("Virus Fighter", True, BLACK)
screen.blit(title, [100, 100])

pygame.display.update()



pygame.draw.rect(screen, GREY, [box_1x, box_1y, box_width, box_height])

pygame.draw.rect(screen, GREY, [box_2x, box_2y, box_width, box_height])


clock.tick(60)

pygame.quit()
