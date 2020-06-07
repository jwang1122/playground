from turtle import *

def drawSpiral(s, a):
    if s>0:
        forward(s)
        right(a)
        drawSpiral(s-5, a)

length = 400
angle = 121
penup()
setpos(-length/2, length/2)
pendown()

drawSpiral(length, angle)

exitonclick()