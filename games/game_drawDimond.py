from turtle import *
import random

window = Screen()
window.bgcolor('grey')
john = Turtle()
john.width(5)
colours = ['cyan','purple','white','red','blue']

def draw():
    john.color('cyan')
    for i in range(10):
        for i in range(2):
            john.fd(100)
            john.right(60)
            john.forward(100)
            john.right(120)
        john.right(36)
        john.color(random.choice(colours))

draw()
exitonclick()
