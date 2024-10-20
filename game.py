
from settings import *
from obstacles import *
from player import *
import pygame
import sys
from color import *
from fruits import *
import cv2
from particles import *
import mediapipe as mp
from hands_test import *
pygame.mixer.init()  # Initialize the mixer module
slash = pygame.mixer.Sound('beep.wav')
boom = pygame.mixer.Sound('boom.wav')

# Cv stuff
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Mediapipe Hands
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
#global

# Main Game pl
class Game:
    def __init__(self):
        pygame.display.set_caption('Geometry Slash')
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 100)
        self.player = Player()
        self.h, self.s, self.v = 0, 85, 70
        self.lives = 3
        self.started = False
        self.color = hsv_to_rgb(self.h,self.s,self.v)
        self.objects = []
        self.cx,self.cy = 0,0
        self.particles = []
        self.shift_count = 0
        #game vars
        self.score = 0
    def run(self):
        while True:
            if self.started == True:
                self.handle_events()
                self.update()
                self.draw()
                self.cx, self.cy = capture_finger(cap,self.cx,self.cy,mpHands,hands,mpDraw)
                self.clock.tick(60)
            else:
                self.handle_events_home()
                self.draw_home()
                self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                cap.release()
                cv2.destroyAllWindows()
                sys.exit()

        for object in self.objects:
            if object.rect.collidepoint(self.corrected_x, self.corrected_y) and object.type=="Fruit":
                size = object.rect.width
                self.objects.remove(object)
                slash.play()
                self.score +=1
                r = random.randint(8,15)
                for i in range(r):
                    self.particles.append(Particle(self.corrected_x, self.corrected_y, size/(r/2)))
                self.v += 20
                self.shift_count = 20
                    
            elif object.rect.collidepoint(self.corrected_x, self.corrected_y) and object.type=="Obstacle":
                self.lives -= 1
                size = object.rect.width
                self.objects.remove(object)
                boom.play()
                r = random.randint(8,15)
                for i in range(r):
                    self.particles.append(Particle(self.corrected_x, self.corrected_y, size/(r/2)))
                if self.shift_count == 0:
                    self.v += 20
                    self.shift_count = 20
        
    def handle_events_home(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                self.started = True
                self.lives = 3

    def update(self):
        if self.lives == 0:
            self.started = False
            cap.release()
            cv2.destroyAllWindows()

        else:
            self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
            self.left_button, self.middle_button, self.right_button = pygame.mouse.get_pressed()
            self.corrected_x, self.corrected_y = correct(self.cx,self.cy)
            self.player.move(self.corrected_x, self.corrected_y)
            
            if self.h>=360: # colorshifting
                self.h=0
            self.h+=.5

            if self.shift_count > 0:
                self.v -=1
                self.shift_count -=1
            for particle in self.particles:
                if particle.out_of_bounds == True:
                    self.particles.remove(particle)
                else:
                    particle.update()

            for object in self.objects:
                if object.out_of_bounds == True:
                    self.objects.remove(object)
                else:
                    object.update()
            
            if len(self.objects) == 0:
                for i in range(random.randint(1,4)):
                    if random.randint(1,4)==1:
                        self.objects.append(Obstacle())
                    else:
                        self.objects.append(Fruit())
       
        

    def draw(self):
        self.screen.fill(hsv_to_rgb(self.h,self.s,self.v)) 
        self.score_text = self.font.render(("Score: " + str(self.score)),True,hsv_to_rgb(self.h,self.s,self.v-20))
        self.screen.blit(self.score_text,((WIDTH-400), 50))
        self.health_text = self.font.render(("Lives: " + str(self.lives)),True,hsv_to_rgb(self.h,self.s,self.v-20))
        self.screen.blit(self.health_text,(100, 50))
        self.player.draw(self.screen, hsv_to_rgb(self.h, self.s, self.v-20))
        for object in self.objects:
            if object.type == "Fruit":
                object.draw(self.screen, hsv_to_rgb(self.h,self.s,self.v-20))
            elif object.type == "Obstacle":
                object.draw(self.screen, hsv_to_rgb(self.h,self.s,self.v-40))
        for particle in self.particles:
            particle.draw(self.screen, hsv_to_rgb(self.h,self.s,self.v-20))
        pygame.display.flip()

    def draw_home(self):
        self.screen.fill(hsv_to_rgb(self.h,self.s,self.v)) 
        self.score_text = self.font.render("Click anywhere to start",True,hsv_to_rgb(self.h,self.s,self.v-20))
        self.screen.blit(self.score_text,(100, 50))
        pygame.display.flip()
    



if __name__ == "__main__":
    Game().run()

