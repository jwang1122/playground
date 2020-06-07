import pyglet

display = pyglet.canvas.get_display()

for screen in display.get_screens():
    print(screen)

#pyglet.app.run()