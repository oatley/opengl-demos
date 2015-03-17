#!/usr/bin/env python

from pyglet.gl import *

#Direct opengl to this window
window = pyglet.window.Window()

# @window.event
# def on_resize(width, height):
# 	glViewport(0, 0, width, height)
# 	glMatrixMode(GL_PROJECTION)
# 	glLoadIdentity()
# 	gluPerspective(65, width / float(height), .1, 1000)
# 	glMatrixMode(GL_MODELVIEW)
# 	return pyglet.event.EVENT_HANDLED



@window.event
def on_draw():
	glClear(GL_COLOR_BUFFER_BIT)
	glLoadIdentity()
	glBegin(GL_TRIANGLES)
	glVertex2f(0, 0)
	glVertex2f(window.width / 2, 0)
	glVertex2f(window.width / 2, window.height / 2)
	glEnd()

pyglet.app.run()