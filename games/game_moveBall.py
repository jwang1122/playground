from random import *
from turtle import *
from freegames import vector


def draw():
    clear()
    goto(ball.x, ball.y)
    dot(20, 'red')

    ontimer(draw, 20)

def north():
    ball.y += 10

def south():
    ball.y -=10

def west():
    ball.x -= 10

def east():
    ball.x += 10

ball = vector(0,0)

setup(420,420,200,200)
hideturtle()
tracer(False)
onkey(north, 'Up')
onkey(south, 'Down')
onkey(west, 'Left')
onkey(east, 'Right')
listen()
draw()
exitonclick()
