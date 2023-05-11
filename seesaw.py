from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import cos,sin,radians

length = 50
theta = 0
speed = 1
x1 = 0
x2 = 0
y1 = 0
y2 = 0
r = 5
state =1

def init():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500,500)
    glutCreateWindow("Radheesh")
    glClearColor(0,0,0,0)
    gluOrtho2D(-100,100,-100,100)


def update(n):
    global theta,speed,state
    # theta += 1*speed

    # if theta == 20:

    #     speed = -speed
    # elif theta == -20:

    #     speed = -speed
    if state == 1:
        if theta < 20:
            theta += speed
        else:
            state = -1
    elif state == -1:
        if theta > -20:
            theta -= speed
        else:
            state = 1

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

def hinge():
    glColor3f(1,0,0)
    glLineWidth(6.0)
    glBegin(GL_POLYGON)
    glVertex2f(0,0)
    glVertex2f(-5, -10)
    glVertex2f(5,-10)
    glEnd()

def weights():
    xc1 = length*cos(radians(theta))
    yc1 = length*sin(radians(theta)) + 5
    xc2 = -length*cos(radians(theta))
    yc2 = -length*sin(radians(theta)) + 5
    glColor3f(1,1,0)
    glLineWidth(6)
    glBegin(GL_TRIANGLE_FAN)
    for i in range (0,360):
        glVertex2f(r*cos(radians(i))+xc1,r*sin(radians(i))+yc1)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    for i in range (0,360):
        glVertex2f(r*cos(radians(i))+xc2,r*sin(radians(i))+yc2)
    glEnd() 

def poly():
    global length,theta
    vertices1 = [
        [length+5,0],
        [length+5,5],
        [length-5,5],
        [length-5,0],
    ]
    vertices2 = [
        [-length+5,0],
        [-length+5,5],
        [-length-5,5],
        [-length-5,0],
    ]
    glColor3f(0,0,1)
    glLineWidth(1)
    glBegin(GL_POLYGON)
    for vertex in vertices1:
        glVertex2fv(rotated_points(vertex,theta))
    glEnd()
    glBegin(GL_POLYGON)
    for vertex in vertices2:
        glVertex2fv(rotated_points(vertex,theta))
    glEnd()


def cso():
    glColor3f(0,1,1)
    glLineWidth(3)
    glBegin(GL_LINES)
    x1 = length*cos(radians(theta))
    y1 = length*sin(radians(theta))
    x2 = -(length)*cos(radians(theta))
    y2 = -(length)*sin(radians(theta))
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    # glColor3f(1,1,1)
    # glLineWidth(2)
    # glBegin(GL_LINES)
    # glVertex2f(-100,-10)
    # glVertex2f(100,-10)
    # glEnd()
    cso()
    hinge()
    # weights()
    poly()
    glFlush()


def main():
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0,update,0)
    glutMainLoop()

main()