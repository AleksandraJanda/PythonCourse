import turtle as t
import random
from tkinter import messagebox

t.colormode(255)

screen = t.Screen()
screen.setup(width=600,height=400)
screen.title('Turtle Race!')

# FUNCTIONS
def generate_color():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

def set_color_turtles():
    for i in range(0,len(turtles)):
        turtles[i].color('black',generate_color())
        turtles[i].shape("turtle")

def set_starting_position():
    reset_position()
    for turtle in turtles:
        turtle.write(arg=f'{turtles.index(turtle)+1}__', move=False, align='right')

def reset_position():
    pos = screen.window_height()/2-50
    for turtle in turtles:
        turtle.penup()
        turtle.hideturtle()
        turtle.speed(10)
        turtle.goto(-250,pos)
        turtle.showturtle()
        pos -= (screen.window_height()-60)//len(turtles)

def get_turtle_color(turtle):
    color = turtle.color()[1]
    print(color)

def set_line(line,x):
    line.hideturtle()
    line.penup()
    line.setx(x)
    line.sety(200)
    line.pendown()
    line.right(90)
    line.forward(screen.window_height())
    #line.write("Turtle")

def move(turtle):
    steps = random.randint(0,10)
    turtle.forward(steps)

def check_turtles_pos():
    turtles_pos = []
    for turtle in turtles:
        turtles_pos.append(turtle.xcor())
    return turtles_pos

def winner(pos_list):
    max_val = max(pos_list)
    return pos_list.index(max_val)

def race():
    reset_position()
    user_bet = screen.textinput(title='Make your bet',prompt='Who will win?')
    if type(user_bet) == str and int(user_bet) <= len(turtles):
        reset_position()

        positions = check_turtles_pos()

        while max(positions) < 200:
            for turtle in turtles:
                move(turtle)
            positions = check_turtles_pos()

        messagebox.showinfo(title='Winner',message=f'The winner is: {winner(positions)+1}. Your choice was: {user_bet}')
        race()

# RACE__________________________
turtles_num = screen.textinput(title='How many turtles?', prompt='How many turtles?')

turtles = []
for _ in range(0,int(turtles_num)):
    turtles.append(t.Turtle())

start_line = t.Turtle()
finish_line = t.Turtle()

set_line(start_line,-200)
set_line(finish_line,200)
set_color_turtles()
set_starting_position()
race()
#_______________________________

screen.exitonclick()