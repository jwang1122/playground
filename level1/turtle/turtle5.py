"""
limit the turtle within window bounds
"""
from turtle import *
from random import *


def newX():
    return randint(-300, 300)


def newY():
    return randint(-300, 300)


john = Turtle()
john.shape("turtle")
john.color("red")
john.pensize(5)
john.shapesize(2)
john.forward(120)
john.right(45)
john.fd(50)


def tap(x, y):
    pos = john.position()
    x = pos[0] + newX()
    y = pos[1] + newY()
    if x > 300 or x < -300: x = pos[0]
    if y > 300 or y < -300: y = pos[1]
    john.goto(x, y)


john.onclick(tap)

mainloop()

exitonclick()