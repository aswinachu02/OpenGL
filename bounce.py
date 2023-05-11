from OpenGL.GL import *
from OpenGL.GL.ARB import separate_shader_objects
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import cos,sin,radians

r = 30
xc = 0
yc = 0
speed = 5
speed2 = 2

def init():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500,500)
    glutCreateWindow("Sumesh")
    glClearColor(0,0,0,0)
    gluOrtho2D(-100,100,-100,100)

def update(n):
    global yc,speed,xc,speed2
    if yc + r == 100:
        speed -= 5
    elif yc - r == -100:
        speed += 5
    if xc + r == 100:
        speed2 -= 2
    elif xc - r == -100:
        speed2 += 2

    xc = xc + speed2
    yc = yc + speed
    glutTimerFunc(50,update,0)
    glutPostRedisplay()


def bounce():
    global r,xc,yc
    glColor3f(0,0,1)
    glLineWidth(1)
    glBegin(GL_TRIANGLE_FAN)
    for i in range (0,360):
        glVertex2f(r*cos(radians(i))+xc,r*sin(radians(i))+yc)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    bounce()
    glFlush()

def main():
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0,update,0)
    glutMainLoop()

main()