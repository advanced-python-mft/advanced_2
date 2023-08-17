import pygame

pygame.init()

dis = pygame.display.set_mode((400,300))
pygame.display.update()
RED = (255, 30, 55)
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    pygame.draw.rect(dis, RED, [260, 140, 60, 60])
    pygame.display.update()

pygame.quit()
quit()