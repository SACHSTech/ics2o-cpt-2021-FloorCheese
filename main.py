""" 
A basic pygame template
"""
 
import pygame
 
# Define some colors
BLACK = (   0,   0,   0)
WHITE = ( 255, 255, 255)
GREEN = (   0, 255,   0)
RED = ( 255,   0,   0)
 
pygame.init()
  
# Set the width and height of the screen [width, height]
size = (701, 501)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
#Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
#box properties
box_x = 50
box_y = 50
box_width = 3
box_height = 3

# -------- Main Program Loop -----------
def main():
  run = True
  while run:
    for event in pygame.event.get(): #Check for user actions
        if event.type == pygame.QUIT: 
            run = False #End loop

  
    # --- Game logic should go here
 
    # --- Drawing code should go here
     
    # First, clear the screen to white or whatever background colour. 
    # Don't put other drawing commands above this, or they will be erased with this command.
    screen.fill(WHITE)
    font = pygame.font.Font('freesansbold.ttf',36)

title_x = 351
title_y = 400
def title_screen(x, y):
  title = font.render("Stop The Virus",True, (WHITE)) #working title
  screen.blit(title, (title_x, title_y))

pygame.draw.rect(screen, RED, [box_x, box_y, box_width, box_height])
    # --- Go ahead and update the screen with what we've drawn.
pygame.display.flip()
 
    # --- Limit to 60 frames per second
clock.tick(60)
     
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()