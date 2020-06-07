import pyglet

display = pyglet.canvas.get_display()
screens = display.get_screens()
window = pyglet.window.Window(fullscreen=False, screen=screens[1], resizable = True)
label0 = pyglet.text.Label('(0,0)',
                           font_name='Times New Roman',
                           font_size=12,
                           x=30, y=10,
                           color=(255, 255, 255, 255),
                           anchor_x='center', anchor_y='center')
label1 = pyglet.text.Label('(120,150)',
                           font_name='Times New Roman',
                           font_size=12,
                           x=120, y=170,
                           color=(255, 255, 255, 255),
                           anchor_x='center', anchor_y='center')
label2 = pyglet.text.Label('(230,150)',
                           font_name='Times New Roman',
                           font_size=12,
                           x=240, y=130,
                           color=(255, 255, 255, 255),
                           anchor_x='center', anchor_y='center')


@window.event
def on_draw():
    window.clear()
    pyglet.graphics.draw(3, pyglet.gl.GL_TRIANGLES,
                         ('v2i', (120, 150, 230, 150, 0, 0)))
    label0.draw()
    label1.draw()
    label2.draw()

    """ 
    two adjacent triangles are drawn, and the shared vertices are reused with indexing,
    Note that the first argument gives the number of vertices in the data, not the number of 
    indices (which is implicit on the length of the index list given in the third argument).
    """
    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                 # [0, 1, 2, 0, 2, 3], # two triangles share same vertices on indexed 0, and 2.
                                 # [0, 3, 2, 0, 3, 2], # two triangles on the same vertices overlap each other.                                 
                                 [0, 3, 2, 3, 1, 2], # two triangles overlap partially.
                                 ('v2i', (300, 100,
                                          350, 100,
                                          350, 250,
                                          300, 250)),
                                 ('c3B', (255, 0, 0, 255, 0, 0, 0, 0, 255, 0, 255, 0))) 
                                 # define color for each vertices, so you need 4 rgb colors.
                                 # c: color; 3: three data for each component; B: unsigned integer


pyglet.app.run()
