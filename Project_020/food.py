from screen_dimensions import *
from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.food_setup()
        self.move_to_new_position()

    def food_setup(self):
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color("yellow")
        self.speed("fastest")

    def move_to_new_position(self):
        rand_x = random.randrange(-(SCREEN_WIDTH // 2 - STEP), (SCREEN_WIDTH // 2 - STEP), STEP)
        rand_y = random.randrange(-(SCREEN_HEIGHT // 2 - STEP), (SCREEN_HEIGHT // 2 - STEP), STEP)
        # print(f"Food Location: ({rand_x}, {rand_y})")
        self.goto(rand_x, rand_y)
