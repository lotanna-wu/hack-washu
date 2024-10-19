import pygame

class Obstacle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)

    def update(self):
        pass

    def draw(self, surface, color):
        pass
