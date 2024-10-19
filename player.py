import pygame
from settings import *


class Player:
    def __init__(self):
        self.rect = pygame.Rect(0, 300, 20, 20)
    
    def move(self, x, y):
        self.rect.x += x
        self.rect.y +=y
    def update(self):
        pass

    def draw(self, surface, color):
        pygame.draw.rect(surface, color, self.rect)