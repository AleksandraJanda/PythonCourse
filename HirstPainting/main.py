import turtle as t
import random

colors = [(23, 126, 213), (24, 182, 216), (36, 84, 43), (39, 70, 46), (41, 138, 218), (45, 112, 40), (63, 180, 226), (68, 162, 37), (87, 203, 146), (87, 29, 37), (95, 40, 48), (99, 43, 23), (108, 45, 27), (111, 216, 247), (131, 234, 210), (162, 81, 28), (172, 59, 112), (172, 131, 29), (207, 233, 246), (233, 251, 246), (236, 221, 87), (236, 168, 89), (236, 130, 159), (237, 50, 83), (244, 153, 148), (250, 55, 14), (251, 137, 144), (252, 222, 0), (253, 253, 248), (254, 247, 250)]

t.colormode(255)

pen = t.Turtle()

pen.speed()
pen.pensize(20)
pen.hideturtle()
pen.penup()
pen.goto(-250,-250)

for i in range(10):
    for j in range(10):
        pen.pendown()
        pen.dot(20,random.choice(colors))
        pen.penup()
        pen.forward(50)
    pen.goto(-250,pen.ycor()+50)

screen = t.Screen()
screen.exitonclick()