import pygame
import random
from settings import *
import math

class Base(object):
    def __init__(self, type):
        self.type = type
        self.x = random.randint(200, WIDTH-200)  
        self.y = HEIGHT 
        self.out_of_bounds = False
        self.hit = False
        self.size = random.randint(60,100)
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        self.speed_y = random.randint(12,19)
        self.speed_x = random.randint(-30,30)/10
        self.gravity = random.randint(11,18)/100
        self.shape = random.randint(1,4)
    def update(self):
        self.rect.y -= self.speed_y
        self.speed_y -= self.gravity
        self.gravity += self.gravity/60
        self.rect.x -= self.speed_x
        #self.rotate_rect =
        if (self.rect.left > WIDTH or self.rect.right < 0 or self.rect.top > HEIGHT):
            self.out_of_bounds = True

    def draw(self, surface, color):
        if self.shape == 1:
           pygame.draw.rect(surface, color, self.rect)
        elif self.shape==2:
            pygame.draw.circle(surface, color,self.rect.center, self.size/2)
        elif self.shape == 3:
            points = [
                (self.rect.centerx, self.rect.top), 
                (self.rect.left, self.rect.bottom),  
                (self.rect.right, self.rect.bottom)  
            ]
            pygame.draw.polygon(surface, color, points)
        elif self.shape == 4:
            radius = self.size / 2
            points = []
            for i in range(6):
                angle = i * (360 / 6)
                x = self.rect.centerx + radius * math.cos(math.radians(angle))
                y = self.rect.centery + radius * math.sin(math.radians(angle))
                points.append((x, y))
            pygame.draw.polygon(surface, color, points)
        

