import pyglet

gunshot = pyglet.resource.media('9_mm_gunshot.wav', streaming=False)
gunshot.play()

pyglet.app.run()