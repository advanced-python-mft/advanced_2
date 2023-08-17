import pygame

# Initialize pygame
pygame.init()

# Set the window size
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Load the pacman image
pacman_image = pygame.image.load("pacman.png")

# Load the ghosts images
ghost_images = ['as.jpg']
for i in range(4):
    ghost_images.append(pygame.image.load("ghost_" + str(i) + ".png"))

# Create the pacman sprite
pacman = pygame.sprite.Sprite()
pacman.image = pacman_image
pacman.rect = pacman_image.get_rect()
pacman.rect.centerx = screen_width / 2
pacman.rect.centery = screen_height / 2

# Create the ghost sprites
ghosts = []
for i in range(4):
    ghost = pygame.sprite.Sprite()
    ghost.image = ghost_images[i]
    ghost.rect.x = 20 + i * 100
    ghost.rect.y = 20

# Create the score
score = 0

# Create the game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Move the pacman sprite
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pacman.rect.x -= 10
            elif event.key == pygame.K_RIGHT:
                pacman.rect.x += 10
            elif event.key == pygame.K_UP:
                pacman.rect.y -= 10
            elif event.key == pygame.K_DOWN:
                pacman.rect.y += 10

    # Check for collisions
    for ghost in ghosts:
        if pacman.rect.colliderect(ghost.rect):
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the sprites
    screen.blit(pacman.image, pacman.rect)
    for ghost in ghosts:
        screen.blit(ghost.image, ghost.rect)

    # Draw the score
    pygame.draw.rect(screen, (255, 0, 0), (10, 10, 100, 20))
    pygame.draw.text(screen, str(score), (20, 20), pygame.font.SysFont("Arial", 20))

    # Update the display
    pygame.display.flip()

# Close pygame
pygame.quit()