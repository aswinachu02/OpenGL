from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import cos,sin,radians

side = 50
theta = 0
r = 10


def init():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500,500)
    glutCreateWindow("Suresh")
    glClearColor(0,0,0,0)
    gluOrtho2D(-100,100,-100,100)


def update(n):
    global theta
    theta += 1
    glutTimerFunc(int(1000/60),update,0)
    glutPostRedisplay()


def rotated_points(vertex,theta):
    return[
        round(
            (vertex[0])*cos(radians(theta)) 
            - (vertex[1])*sin(radians(theta))
            ),
        round(
            (vertex[0])*sin(radians(theta)) 
            + (vertex[1])*cos(radians(theta))
        )
    ]

def fan():
    global side
    vertices = [
        [0,0],
        [-side/4,side],
        [side/4,side]
    ]
    glColor3f(1,0,1)
    glLineWidth(5.0)
    glBegin(GL_POLYGON)
    # for vertex in vertices:
    #     glVertex2fv(vertex)
    for vertex in vertices:
        glVertex2fv(rotated_points(vertex,theta))
    for vertex in vertices:
        glVertex2fv(rotated_points(vertex,theta+120))
    for vertex in vertices:
        glVertex2fv(rotated_points(vertex,theta+240))        
    glEnd()

def pillar():
    vertices = [
        [-5,0],
        [-5,-100],
        [5,-100],
        [5,0]
    ]
    glColor3f(0,0.5,0.5)
    glLineWidth(1)
    glBegin(GL_POLYGON)
    for vertex in vertices:
        glVertex2fv(vertex)
    glEnd()



def circle():
    global r,xc,yc
    glColor3f(0,0,1)
    glLineWidth(1)
    glBegin(GL_TRIANGLE_FAN)
    for i in range (0,360):
        glVertex2f(r*cos(radians(i)),r*sin(radians(i)))
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    pillar()
    fan()
    circle()
    glFlush()

def main():
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0,update,0)
    glutMainLoop()

main()