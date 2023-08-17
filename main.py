import pygame

pygame.init()

dis = pygame.display.set_mode((400,300))
pygame.display.update()
RED = (255, 0, 0)
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    pygame.draw.rect(dis, RED, [100, 100, 60, 60])
    pygame.display.update()

pygame.quit()
quit()
