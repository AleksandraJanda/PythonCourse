from turtle import Turtle

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.heading = 0
        self.collision = False

    def clear(self):
        self.segments[3:].clear()

    def create_snake(self):
        for _ in range(0, 3):
            segment = Segment()
            self.segments.append(segment)

        for i in range(len(self.segments)):
            if i > 0:
                self.segments[i].goto(self.segments[i - 1].xcor() - 20, self.segments[i - 1].ycor())
            self.segments[0].goto(0, 0)

    def move(self):
        for s in range(len(self.segments) - 1, 0, -1):
            x = self.segments[s - 1].xcor()
            y = self.segments[s - 1].ycor()
            self.segments[s].goto(x, y)

        self.segments[0].forward(20)

    def set_heading(self,heading):
        self.heading = heading
        self.segments[0].setheading(heading)

    def up(self):
        if self.heading != 270:
            self.set_heading(90)

    def down(self):
        if self.heading != 90:
            self.set_heading(270)

    def left(self):
        if self.heading != 0:
            self.set_heading(180)

    def right(self):
        if self.heading != 180:
            self.set_heading(0)

    def grow(self):
        segment = Segment()
        self.segments.append(segment)
        repositionx = 0
        repositiony = 0
        if self.heading == 0:
            repositionx = -20
        elif self.heading == 90:
            repositiony = 20
        elif self.heading == 180:
            repositionx = 20
        elif self.heading == 270:
            repositiony = -20
        self.segments[-1].goto(self.segments[-2].xcor() + repositionx, self.segments[-2].ycor() + repositiony)

    def tail_collision(self):
        for s in range(1, len(self.segments)):
            if self.segments[0].distance(self.segments[s]) <= 10:
                return True
        return None


class Segment(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.speed(1)
        self.color('white')

    def clear(self):
        self.goto(-500,-500)