import pygame
import random
from settings import *
class Obstacle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.rect.x = random.randint(0, WIDTH - 50)  # Random x position
        self.rect.y = HEIGHT  # Start off the bottom of the screen
        self.speed = random.uniform(2, 5)  # Random speed for falling
        self.gravity = 0.5

    def update(self):
        self.rect.y += self.speed - self.gravity

    def draw(self, surface, color):
        pygame.draw.rect(surface, color, self.rect)
