from turtle import *
from random import *

def getColor():
    return choice(["yellow","lightblue","pink","magenta","aqua"])

def distance():
    return randint(-100, 100)

def angle():
    return randint(0,360)

screen = Screen()
screen.bgcolor(getColor())

t1 = Turtle()
t1.pu()
t1.shape("turtle")
t1.color("red")
x1 = distance()
y1 = distance()
t1.goto(x1, y1)
t1.rt(angle())

t2 = Turtle()
t2.pu()
t2.shape("turtle")
t2.color("blue")
x2 = distance()
y2 = distance()
t2.goto(x2, y2)
t2.lt(angle())

pu()
goto(-300, 300)
pd()
color("blue")
write("the blue turtle is at position (" + str(x2) + ", " + str(y2) + ")",
    move=True,
    font=('Arial', 18, 'normal'))

goto(0, 300)
color("red")
write("the red turtle is at position (" + str(x1) + ", " + str(y1) + ")",
    move = True,
    font=('Arial', 18, 'normal'))

exitonclick()