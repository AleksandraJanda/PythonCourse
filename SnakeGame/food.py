from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.penup()
        self.speed(10)
        self.color("blue")
        self.move()

    def move(self):
        self.goto(random.randint(-250, 250), random.randint(-250, 250))