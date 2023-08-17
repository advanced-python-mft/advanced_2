import pygame

pygame.init()

dis = pygame.display.set_mode((400,300))
pygame.display.update()
RED = (25, 155, 20)
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    pygame.draw.rect(dis, RED, [255, 100, 100, 100])
    pygame.display.update()

pygame.quit()
quit()