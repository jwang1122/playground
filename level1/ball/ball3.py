"""
Use left and right arrow key to move the ball to left or right.
"""
from turtle import *
from freegames import vector

t1 = Turtle(visible=False)
t1.pu()

def draw():
    t1.clear()
    t1.goto(pos.x, pos.y)
    t1.dot(20)

    ontimer(draw, 20)


def west():
    pos.x -= 30


def east():
    pos.x += 30

pos = vector(0,-200)
tracer(False)
onkey(west, 'Left')
onkey(east, 'Right')
listen()

draw()

exitonclick()
