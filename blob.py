import pygame
import math
import random
from settings import *

class Blob:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = BLOB_SIZE
        self.speed = BLOB_SPEED
        self.energy = 500
        self.target_food = None
        self.food_eaten = 0
        self.at_food = False

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

    def move(self, food_list):
        
        if self.at_food:
            return

        if self.food_eaten >= 1 and self.color == BLUE:
            return
        
        if self.target_food not in food_list:
            self.target_food = None

        if self.target_food is None:
            min_dist = float('inf')
            best_food = None
            chosen_side = None

            for food in food_list:
                if food.is_full():
                    continue

                dist_left = float('inf')
                dist_right = float('inf')

                seat_offset = self.size + food.size

                if not food.seat_left:
                    dx = (food.x - seat_offset) - self.x
                    dy = food.y - self.y
                    dist_left = math.hypot(dx, dy)
                
                if not food.seat_right:
                    dx = (food.x + seat_offset) - self.x
                    dy = food.y - self.y
                    dist_right = math.hypot(dx, dy)

                if dist_left < dist_right:
                    current_dist = dist_left
                    side = "left"
                else:
                    current_dist = dist_right
                    side = "right"

                if current_dist < min_dist:
                    min_dist = current_dist
                    best_food = food
                    chosen_side = side
                
            if best_food is not None:
                self.target_food = best_food
                self.my_side = chosen_side
            
            if chosen_side == "left":
                best_food.seat_left = True
            else:
                best_food.seat_right = True

        else:
            offset = self.size + self.target_food.size

            dest_y = self.target_food.y

            if self.my_side == "left":
                dest_x = self.target_food.x - offset
            else:
                dest_x = self.target_food.x + offset

            dx = dest_x - self.x
            dy = dest_y - self.y
            distance = math.hypot(dx, dy)
        
            touch_distance = self.size + (self.target_food.size * 2)
            
            if distance > self.speed:
                move_x = (dx / distance) * self.speed
                move_y = (dy / distance) * self.speed
                self.x += move_x
                self.y += move_y
            else:
                self.x = dest_x
                self.y = dest_y
                self.at_food = True