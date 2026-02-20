from turtle import Turtle
import time
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.is_collision = False
        self.paddle = ''
        self.shape('circle')
        self.penup()
        self.color('white')
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.random_coordinates = [0.9, 1, 1.1]

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= - random.choice(self.random_coordinates)

    def bounce_x(self):
        self.x_move *= - random.choice(self.random_coordinates)
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
