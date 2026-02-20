import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from tkinter import messagebox

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = Screen()
screen.title('Turtle Crossing')
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)
screen.bgcolor('white')
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.up,'Up')

game_is_on = True

def game():
    global game_is_on
    game_is_on = True

    while game_is_on:
        time.sleep(0.1)

        car_manager.move()

        screen.update()

        if (SCREEN_HEIGHT/2 - player.ycor()) <= 10:
            player.set_starting_position()
            scoreboard.level += 1
            scoreboard.update_level()
            car_manager.speed += 1

        for car in car_manager.cars:
            if -20 < car.xcor() < 20 and len(car_manager.cars) <= 25:
                car_manager.generate_new_car()

        for car in car_manager.cars:
            if car.xcor() < -340:
                car_manager.clear(car_manager.cars.index(car))

        for car in car_manager.cars:
            if player.distance(car) < 20:
                game_is_on = False
                messagebox.showerror(message='GAME OVER!')
                if messagebox.OK:
                    player.set_starting_position()
                    scoreboard.level = 1
                    scoreboard.update_level()
                    car_manager.speed = 5
                    game()

game()

screen.exitonclick()