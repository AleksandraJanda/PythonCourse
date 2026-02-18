import turtle as t

tim = t.Turtle()
screen = t.Screen()

def a():
    tim.left(45)

def d():
    tim.right(45)

def s():
    tim.backward(10)

def w():
    tim.forward(10)

def c():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

tim.shape('turtle')
tim.pensize(2)
tim.speed(10)

screen.listen()
screen.onkey(a, 'a')
screen.onkey(d, 'd')
screen.onkey(s, 's')
screen.onkey(w, 'w')
screen.onkey(c, 'c')

screen.exitonclick()