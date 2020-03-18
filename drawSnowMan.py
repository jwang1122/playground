from turtle import *
from snowman import *

pen1 = Turtle()
screen1 = Screen()
pen1.shape("turtle")

man = Snowman(0,0,20,40,70)
man.draw(pen1)

kid = Snowman(130, -50, 10,20,40)
kid.draw(pen1)


woman = Snowman(-140,0,20,40,70)
woman.draw(pen1)

pen1.hideturtle()


screen1.mainloop()