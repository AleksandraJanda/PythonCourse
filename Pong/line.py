from turtle import Turtle

class Line(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.y_max = 300
        self.y_min = -300
        self.draw_dash()

    def draw_dash(self):
        self.penup()
        self.goto(0, self.y_min)


        current_position = self.ycor()

        while self.ycor() < self.y_max:
            if self.ycor()%20 == 0:
                self.pendown()
            else:
                self.penup()
            self.goto(0, current_position)
            current_position += 10