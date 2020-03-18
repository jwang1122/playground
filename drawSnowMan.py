from turtle import *
from snowman import *

pen1 = Turtle()
screen1 = Screen()
pen1.shape("turtle")

man = Snowman(0, -100, 20, 40, 70)
man.draw(pen1)

kid = Snowman(130, -100, 10, 20, 40)
kid.draw(pen1)

woman = Snowman(-150, -100, 20, 40, 70)
woman.draw(pen1)

drawLine(pen1, -230, -100, 0, 400)
pen1.hideturtle()


screen1.mainloop()
