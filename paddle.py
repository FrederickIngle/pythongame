import pygame
BLACK = (0,0,0)

class Paddle(pygame.sprite.Sprite):

    def __init__(self,color,width,height):
        #call the parent class (Sprite) constructor
        super().__init__()

        #Pass the color of the paddle, its width and height
        #awt the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        #draw the paddle
        pygame.draw.rect(self.image,color,[0,0, width, height])

        #Fetch the rectangle object that has dimenstions of the image
        self.rect = self.image.get_rect()