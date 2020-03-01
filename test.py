from turtle import *
from random import *
from freegames import vector
bg_img=r'grassField.gif'
screen = Screen()
s = Shape('compound')
poly1 = ((0,0),(10,-5),(0,10),(-10,-5))
s.addcomponent(poly1,'red','green')
poly2 = ((0,0),(10,-5),(-10,-5))
s.addcomponent(poly2,'blue','yellow')
screen.bgpic(bg_img)
screen.register_shape("myshape", s)

shape("myshape")
pu()
goto(100, 100)
pd()
pensize(5)
pencolor('red')
color('red','red')
begin_fill()
for i in range(12):
    lt(30)
    fd(20)
end_fill()
pu()
goto(0,500)

exitonclick()