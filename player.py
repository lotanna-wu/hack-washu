import pygame
from settings import *


class Player:
    def __init__(self):
        self.rect = pygame.Rect(0, 300, 20, 20)
    
    def move(self, x, y):
        self.rect.center = (x,y)
  
    def draw(self, surface, color):
        pygame.draw.rect(surface, color, self.rect)