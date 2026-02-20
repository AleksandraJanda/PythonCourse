from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-290,260)
        self.level = 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(arg=f'Level: {self.level}', align='left', font=FONT)