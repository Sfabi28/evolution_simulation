import pygame
from settings import *

class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = FOOD_SIZE
        self.color = GREEN

        self.seat_left = False
        self.seat_right = False

    def is_full(self):
        return self.seat_left and self.seat_right

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)