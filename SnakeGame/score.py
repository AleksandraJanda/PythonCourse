from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.message = 'Score: '
        self.count = 0
        self.goto(0,270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f'{self.message}{self.count}', move=False, align='center', font=('Arial', 12, 'normal'))