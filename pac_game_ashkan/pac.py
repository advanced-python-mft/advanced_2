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
RED = (255, 0, 0)

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

#Making the enemy
class Enemy(pygame.sprite.Sprite):
    #The appearance of the enemy
    def __init__(self, target):
        #Enemy size and color
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        #The shape and location of the enemy
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(0, HEIGHT - self.rect.height)
        self.speed = 2 #The initial speed of the enemy
        self.target = target #enemy target

    #Enemy movement
    def update(self):
        #Find the target
        dx = self.target.rect.x - self.rect.x
        dy = self.target.rect.y - self.rect.y
        if dx < 0:
            self.rect.x -= self.speed
        elif dx > 0:
            self.rect.x += self.speed
        if dy < 0:
            self.rect.y -= self.speed
        elif dy > 0:
            self.rect.y += self.speed
        
        #Restrictions on the enemy not to leave the margins
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

#About showing points
def show_score(score):
    #Text size and font
    font = pygame.font.Font(None, 36)

    #Our text along with its score and color
    text = font.render("SCORE: " + str(score), True, YELLOW)

    #Its location
    window.blit(text, (10, 10))

#Maintain and manage all sprit objects
all_sprites = pygame.sprite.Group()

#Player representative
player = Player()

#Maintain and manage all enemy objects
enemies = pygame.sprite.Group()

#Add player to game
all_sprites.add(player)


#Add points to the game
#Number of points
for _ in range(10):
    square = Square(player)
    all_sprites.add(square)

#Add enemy to the game
#Number of enemy
for _ in range(1):
    enemy = Enemy(player)
    all_sprites.add(enemy)
    enemies.add(enemy)


#Settings section
running = True
while running:
    #To limit the number of frames per second
    clock.tick(FPS)


    for event in pygame.event.get(): #In addition to each event
        #When the received event was of QUIT type
        if event.type == pygame.QUIT:
            running = False #The loop is terminated

    all_sprites.update() #All sprites should be updated

    hits = pygame.sprite.spritecollide(player, enemies, False) #Capture enemy collisions with the player
    if hits:
        print("The game is over!")
        running = False

    window.fill((0, 0, 0)) #back ground
    all_sprites.draw(window) #In this part, we say that all the sprites in the game should be
    show_score(player.score) #Show scores in the game
    pygame.display.flip() #Show all changes

pygame.quit() #End of events
