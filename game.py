
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
ambience = pygame.mixer.music.load('lofi.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)
# Cv stuff


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
        self.started = False
        self.color = hsv_to_rgb(self.h,self.s,self.v)
        self.objects = []
        self.cx,self.cy = 0,0
        self.particles = []
        self.shift_count = 0

        self.lives = 3
        self.score = 0
        self.highscore = 0

        self.score_text = self.font.render(("Score: " + str(self.score)),True,hsv_to_rgb(self.h,self.s,self.v-20))
        self.highscore_text = self.font.render(("High: " + str(max(self.score, self.highscore))),True,hsv_to_rgb(self.h,self.s,self.v-20))
        self.health_text = self.font.render(("Lives: " + str(self.lives)),True,hsv_to_rgb(self.h,self.s,self.v-20))

    def run(self):
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            print("Error: Could not open video.")
            exit()
        while True:
            if self.started == True:
                self.cx, self.cy = capture_finger(self.cap,self.cx,self.cy,mpHands,hands,mpDraw)
                self.handle_events()
                self.update()
                self.draw()
                self.clock.tick(60)
            else:
                self.cx, self.cy = capture_finger(self.cap,self.cx,self.cy,mpHands,hands,mpDraw)
                self.handle_events_home()
                self.draw_home()
                self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #end the program if the user wants to quit
                pygame.quit()
                self.cap.release()
                cv2.destroyAllWindows()
                sys.exit()
            
        for object in self.objects: #iterate through each object, remove the ones that the player hits and add explosion effect
            if object.rect.collidepoint(self.corrected_x, self.corrected_y) and object.type=="Fruit":
                size = object.rect.width
                self.objects.remove(object)
                slash.play()
                self.score +=1
                r = random.randint(8,15)
                for i in range(r):
                    self.particles.append(Particle(self.corrected_x, self.corrected_y, size/(r/2)))
                if self.shift_count == 0:
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
        
    def handle_events_home(self): #the home page events, see if player starts game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                self.started = True
                self.lives = 3
                self.score = 0

    def update(self): #updating game logic
        if self.lives == 0:
            self.started = False
            self.highscore = max(self.score, self.highscore)
            

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
                for i in range(random.randint(2,5)):
                    if random.randint(1,4)==1:
                        self.objects.append(Obstacle())
                    else:
                        self.objects.append(Fruit())
       
        

    def draw(self): #redrawing game stuff
        score_width = self.score_text.get_width()
        highscore_width = self.highscore_text.get_width()
        health_width = self.health_text.get_width()
        total_width = score_width + highscore_width + health_width + 40

        start_x = (WIDTH - total_width) // 2
        self.screen.fill(hsv_to_rgb(self.h,self.s,self.v)) 
        self.score_text = self.font.render(("Score: " + str(self.score)),True,hsv_to_rgb(self.h,self.s,self.v-20))
        self.highscore_text = self.font.render(("High: " + str(max(self.score, self.highscore))),True,hsv_to_rgb(self.h,self.s,self.v-20))
        self.health_text = self.font.render(("Lives: " + str(self.lives)),True,hsv_to_rgb(self.h,self.s,self.v-20))
        self.screen.blit(self.score_text,(start_x, 50))
        self.screen.blit(self.highscore_text,(start_x + score_width + 20, 50))
        self.screen.blit(self.health_text,(start_x + score_width + highscore_width + 40, 50))
        self.player.draw(self.screen, hsv_to_rgb(self.h, self.s, self.v-20))

        for object in self.objects:
            if object.type == "Fruit":
                object.draw(self.screen, hsv_to_rgb(self.h,self.s,self.v-20))
            elif object.type == "Obstacle":
                object.draw(self.screen, hsv_to_rgb(self.h,self.s,self.v-40))
        for particle in self.particles:
            particle.draw(self.screen, hsv_to_rgb(self.h,self.s,self.v-20))
        pygame.display.flip()

    def draw_home(self): #redrawing home stuff
        self.screen.fill(hsv_to_rgb(self.h,self.s,self.v)) 
        self.score_text = self.font.render("Click anywhere to start",True,hsv_to_rgb(self.h,self.s,self.v-20))
        self.screen.blit(self.score_text,(100, 50))

        self.score_text = self.font.render("Avoid Darker Objects",True,hsv_to_rgb(self.h,self.s,self.v-20))
        self.screen.blit(self.score_text,(100, 150))

        self.score_text = self.font.render("High: "+str(self.highscore),True,hsv_to_rgb(self.h,self.s,self.v-20))
        self.screen.blit(self.score_text,(100, 300))
        pygame.display.flip()
    



if __name__ == "__main__":
    Game().run()#runs the game

