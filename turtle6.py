"""
random moving the turtle on mouse click,
only allow the turtle moving within certain area.
"""
from turtle import *
from random import *

def distance():
    return randint(-100,200)

def angle():
    return randint(-380, 360)

john = Turtle()
john.shape("turtle")
john.color("red")
john.pensize(5)
john.shapesize(2)
john.forward(120)
john.right(45)
john.fd(50)

def tap(x, y):
    john.right(angle())
    john.forward(distance())
    pos = john.position()
    if pos[0] < -200 or pos[0] > 200 or pos[1] < -200 or pos[1] > 200:
        john.goto(x, y)

john.onclick(tap)

mainloop()

exitonclick()