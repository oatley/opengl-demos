#!/usr/bin/env python

from pyglet.gl import *
from pyglet.window import key

dx = 0.0
dy = 0.0
d = 1.0
thrustx = 0.0
thrusty = 0.0
thrustd = 1.0

mvx = 0.0
mvy = 0.0

#Direct opengl to this window
window = pyglet.window.Window(800, 600)
# KEY HANDLER FOR AWESOME WINDOWS
key_handler = key.KeyStateHandler()
window.push_handlers(key_handler)

# START 3D !
@window.event
def on_resize(width, height):
		glEnable(GL_DEPTH_TEST)
		glDisable(GL_CULL_FACE)
		glViewport(0, 0, width, height)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluPerspective(65, width / float(height), .1, 1000)
		glMatrixMode(GL_MODELVIEW)
		return pyglet.event.EVENT_HANDLED

def update(dt):
	 on_draw()

@window.event
def on_draw():
	global dx, dy, d, thrustd, thrustx, thrusty, window, key_handler, mvx, mvy
	t = 0.5 * window.width
	if key_handler[key.LEFT]:
		#print "left"
		dx = 1.0
		thrustx += 1
	if key_handler[key.RIGHT]:
		#print "right"
		dx = 1.0
		thrustx -= 1
	if key_handler[key.UP]:
		#print "up"
		dy = 1.0
		thrusty += 1
	if key_handler[key.DOWN]:
		#print "down"
		dy = 1.0
		thrusty -= 1
	if key_handler[key.Z]:
		#print "zoom in"
		d = 1.0
		thrustd += 0.01
	if key_handler[key.X]:
		#print "zoom out"
		d = 1.0
		thrustd -= 0.01

	# Camera
	if key_handler[key.W]:
		print "camera - up"
		mvy -= 0.01
	if key_handler[key.A]:
		print "camera - left"
		mvx += 0.01
	if key_handler[key.S]:
		print "camera - down"
		mvy += 0.01
	if key_handler[key.D]:
		print "camera - right"
		mvx -= 0.01


	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()

	glTranslatef(mvx, mvy, -5.0)
	glRotatef(thrustx, 0.0, dx, 0.0)
	glRotatef(thrusty, dy, 0.0, 0.0)

	#fractal(l=thrustd, n=3)
	#cube(l=thrustd)
	#draw_akshay(l=thrustd)

def draw_akshay(l=0.0, transx=0.0, transy=0.0, transz=0.0):
	cube(l=l/1.5, transx=transx, transy=transy, transz=transz)
	glPushMatrix()
	cube(l=l, transx=transx, transy=transy-1.0, transz=transz)
	glPushMatrix()
	cube(l=l, transx=transx+1.0, transy=transy, transz=transz)
	cube(l=l/2, transx=transx, transy=transy-1.0, transz=transz)
	cube(l=l/2, transx=transx, transy=transy-1.0, transz=transz)
	glPopMatrix()
	cube(l=l, transx=transx-1.0, transy=transy, transz=transz)
	cube(l=l/2, transx=transx, transy=transy-1.0, transz=transz)
	cube(l=l/2, transx=transx, transy=transy-1.0, transz=transz)
	glPopMatrix()
	




def fractal(l=0.0, n=1, transx=0.0, transy=0.0, transz=0.0):
	cube(l=l, transx=transx, transy=transy, transz=transz)
	if n:
		modx = 1.5
		mody = 1.5
		modz = 1.5
		glPushMatrix()
		fractal(l=l/2, n=n-1, transx=0.0, transy=mody, transz=0.0)
		glPopMatrix() 
		glPushMatrix()
		fractal(l=l/2, n=n-1, transx=0.0, transy=-mody, transz=0.0)
		glPopMatrix()
		glPushMatrix()
		fractal(l=l/2, n=n-1, transx=0.0, transy=0.0, transz=modz)
		glPopMatrix()
		glPushMatrix()
		fractal(l=l/2, n=n-1, transx=0.0, transy=0.0, transz=-modz)
		glPopMatrix()
		glPushMatrix()
		fractal(l=l/2, n=n-1, transx=modx, transy=0.0, transz=0.0)
		glPopMatrix()
		glPushMatrix()
		fractal(l=l/2, n=n-1, transx=-modx, transy=0.0, transz=0.0)
		glPopMatrix()

def cube(l=0.0, transx=0.0, transy=0.0, transz=0.0):
	glTranslatef((l*2) * transx, (l*2) * transy, (l*2) * transz)
	draw_square_top(l=l, color=[1.0, 0.0, 0.0])
	draw_square_top(l=-l, color=[1.0, 0.0, 0.0])
	draw_square_front(l=l, color=[0.0, 1.0, 0.0])
	draw_square_front(l=-l, color=[0.0, 1.0, 0.0])
	draw_square_right(l=l, color=[0.0, 0.0, 1.0])
	draw_square_right(l=-l, color=[0.0, 0.0, 1.0])

def draw_square_top(l=1.0, color=[1.0, 1.0, 1.0]):
	glBegin(GL_POLYGON)
	glColor3f(*color)
	glVertex3f(  l, l,  l)
	glVertex3f(  l, l, -l)
	glVertex3f( -l, l, -l)
	glVertex3f( -l, l,  l)
	glEnd()

def draw_square_front(l=1.0, color=[1.0, 1.0, 1.0]):
	glBegin(GL_POLYGON)
	glColor3f(*color)
	glVertex3f( l, -l, -l)
	glVertex3f( l,  l, -l)
	glVertex3f(-l,  l, -l)
	glVertex3f(-l, -l, -l)
	glEnd()

def draw_square_right(l=1.0, color=[1.0, 1.0, 1.0]):
	glBegin(GL_POLYGON)
	glColor3f(*color)
	glVertex3f( l, -l,  -l)
	glVertex3f( l,  l,  -l)
	glVertex3f( l,  l,   l)
	glVertex3f( l, -l,   l)
	glEnd()

pyglet.clock.schedule_interval(update, 1/120.0)
pyglet.app.run()
