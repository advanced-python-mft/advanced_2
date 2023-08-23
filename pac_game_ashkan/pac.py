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

#Basic work before making the main game
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PAC")
clock = pygame.time.Clock()

# Definition of game options

#Inherited from pygame.sprite.Sprite class
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
        