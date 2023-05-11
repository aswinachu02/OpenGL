from OpenGL.GL import *
from OpenGL.GL.ARB import separate_shader_objects
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import cos,sin,radians

r1 = 30
r2 = 20
xc = 100
yc = 100
theta = 90
r3 = 100

def init():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500,500)
    glutCreateWindow("Saleem")
    glClearColor(0,0,0,0)
    gluOrtho2D(-250,250,-250,250)


def update(n):
    global xc,yc,theta
    theta += 1
    glutTimerFunc(int(1000/60),update,0)
    glutPostRedisplay()

def planet():
    global r2
    xp = r3*cos(radians(theta)) 
    yp = r3*sin(radians(theta)) 
    glColor3f(0,0,1)
    glLineWidth(1)
    glBegin(GL_TRIANGLE_FAN)
    for i in range (0,360):
        offset = theta/10
        if i < 180:
            glColor3f(0,1,0)
        else:
            glColor3f(0,0,1)
        glVertex2f(r2*cos(offset + radians(i))+xp,r2*sin(offset + radians(i))+yp)
    glEnd()

def sun():
    global r
    glColor3f(1,0.5,0)
    glLineWidth(1)
    glBegin(GL_TRIANGLE_FAN)
    for i in range (0,360):
        glVertex2f(r1*cos(radians(i)),r1*sin(radians(i)))
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    sun()
    planet()
    glFlush()

def main():
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0,update,0)
    glutMainLoop()

main()