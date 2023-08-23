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
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #Character creation
        self.image = pygame.Surface((50, 50))
        self.image.fill(YELLOW)
        #Body part, size and location
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speed = 5 #Initial speed
        self.score = 0 #Initial score
    def update(self):
        pass