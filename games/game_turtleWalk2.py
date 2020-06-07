from turtle import *
from random import *


def randomcolour():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


john = Turtle()
colormode(255)
john.shape("turtle")
john.pensize(5)
john.speed(1)
john.penup()
john.left(90)
john.goto(0,100)
john.pendown()
for i in range(8):
    john.color(randomcolour())
    john.rt(45)
    john.fd(50)

exitonclick()