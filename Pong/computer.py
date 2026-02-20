from paddle import Paddle
import time

class Computer(Paddle):

    def __init__(self):
        super().__init__()
        self.set_position(380,0)
        self.direction = 'up'

    def move(self,direction):
        if direction == 'up':
            self.move_up()
        else:
            self.move_down()

    def move_in_loop(self):
        if self.ycor() == 240:
            self.direction = 'down'
        elif self.ycor() == -240:
            self.direction = 'up'
        self.move(self.direction)
        time.sleep(0.1)