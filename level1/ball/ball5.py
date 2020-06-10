"""
Move the ball gradually on fire.
"""
from turtle import *
from freegames import vector

t1 = Turtle(visible=False)
t1.penup()


def draw():
    t1.pu()
    t1.clear()
    t1.goto(pos.x, pos.y)
    t1.dot(20)

    if speed.y != 0:
        speed.y += 0.35
        pos.move(speed)

    ontimer(draw, 20) 

def west():
    pos.x -= 30


def east():
    pos.x += 30

def fire():
    speed.y = 25

pos = vector(0,-200)
speed = vector(0, 0)
tracer(False)
onkey(west, 'Left')
onkey(east, 'Right')
onkey(fire, "space")
listen()

draw()

exitonclick()
