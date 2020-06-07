from turtle import *
import random

wn = Screen()
terry = Turtle()
wn.bgcolor("red")
terry.color("white")
for i in range(50):
    terry.right(random.randint(0, 45))
    distance = random.randint(0, 150)
    terry.forward(distance)
    terry.backward(distance)
    aifjaldi
