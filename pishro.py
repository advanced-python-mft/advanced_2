import pygame

pygame.init()

dis = pygame.display.set_mode((400,300))
pygame.display.update()

img = pygame.image.load('pishro.jpg')
img = pygame.transform.scale(img, (100, 100))

RED = (255, 0, 0)
BLACK = (0, 0, 0)
game = True
x, y = 100, 100
x_change = 0
y_change = 0
clock = pygame.time.Clock()
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x_change = 10
                y_change = 0
            elif event.key == pygame.K_LEFT:
                x_change = -10
                y_change = 0

    dis.fill(BLACK)
    x += x_change
    y += y_change
    # pygame.draw.rect(dis, RED, [x, y, 60, 60])
    dis.blit(img, (x, y))
    pygame.display.update()
    clock.tick(50)
pygame.quit()
quit()