from paddle import Paddle

class Player(Paddle):

    def __init__(self):
        super().__init__()
        self.set_position(-380, 0)
        self.speed(10)
        
    def move_up(self):
        super().move_up()
        self.set_position(self.xcor(), self.ycor() + 20)

    def move_down(self):
        super().move_down()
        self.set_position(self.xcor(), self.ycor() - 20)

    def f(self):
        return None