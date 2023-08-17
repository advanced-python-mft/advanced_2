import pygame

pygame.init()

dis = pygame.display.set_mode((400,300))
pygame.display.update()
RED = (255, 0, 0)
game = True
x = 100
y = 100
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    x += 1
    y += 1
    pygame.draw.rect(dis, RED, [x, y, 60, 60])
    pygame.display.update()

pygame.quit()
quit()
