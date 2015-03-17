#!/usr/bin/env python

from pyglet.gl import *
from pyglet.window import key

#Direct opengl to this window
window = pyglet.window.Window()

dx = 0
dy = 0
thrustx = 0
thrusty = 0

# KEY HANDLER FOR AWESOME WINDOWS
key_handler = key.KeyStateHandler()
window.push_handlers(key_handler)


# START 3D !
@window.event
def on_resize(width, height):
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
   global dx, dy, thrustx, thrusty, window, key_handler
   l = 0.5 * window.width
   if key_handler[key.LEFT]:
      print "left"
      dx = 1.0
      thrustx += 1
   if key_handler[key.RIGHT]:
      print "right"
      dx = 1.0
      thrustx -= 1
   if key_handler[key.UP]:
      print "up"
      dy = 1.0
      thrusty += 1
   if key_handler[key.DOWN]:
      print "down"
      dy = 1.0
      thrusty -= 1

   glClear(GL_COLOR_BUFFER_BIT)
   glLoadIdentity()

   glTranslatef(0.0, 0.0, -5.0)

   glRotatef(thrustx, 0.0, dx, 0.0)
   glRotatef(thrusty, dy, 0.0, 0.0)

   draw_square()


def draw_square(l=1.0, color=[1.0, 1.0, 1.0]):
   glBegin(GL_POLYGON);
   glColor3f(*color);
   glVertex3f( l,  l,  -l);
   glVertex3f( l, -l,  -l);
   glVertex3f(-l, -l,  -l);
   glVertex3f(-l,  l,  -l);
   glEnd();


pyglet.clock.schedule_interval(update, 1/120.0)
pyglet.app.run()