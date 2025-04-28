# Make it possible for the bird to move in all directions.
# Make is impossible for the bird to move outside the screen.
# Check that the box goes red when it collides with the bird.
# Make it impossible for the bird to move into the box. 
#  Hint: Move the bird back to its previous position.
# Add a second box to the game.
# Make it impossible for the bird to move into the second box.
# Which changes do you need to make if you want to add another ten boxes to the game?


import pygame

# Define colors.
RED = (255, 0, 0)
GREEN = (0, 255, 0)
SKY_BLUE = (135, 206, 235)

# Initialize all imported pygame modules.
pygame.init()

# Set the width and height of the screen [width, height].
size = (800, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Collision with Walls")

# --- Add visual elements to the game.
# Bird
bird_image = pygame.image.load("pelican.png")
bird_x = 2
bird_y = 2
bird_speed = 5

box1 = pygame.Rect(100, 100, 200, 200)
box1_color = GREEN

# Box
# Green but red when there is a collision.
box = pygame.Rect(100, 100, 200, 200)
box_color = GREEN

box2 = pygame.Rect(500, 300, 150, 150)
box2_color = GREEN

is_running = True
# Game time
clock = pygame.time.Clock()
# -------- Main Program Loop -----------
while is_running:
    # --- Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    # --- Game logic should go here
    # Move the bird with the arrow keys.
    
    # ... Write code here ....
    prev_x = bird_x
    prev_y = bird_y

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        bird_x -= bird_speed
    if keys[pygame.K_RIGHT]:
        bird_x += bird_speed
    if keys[pygame.K_UP]:
        bird_y -= bird_speed
    if keys[pygame.K_DOWN]:
        bird_y += bird_speed

    if bird_x < 0:
        bird_x = 0
    if bird_y < 0:
        bird_y = 0
    if bird_x > size[0] - bird_image.get_width():
        bird_x = size[0] - bird_image.get_width()
    if bird_y > size[1] - bird_image.get_height():
        bird_y = size[1] - bird_image.get_height()

    bird_rect = pygame.Rect(bird_x, bird_y, bird_image.get_width(), bird_image.get_height())


    # Check for collision between the bird and the box.
    if box.colliderect(bird_image.get_rect(topleft=(bird_x, bird_y))):
        box_color = RED
    else:
        box_color = GREEN

    # --- Screen-clearing code goes here
    screen.fill(SKY_BLUE)
    # --- Drawing code should go here
    screen.blit(bird_image, (bird_x, bird_y))
    pygame.draw.rect(screen, box_color, box)
    pygame.display.update()  # or pygame.display.flip()
    # --- Increase game time
    clock.tick(60)  # 60 frames per second

# Clean up when the game exits.
pygame.quit()