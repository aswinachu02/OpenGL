from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import *
from datetime import *


r = 50
l1 = 48
l2 = 38
l3 = 28
theta1 = 90
theta2 = 90
theta3 = 90


def init():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500,500)
    # glutInitWindowPosition(100,100)
    glutCreateWindow("Sudheep")
    glClearColor(0,0,0,0)
    gluOrtho2D(-100,100,-100,100)

def update(n):
    global theta1,theta2,theta3
    theta1 -= 360/60
    theta2 -= 360/3600
    theta3 -= 360/(3600*12)
    glutTimerFunc(1000,update,0)
    glutPostRedisplay()

def hour():
    global l1,theta1
    glColor3f(1,1,0)
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(0,0)
    x = l1*cos(radians(theta1))
    y = l1*sin(radians(theta1))
    glVertex2f(x,y)
    glEnd()

def minute():
    global l2,theta2
    glColor3f(1,0,0)
    glLineWidth(4)
    glBegin(GL_LINES)
    glVertex2f(0,0)
    x = l2*cos(radians(theta2))
    y = l2*sin(radians(theta2))
    glVertex2f(x,y)
    glEnd()

def second():
    global l3,theta3
    glColor3f(0,1,0)
    glLineWidth(6)
    glBegin(GL_LINES)
    glVertex2f(0,0)
    x = l3*cos(radians(theta3))
    y = l3*sin(radians(theta3))
    glVertex2f(x,y)
    glEnd()

def circle():
    glColor3f(0,0,1)
    glLineWidth(4)
    glBegin(GL_TRIANGLE_FAN)
    for i in range (0,360):
        glVertex2f(r*cos(radians(i)),r*sin(radians(i)))
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    circle()
    hour()
    minute()
    second()
    glFlush()

def main():
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0,update,0)
    glutMainLoop()

main()
