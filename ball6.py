"""
Move the ball gradually on fire.
When the ball is out of the screen, put the ball back.
"""
from turtle import *
from freegames import vector

cannon = Turtle(visible=False)
cannon.pu()
cannon.screen.bgcolor("aqua")

def draw():
    cannon.pu()
    cannon.clear()
    cannon.goto(pos.x, pos.y)
    cannon.dot(20,'red')

    if speed.y != 0:
        speed.y += 0.35
        pos.move(speed)
        if pos.y > 300:
            speed.y = 0
            pos.y = -200
        

    ontimer(draw, 20) 

def west():
    pos.x -= 30


def east():
    pos.x += 30

def fire():
    speed.y = 10

pos = vector(0,-200)
speed = vector(0, 0)
tracer(False)
onkey(west, 'Left')
onkey(east, 'Right')
onkey(fire, "space")
listen()

draw()

exitonclick()
