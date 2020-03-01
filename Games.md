# Games Exercise Document

[pyglet Document](https://pyglet.readthedocs.io/en/stable/index.html)
[Turtle Document](https://docs.python.org/3.3/library/turtle.html?highlight=turtle)
[20 modules must have](https://pythontips.com/2013/07/30/20-python-libraries-you-cant-live-without/)
[OpenGL](https://www.opengl.org/)
[OpenGL SDK](https://www.opengl.org/sdk/)

'''py
 python -m turtledemo
 ```
## install ffmpeg for play music in pyglet
```
sudo chown -R $(whoami) /usr/local/share/man/man3
brew install ffmpeg
pip install PyOpenGL
```

## Game learning steps
* Draw turtle on screen (game_turtleWalk.py)
* Move ball around within screen (game_bounce.py)
* Use key to controll ball (game_moveBall.py)
* Use mouse to controll ball (game_moveBallByMouse.py)
* Show image on the screen ()
* Use key to controll the image
* draw backgroun on the screen (game_showImage.py)
* write score message on screen

## turtle drawing
![Snow couple](snowCouple.png)

## game_bounce.py

* Make the ball big or smaller
* Make the ball speed up and down
* Change how the ball bounces when it hits a wall
* Change the ball color
* Change background color
* write a program test how random() works
* write a program test how choice() works
* write a program test how vector() works


# display turtle

```py
t=Turtle()
t.shape("turtle")
```

# display background image
```py
bg_img = r'snowCouple.png'
screen = Screen()

screen.bgpic(bg_img)
```

# register new shape from image file
```py
obj_img = 'wolf.gif'
screen = Screen()
screen.register_shape(obj_img)
john = Turtle()
john.shape(obj_img)
```

# change turtle color
```py
john = Turtle()
colormode(255)
john.shape("turtle")
john.color(12,45,190)
```