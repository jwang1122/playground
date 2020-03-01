from random import *
from turtle import *
from freegames import vector


def draw():
    clear()
    goto(ball.x, ball.y)
    dot(20, 'red')

    ontimer(draw, 20)


def tap(x, y):
    ball.x += (x-ball.x)/10
    ball.y += (y-ball.y)/10


ball = vector(0, 0)

setup(420, 420, 200, 200)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
