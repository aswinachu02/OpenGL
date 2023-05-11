from math import radians
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import *

r = 10

ar = [0.1]

def init():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500,500)
    glutCreateWindow("Hareesh")
    glClearColor(0,0,0,0)
    gluOrtho2D(-100,100,-100,100)

def update(x):
    global r, ar
    

    ar.append(ar[len(ar) - 1] + 10)

    glutTimerFunc(int(1000),update,0)
    glutPostRedisplay()

def circle():
    global r,ar
    glColor3f(1,0,0)
    glPointSize(3)
    glBegin(GL_POINTS)
    for j in ar:
        for i in range(0,46):
            x = j*cos(radians(i))
            y = j*sin(radians(i))
            glVertex2f(x,y)
            glVertex2f(x,-y)
            glVertex2f(-x,y)
            glVertex2f(-x,-y)
            glVertex2f(y,x)
            glVertex2f(y,-x)
            glVertex2f(-y,x)
            glVertex2f(-y,-x)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    circle()
    glFlush()

def main():
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0,update,0)
    glutMainLoop()

main()