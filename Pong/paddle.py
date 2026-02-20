from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')
        self.resizemode('user')
        self.shapesize(stretch_wid= 4, stretch_len= 0.5, outline= 12)
        self.y_max = self.ycor()+40
        self.y_min = self.ycor()-40

    def set_position(self,x,y):
        self.goto(x,y)

    def move_up(self):
        self.set_position(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.set_position(self.xcor(), self.ycor() - 20)