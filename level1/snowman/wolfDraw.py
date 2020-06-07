from turtle import *

obj_img = './images/wolf.gif'
screen = Screen()
screen.register_shape(obj_img)

john = Turtle()
john.shapesize(10)
john.goto(-0,0)
john.shape(obj_img)
for i in range(6):
    john.rt(60)
    john.fd(100)

input("press any key...")