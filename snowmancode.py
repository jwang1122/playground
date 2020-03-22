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


drawCircle(-120,100,50)
pen1.color('red','red')
pen1.begin_fill()
drawRectangle(-145,200,50,-80)
pen1.color('red')
pen1.end_fill()
pen1.width(10)
drawLine(-170,200,0,100)
pen1.color('black')
pen1.width(1)
drawCircle(-45,25,75)
drawCircle(-20,-148,100)
pen1.color('blue')
pen1.width(7)
drawCircle(-135,165,1)
drawCircle(-100,165,1)
pen1.width(2)
drawLine(-155,130,-45,25)
pen1.width(1)
pen1.color('black','red')
pen1.begin_fill()
drawTriangle(70,10,50)


screen1.mainloop()