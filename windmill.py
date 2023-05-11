from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
import random
import time

RADIUS = 100
theta = 0
r = 25
xc=0
yc=0
height = 200
moonRadius = 25
moonxc = -150
moonyc = 150
rainx = 50
rainy = 200
rainy2 = 180


def init():
    glutInitDisplayMode(GLUT_RGB)
    glutInit()
    glutInitWindowSize(500,500)
    glutCreateWindow("Fan")
    glClearColor(0,0,0,0)
    gluOrtho2D(-200,200,-200,200)

def rotate(x):
    global theta, rainy, rainy2
    theta -= 1
    rainy -= 0.5
    rainy2 -= 0.5
    if rainy == -200:
        rainy = 200
        rainy2 = 180
    glutTimerFunc(int(1000/60), rotate, 0)
    glutPostRedisplay()

def getRotatedPoints(vertice, theta):
    return [
        round(
            vertice[0]*cos(radians(theta)) 
            - vertice[1]*sin(radians(theta))
        ),
        round(
            vertice[0]*sin(radians(theta)) 
            + vertice[1]*cos(radians(theta))
        ),
    ]

def circle():
    global r, xc, yc
    glColor3f(0,1,0)
    glBegin(GL_TRIANGLE_FAN)
    for i in range (0,361):
        x = r*cos(radians(i))+xc
        y = r*sin(radians(i))+yc 
        glVertex2f(x,y)
    glEnd()

def windMill():
    global height
    vertices = [
        [0,0],
        [-height/8, -height],
        [height/8, -height]
    ]
    glColor3f(1,0.5,0.3)
    glBegin(GL_POLYGON)
    for vertice in vertices:
        glVertex2fv(vertice)
    glEnd()

def moon():
    global moonRadius, moonxc, moonyc
    glColor3f(0.8,0.8,0.8)
    glBegin(GL_TRIANGLE_FAN)
    for i in range (361):
        x = moonRadius * cos(radians(i)) + moonxc
        y = moonRadius * sin(radians(i)) + moonyc
        glVertex2f(x, y)
    glEnd()

def rain(x,y):
    global rainx, rainy, rainy2
    glColor3f(0,0,0.8)
    glBegin(GL_LINES)
    glVertex2f(x, rainy - y)    
    glVertex2f(x, rainy2 - y)    
    glEnd()

def wings():
    global theta
    vertices = [
        [0,0],
        [-RADIUS/4, RADIUS],
        [RADIUS/4, RADIUS]
    ]
    glColor3f(0,1,1)
    glLineWidth(6.0)
    glBegin(GL_POLYGON)
    for vertice in vertices:
        glVertex2fv(getRotatedPoints(vertice, theta))
    for vertice in vertices:
        glVertex2fv(getRotatedPoints(vertice, theta + 120))
    for vertice in vertices:
        glVertex2fv(getRotatedPoints(vertice, theta + 240))
    glEnd()


def fan():
    glClear(GL_COLOR_BUFFER_BIT)
    for i in range(random.randint(0,40)):
        rain(random.randint(-200,200),random.randint(-100,100))
    windMill()
    wings()
    circle()
    moon()
    glFlush()


def main():
    init()
    glutDisplayFunc(fan)
    glutTimerFunc(0,rotate,0)
    glutMainLoop()

main()