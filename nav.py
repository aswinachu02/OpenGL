from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

b_centre = [500, 500]
b_rad = 75
speed=5

def init():
    glutInitDisplayMode(GLUT_RGB)
    glutInit()
    glutInitWindowSize(1024, 768)
    glutCreateWindow("O/P")
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(0, 1024, 768, 0)


def plot_ball():
    glPointSize(3.0)
    glColor3f(1.0, 0, 0)
    glBegin(GL_POINTS)
    #plotting ball weird method
    for i in range(46):
        x = b_rad * cos(radians(i))
        y = b_rad * sin(radians(i))
        glVertex2f(b_centre[0] + x, b_centre[1] + y)
        glVertex2f(b_centre[0] + y, b_centre[1] + x)
        glVertex2f(b_centre[0] + x, b_centre[1] - y)
        glVertex2f(b_centre[0] - x, b_centre[1] + y)
        glVertex2f(b_centre[0] - y, b_centre[1] - x)
        glVertex2f(b_centre[0] - x, b_centre[1] - y)
        glVertex2f(b_centre[0] - y, b_centre[1] + x)
        glVertex2f(b_centre[0] + y, b_centre[1] - x)
    glEnd()


def disp():
    glClear(GL_COLOR_BUFFER_BIT)
    plot_ball()

    glFlush()


def animator(x):
    global b_centre,speed
    
    if b_centre[1] == 650:
        speed=-5
    if b_centre[1]==500:
        speed=5 
    b_centre[1] = b_centre[1] + speed
    glutTimerFunc(50, animator, 0)
    glutPostRedisplay()


def main():
    init()
    glutDisplayFunc(disp)
    glutTimerFunc(0, animator, 0)
    glutMainLoop()


main()