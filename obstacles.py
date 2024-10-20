import pygame
import random
from settings import *
from object import *

class Obstacle(Base):
    def __init__(self):
        super().__init__(self)
        self.type = "Obstacle"
