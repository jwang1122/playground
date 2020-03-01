import pyglet

context = pyglet.gl.get_current_context()
object_space = context.object_space
window = pyglet.window.Window()
label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          color=(255,255,255,255),
                          anchor_x='center', anchor_y='center')
@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()