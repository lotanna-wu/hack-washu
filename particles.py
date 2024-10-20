import pygame
import random
from settings import *

class Particle():
    def __init__(self, x, y, size):
        self.type = "Particle"
        self.x = x
        self.y = y 
        self.out_of_bounds = False
        self.hit = False
        self.rect = pygame.Rect(self.x, self.y, size, size)
        self.speed_y = random.randint(0,10)
        self.speed_x = random.randint(-30,30)/10
        self.gravity = random.randint(11,18)/100
        self.angle = 0

    def update(self):
        self.rect.y -= self.speed_y
        self.speed_y -= self.gravity
        self.gravity += self.gravity/60
        self.rect.x -= self.speed_x
        #self.rotate_rect =
        if (self.rect.left > WIDTH or self.rect.right < 0 or self.rect.top > HEIGHT or self.rect.bottom < 0):
            self.out_of_bounds = True

    def draw(self, surface, color):
        pygame.draw.rect(surface, color, self.rect)

