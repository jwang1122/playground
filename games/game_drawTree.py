from turtle import *

def branch(t, length, angle, scale):
    if length < 10:
        return
    t.fd(length)
    t.lt(angle)
    branch(t, length * scale, angle, scale)
    t.rt(angle*2)
    branch(t, length*scale, angle, scale)
    t.lt(angle + 180)
    t.fd(length)
    t.lt(180)

def draw():
    window = Screen()
    window.bgcolor("#E3F2FD")
    tracer(25, None)
    t = Turtle()
    t.shape("turtle")
    t.color("#1B5E20")
    t.speed(0)
    t.left(90)
    branch(t, 70, 25, 0.8)
    t.color("brown")
    t.left(180)
    branch(t, 70, 32, 0.75)
    window.exitonclick()

draw()
