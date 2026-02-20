from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
ROADS_COORDS = [200,150,100,50,0,-50,-100,-150,-200]
CARS_COORDS = [100,150,200,250,300,350,400,450,500,550,600,650]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.speed = 5
        self.generate_cars()

    def generate_cars(self):
        for c in ROADS_COORDS:
            car = Car()
            car.place_car(c)
            self.cars.append(car)

    def move(self):
        for c in self.cars:
            c.forward(self.speed)

    def clear(self,id):
        self.cars[id].clear()
        self.cars.pop(id)

    def generate_new_car(self):
        new_car = Car()
        new_car.place_car(random.choice(ROADS_COORDS))
        self.cars.append(new_car)
        self.move()

class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color(random.choice(COLORS))
        self.setheading(180)

    def place_car(self,y):
        if self.speed == 5:
            self.goto(random.choice(CARS_COORDS[:6]),y)
        else:
            self.goto(random.choice(CARS_COORDS[4:]), y)
