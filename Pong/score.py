from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')

    def set_position(self,x,y):
        self.goto(x,y)

    def update(self,score):
        self.clear()
        self.write(arg=score, move=False, align='center', font=('Arial',22,'normal'))
