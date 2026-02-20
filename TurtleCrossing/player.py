from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.set_starting_position()

    def set_starting_position(self):
        self.goto(0,-280)
        self.setheading(90)

    def up(self):
        self.forward(20)