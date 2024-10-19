
from settings import *
from obstacles import *
from player import *
import pygame
import sys
from color import *
from fruits import *
# Constants

# Main Game pl
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Geometry Slash')
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.h, self.s, self.v =200, 85, 70
        self.color = hsv_to_rgb(self.h,self.s,self.v)
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.objects = []
        self.objects.append(Obstacle())
        self.objects.append(Fruit())
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
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.player.move(self.mouse_x, self.mouse_y)
        if self.h>=360:
            self.h=0
        self.h+=.5
        
        for object in self.objects:
            object.update()
        

    def draw(self):
        self.screen.fill(hsv_to_rgb(self.h,self.s,self.v)) 
        self.player.draw(self.screen, hsv_to_rgb(self.h, self.s, self.v-20))
        for object in self.objects:
            if object.type == "Fruit":
                object.draw(self.screen, (255,255,255))
            else:
                object.draw(self.screen, (255,0,0))
        pygame.display.flip()

if __name__ == "__main__":
    Game().run()

    