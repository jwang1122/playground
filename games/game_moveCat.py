from turtle import *
from random import *

obj_img = 'cat.gif'
bg_img = r'grassField.gif'
screen = Screen()
screen.register_shape(obj_img)
screen.bgpic(bg_img)
setup(640,480,0,0)
john = Turtle()
john.shapesize(1)
john.pu()
john.shape(obj_img)

def draw():
    x = randint(-200,200)
    y = randint(-200, 0)

    john.goto(x, y)
        
    ontimer(draw, 50)

draw()

exitonclick()
