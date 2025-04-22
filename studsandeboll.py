'''
Task

Make the circle stay inside of the window.
'''


import pygame
 
# Define some colors
green = (23,252,187)
WHITE = (255, 255, 255)
RANDOM = (13, 216, 45)
Turkoise = (13, 218, 230)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Draw circle")

# Add visual elements to the game
circle_x = 50
circle_y = 50
circle_radius = 25
circle_speed_y = 7
circle_speed_x = 7

 
# Loop until the user clicks the close button.
is_running = True
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while is_running:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
 
    # --- Game logic should go here
    circle_x += circle_speed_x
    circle_y += circle_speed_y
    if circle_y > 475:
        circle_speed_y = -7
    if circle_y < circle_radius:
        circle_speed_y = 7

    if circle_x > 700 - circle_radius:
        circle_speed_x = -7
    if circle_x < circle_radius:
        circle_speed_x = 7
    

 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(RANDOM)
 
    # --- Drawing code should go here
    pygame.draw.circle(screen, Turkoise, [circle_x, circle_y], circle_radius)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(120)
 
# Clean up when the game exits.
pygame.quit()

# jag ar klar