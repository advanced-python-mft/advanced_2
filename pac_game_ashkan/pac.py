'''
CB: ASHKAN
2023/8/23 3:01 PM
'''

#Add some libraries
import pygame
import random

#Definition of width and height
WIDTH = 1500
HEIGHT = 1000
FPS = 60

#The color of the characters
YELLOW = (255, 255, 0)
PURPLE = (106, 13, 173)

#Basic work before making the main game
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PAC")
clock = pygame.time.Clock()

# Definition of game options

#Inherited from pygame.sprite.Sprite class
# Player class
class Player(pygame.sprite.Sprite):
    #Character creation
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #Character color and size
        self.image = pygame.Surface((50, 50))
        self.image.fill(YELLOW)
        #Body part and location
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speed = 5 #Initial speed
        self.score = 0 #Initial score
    
    #Character movement
    def update(self):
        #Capturing any movement from the user
        keys = pygame.key.get_pressed()

        #Betting on movement
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        #Betting on the character that hits the wall of rage but does not pass
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

#Inherited from pygame.sprite.Sprite class
#Points class
class Square(pygame.sprite.Sprite):
    #Appearance of points
    def __init__(self, player):
        #Score color and size
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(PURPLE)
        #Moving points randomly
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(0, HEIGHT - self.rect.height)
        self.player = player

    #Movement and points
    def update(self):
        if pygame.sprite.collide_rect(self, self.player):
            #Collect points
            self.player.score += 1 
            #Transfer points
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.rect.y = random.randint(0, HEIGHT - self.rect.height)