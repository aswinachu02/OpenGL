from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import *


r1 = 40
r2 = 130

xt = 300
yt = 0

ax = []
ay = []

speed = 1
theta = 0

def init():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500,500)
    glutCreateWindow("Bouncing")
    glClearColor(0,0,0,0)
    gluOrtho2D(-500,500,-500,500)


def circle():
    global r1,r2,theta
    glColor3f(1,0,0)
    glPointSize(3)
    glBegin(GL_POINTS)
    xc = r2*cos(radians(theta)) + xt
    yc = r2*sin(radians(theta))
    ax.append(xc)
    ay.append(yc)
    for j in range (0,r1):
        for i in range (0,46):
            x = j*cos(radians(i))
            y = j*sin(radians(i))
            glVertex2f(x+xc,y+yc)
            glVertex2f(x+xc,-y+yc)
            glVertex2f(-x+xc,y+yc)
            glVertex2f(-x+xc,-y+yc)
            glVertex2f(y+xc,x+yc)
            glVertex2f(-y+xc,x+yc)
            glVertex2f(y+xc,-x+yc)
            glVertex2f(-y+xc,-x+yc)
    glEnd()

def trail():
    global ax,ay,r2
    glColor3f(0,1,0)
    glPointSize(1)
    glBegin(GL_POINTS)
    for i in range (0, len(ax)):
        glVertex2f(ax[i],ay[i]-r1)
    glEnd()

def update(n):
    global speed,theta,xt,r2
    theta += speed
    if theta == 180:
        theta = 0
        xt -= 2*r2-30
        r2 -= 30
    if r2 <0:
        speed = 0
    
    glutTimerFunc(1,update,0)
    glutPostRedisplay()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    trail()
    circle()
    glFlush()

def main():
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0,update,0)
    glutMainLoop()

main()