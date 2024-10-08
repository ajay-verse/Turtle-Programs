from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("green")
        self.speed("fastest")
        x_axis = random.randint(-280, 280)
        y_axis = random.randint(-280, 280)
        self.goto(x_axis, y_axis)

    def refresh(self):
        x_axis = random.randint(-280, 280)
        y_axis = random.randint(-280, 280)
        self.goto(x_axis, y_axis)
