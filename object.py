import pygame
import random
from settings import *

class Base(object):
    def __init__(self, type):
        self.type = type
        self.x = random.randint(0, WIDTH - 50)  
        self.y = HEIGHT 
        self.out_of_bounds = False
        self.hit = False
        self.rect = pygame.Rect(self.x, self.y, 50, 50)
        self.speed_y = random.randint(12,19)
        self.speed_x = random.randint(-10,10)/10
        self.gravity = random.randint(11,18)/100

    def update(self):
        self.rect.y -= self.speed_y
        self.speed_y -= self.gravity
        self.rect.x -= self.speed_x

        if (self.rect.left > WIDTH or self.rect.right < 0 or self.rect.top > HEIGHT or self.rect.bottom < 0):
            self.out_of_bounds = True

    def draw(self, surface, color):
        pygame.draw.rect(surface, color, self.rect)

