import pygame
import random
from settings import *
from object import *

class Fruit(Base):
    def __init__(self):
        super().__init__(self)
        self.type = "Fruit"
