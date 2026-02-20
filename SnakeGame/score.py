from os import write
from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.count = 0
        self.goto(0,270)
        self.high_score = 0
        self.read_high_score()
        self.update_score()

    def write_high_score(self):
        with open('data.txt', mode='w') as file:
            file.write(str(self.count))

    def read_high_score(self):
        with open('data.txt') as file:
            hs = file.read()
            self.high_score = int(hs)

    def check_highest_score(self):
        if self.count > self.high_score:
            self.write_high_score()
        self.read_high_score()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f'Score: {self.count} -- High Score: {self.high_score}', move=False, align='center', font=('Arial', 12, 'normal'))