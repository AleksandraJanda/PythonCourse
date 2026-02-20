from turtle import Screen
from player import Player
from computer import Computer
from line import Line
from score import Score
from ball import Ball

screen = Screen()
screen.title('Pong')
screen.setup(width= 800, height= 600)
screen.bgcolor('black')
screen.tracer(0)
screen.listen()

line = Line()
player = Player()
computer = Computer()
p_score = Score()
c_score = Score()
p_score.set_position(-50,260)
c_score.set_position(50,260)
p_points = 0
c_points = 0
p_score.update(p_points)
c_score.update(c_points)

ball = Ball()

screen.onkey(player.move_up, 'Up')
screen.onkey(player.move_down, 'Down')

game_on = True
while game_on:
    screen.update()
    ball.move()
    computer.move_in_loop()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(computer) <= 50 and ball.xcor() > 320 or ball.distance(player) <= 30 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        p_points += 1
        p_score.update(p_points)

    # Detect L paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()
        c_points += 1
        c_score.update(c_points)

    if player.ycor() == -240:
        screen.onkey(player.move_up, 'Up')
        screen.onkey(player.f, 'Down')
    elif player.ycor() == 240:
        screen.onkey(player.f, 'Up')
        screen.onkey(player.move_down, 'Down')
    else:
        screen.onkey(player.move_up,'Up')
        screen.onkey(player.move_down,'Down')

screen.exitonclick()
