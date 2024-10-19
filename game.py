
from settings import *
from obstacles import *
from player import *
import pygame
import sys

# Constants
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Main Game pl
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Geometry Dash')
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.color = (255,255,255)

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            keys = pygame.key.get_pressed()

    def update(self):
        self.player.update()
        

    def draw(self):
        self.screen.fill(self.color)  # Fill the screen with white
        self.player.draw(self.screen, GREEN)
        pygame.display.flip()

if __name__ == "__main__":
    Game().run()

    