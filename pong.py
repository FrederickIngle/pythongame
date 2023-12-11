import pygame

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

