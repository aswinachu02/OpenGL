from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import *

theta = 0
Speed = 1

def init():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500,500)
    glutCreateWindow("Saneesh")
    glClearColor(0,0,0,0)
    gluOrtho2D(-200,200,-200,200)


def update(n):
    global theta,Speed

    theta += Speed 
    if theta == 30:
        Speed = -Speed
    elif theta == -30:
        Speed = -Speed
    glutTimerFunc(int(1000/60),update,0)
    glutPostRedisplay()

def snowman():
    r1 = 50 
    r2 = 40
    r3 = 25
    glColor3f(1,1,1)
    glLineWidth(3)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0,360):
        glVertex2f(r1*cos(radians(i)),r1*sin(radians(i)))
    glEnd()

    glColor3f(1,1,1)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0,360):
        glVertex2f(r2*cos(radians(i)),r2*sin(radians(i))+70)
    glEnd()

def snowmanhead():
    r3 = 25
    glColor3f(1,1,1)
    glPointSize(3)
    glBegin(GL_POINTS)
    for i in range (0,r3):
        for j in range(0,46):
            print(j)
            x = i*cos(radians(j))
            y = i*sin(radians(j))
            glVertex2f(x,y+125)
            glVertex2f(-x,y+125)
            glVertex2f(x,-y+125)
            glVertex2f(-x,-y+125)
            glVertex2f(y,x+125)
            glVertex2f(y,-x+125)
            glVertex2f(-y,x+125)
            glVertex2f(-y,-x+125)
    glEnd()

def kai():
    glColor3f(0,1,1)
    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex2f(0,70)
    x = (110)*cos(radians(theta))
    y = (110)*sin(radians(theta))+70
    glVertex2f(-x,y)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(0,70)
    glVertex2f(x,y)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    kai()
    snowman()
    snowmanhead()
    glFlush()

def main():
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0,update,0)
    glutMainLoop()

main()