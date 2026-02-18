from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time
from tkinter import messagebox

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

game_on = True

snake = Snake()
screen.listen()
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.right, key='Right')

food = Food()
score = Score()

while game_on:
    screen.update()
    time.sleep(0.3)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.move()
        snake.grow()
        score.count += 1
        score.update_score()

    if snake.tail_collision():
        game_on = False

    if abs(snake.segments[0].xcor()) == screen.window_width()/2 or abs(snake.segments[0].ycor()) == screen.window_height()/2:
        game_on = False

messagebox.showinfo(title='Game Over!', message=f'Snake length: {len(snake.segments)}')

screen.exitonclick()