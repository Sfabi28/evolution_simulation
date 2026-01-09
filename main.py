import pygame
import sys
import random
import matplotlib.pyplot as plt
from stats import show_graph
from settings import *
from blob import Blob
from food import Food 
import math

FOOD_PADDING = 50
MIN_FOOD_DISTANCE = 40

def spawn_food(amount):
    new_food_list = []
    attempts = 0
    
    while len(new_food_list) < amount and attempts < 10000:
        attempts += 1
        
        x = random.randint(FOOD_PADDING, WIDTH - FOOD_PADDING)
        y = random.randint(FOOD_PADDING, HEIGHT - FOOD_PADDING)
        
        too_close = False
        for f in new_food_list:
            dx = x - f.x
            dy = y - f.y
            dist = math.hypot(dx, dy)
            
            if dist < MIN_FOOD_DISTANCE:
                too_close = True
                break
        if not too_close:
            new_food_list.append(Food(x, y))
            
    return new_food_list


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("evolution simulation")
    clock = pygame.time.Clock()

    red_blobs = []
    blue_blobs = []
    food = []

    for _ in range(10):
        red_blobs.append(Blob(random.randint(0, WIDTH), random.randint(0, HEIGHT), color=RED))

    for _ in range(10):
        blue_blobs.append(Blob(random.randint(0, WIDTH), random.randint(0, HEIGHT), color=BLUE))

    day = 0
    game_over = False
    step = "morning"

    stats_red = [len(red_blobs)]
    stats_blue = [len(blue_blobs)]
    days_list = [0]

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                show_graph(days_list, stats_red, stats_blue)
                sys.exit()

        if step == "morning":
            day += 1
            print(f"Day {day} starting")
            food.clear()
            food = spawn_food(FOOD_AMOUNT)

            step = "lunch"
        
        if step == "lunch":
            
            all_moving_blobs = red_blobs + blue_blobs

            random.shuffle(all_moving_blobs)
            
            for b in all_moving_blobs: 
                b.move(food)

            all_arrived = True

            for b in all_moving_blobs:
                if not b.at_food and b.target_food is not None:
                    all_arrived = False
                    break

            if all_arrived:
                step = "dinner"

        if step == "dinner":

            food_occupants = {}
            all_blobs = red_blobs + blue_blobs    

            for b in all_blobs:
                if b.at_food and b.target_food:
                    if b.target_food not in food_occupants:
                        food_occupants[b.target_food] = []
                    food_occupants[b.target_food].append(b)
                
            for f, blobs_at_table in food_occupants.items():

                if len(blobs_at_table) == 1:
                    blobs_at_table[0].food_eaten = 1

                elif len(blobs_at_table) == 2:
                    b1 = blobs_at_table[0]
                    b2 = blobs_at_table[1]
                    
                    if b1.color == BLUE and b2.color == BLUE:
                        b1.food_eaten = 0.5
                        b2.food_eaten = 0.5
                    
                    elif b1.color == RED and b2.color == RED:
                        if random.random() < 0.5:
                            b1.food_eaten = 0.5
                            b2.food_eaten = 0
                        else:
                            b1.food_eaten = 0
                            b2.food_eaten = 0
                    
                    else:
                        winner = b1 if b1.color == RED else b2
                        loser = b1 if b1.color == BLUE else b2
                        
                        winner.food_eaten = 1
                        loser.food_eaten = 0
            
            step = "night"

        if step == "night":
            next_red = []
            next_blue = []

            def process_life(current_list, next_list):
                for b in current_list:
                    home_x = random.randint(0, WIDTH)
                    home_y = random.randint(0, HEIGHT)
                    
                    if b.food_eaten == 1:
                        next_list.append(Blob(home_x, home_y, b.color))
                        next_list.append(Blob(home_x, home_y, b.color))
                    
                    elif b.food_eaten == 0.5:
                        next_list.append(Blob(home_x, home_y, b.color))

            process_life(red_blobs, next_red)
            process_life(blue_blobs, next_blue)

            red_blobs = next_red
            blue_blobs = next_blue

            print(f"Fine Giorno. Rossi: {len(red_blobs)} - Blu: {len(blue_blobs)}")

            stats_red.append(len(red_blobs))
            stats_blue.append(len(blue_blobs))
            days_list.append(day)

            pygame.time.wait(100)

            if len(red_blobs) == 0 and len(blue_blobs) == 0:
                game_over = True
            else:
                step = "morning"


        screen.fill(BLACK)
        
        for f in food:
            f.draw(screen)
        for b in red_blobs:
            b.draw(screen)
        for b in blue_blobs:
            b.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

    if len(days_list) > 1:
        show_graph(days_list, stats_red, stats_blue)


if __name__ == "__main__":
    main()



        

        

