import pygame

pygame.init()
dis_x, dis_y = 400,300
dis = pygame.display.set_mode((dis_x, dis_y))
pygame.display.update()
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
    if x<0:
        x = dis_x
    pygame.draw.rect(dis, RED, [x, y, 60, 60])
    pygame.display.update()
    clock.tick(50)
pygame.quit()
quit()