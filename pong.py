import pygame
from paddle import Paddle

#Setup
pygame.init()
clock = pygame.time.Clock()

# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)

#main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('My Game')

    #create paddle objects
paddleA = Paddle(WHITE,10,100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE,10,100)
paddleB.rect.x = 670
paddleB.rect.y = 200

#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()
# Add the paddles to the list of sprites
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)


running = True
while running:
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #updating the window
    pygame.display.flip()
    clock.tick(60)

   
    




pygame.quit

