import pygame
import random
from settings import *

class Fruit:
    def __init__(self):
        self.x = random.randint(0, WIDTH - 50)  
        self.y = HEIGHT 
        self.type = "Fruit"
        self.rect = pygame.Rect(self.x, self.y, 50, 50)
        

        self.speed_y = random.randint(7,9)
        self.speed_x = random.randint(-10,10)/10

        self.gravity = 0.05

    def update(self):
        self.rect.y -= self.speed_y
        self.speed_y -= self.gravity
        self.rect.x -= self.speed_x
    

    def draw(self, surface, color):
        pygame.draw.rect(surface, color, self.rect)

