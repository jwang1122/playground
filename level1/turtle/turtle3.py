"""
response mouse click on tutle to move the turtle around
"""
from turtle import *


john = Turtle()
john.shape("turtle")
john.color("red")
john.pensize(5)
john.shapesize(2)
john.forward(120)
john.right(45)
john.fd(50)

def tap(x, y):
    john.right(45)
    john.forward(50)

john.onclick(tap)

mainloop()
