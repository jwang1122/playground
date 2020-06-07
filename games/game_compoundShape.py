"""
1. create compound shape
2. draw cicle and fill with color
3. write string on final position
"""
from turtle import *
from random import *
from freegames import vector


bg_img=r'grassField.gif'
screen = Screen()
screen.title("Welcome to turtle python")
s = Shape('compound')
poly1 = ((0,0),(10,-5),(0,10),(-10,-5))
s.addcomponent(poly1,'red','green')
poly2 = ((0,0),(10,-5),(-10,-5))
s.addcomponent(poly2,'blue','red')
screen.register_shape("myshape", s)

screen.bgpic(bg_img)

shape("myshape")
pu()
goto(-200, 100)
pd()
#shapesize(2)
pencolor('red')
color('red','red')
begin_fill()
for i in range(12):
    lt(30)
    fd(20)
end_fill()
pu()
fd(30)
write((screen.getshapes()), font=('Arial',14,'bold'))

#pu()
#goto(0,500)
s.hide

exitonclick()