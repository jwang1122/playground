from turtle import *

window = Screen()
window.colormode(255)
window.bgcolor(50,0,70)
john = Turtle()
john.speed(0)
john.width(2)
john.pencolor(250,250,0)

def shape(angle, side, limit):
    reverseDirection = 200
    john.forward(side)

    if side % (reverseDirection * 2) == 0:
        angle += 2
    elif side % reverseDirection == 0:
        angle -= 2

    john.right(angle)
    side += 2
    if side < limit:
        shape(angle, side, limit)

angle = 119
side = 0
limit = 600
shape(angle, side, limit)
exitonclick()
