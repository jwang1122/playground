from turtle import *

pen1 = Turtle()
screen1 = Screen()

def drawCircle(x, y, r):
    """
    draw a circle with radius r and position (x, y)
    """
    pen1.up()
    pen1.goto(x,y)
    pen1.down()
    pen1.circle(r)

def drawRectangle(x, y, width, height):
    """
    draw a circle with radius r and position (x, y)
    """
    pen1.up()
    pen1.goto(x,y)
    pen1.down()
    pen1.fd(width)
    pen1.right(90)
    pen1.fd(height)
    pen1.right(90)
    pen1.fd(width)
    pen1.right(90)
    pen1.fd(height)

def drawLine(x,y,angle,length):
    pen1.up()
    pen1.goto(x,y)
    pen1.down()
    pen1.right(angle)
    pen1.fd(length)

def drawTriangle(x, y, side):
    pen1.up()
    pen1.goto(x,y)
    pen1.down()
    pen1.right(60)
    pen1.fd(side)
    pen1.right(120)
    pen1.fd(side)
    pen1.right(120)
    pen1.fd(side)

drawLine(10,10,-45,50)
# drawCircle(100,100,50)
# drawRectangle(10,10,60,40)
# pen1.width(10)
# pen1.color('red')
# drawLine(10,10,-10,50)
# pen1.width(1)
# pen1.color('black','red')
# pen1.begin_fill()
# drawTriangle(70,10,50)
# pen1.end_fill()

screen1.mainloop()