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

#Basic work before making the main game
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PAC")
clock = pygame.time.Clock()

# Definition of game options
class Player():
    def __init__(self):
        pass
    def update(self):
        pass