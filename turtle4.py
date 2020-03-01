"""
Randomly moving turtle on mouse click.
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
 
john.onclick(tap)

mainloop()

exitonclick()