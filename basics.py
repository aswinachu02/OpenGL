from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import cos,sin,radians

i=0
ar = []
def init():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500,500)
    glutCreateWindow("Ramesh")
    glClearColor(0,0,0,0)
    gluOrtho2D(-100,100,-100,100)


def pie_plot(r):
    global ar
    glPointSize(3)
    glBegin(GL_POINTS)
    j =0
    for i in range (0,360):
        # glColor3f(1-(j/(len(ar)+1)),(j/(len(ar)+1)),j/(len(ar)+1))
        glColor3f(cos(j),sin(j/2),0)
        if i >= ar[j]:
            j += 1
        glVertex2f(r*cos(radians(i)),r*sin(radians(i)))
    glEnd()

    
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    for i in range (0,30):
        pie_plot(i)
    glFlush()

def inputs():
    global ar
    n = int(input("Enter no.of categories: "))
    for i in range (0,n):
        ang = int(input("Enter percentage:"))
        angle = 0 if i == 0 else ar[i-1]  +  int(ang*360/100)
        ar.append(angle)
    ar.append(360)

def main():
    inputs()
    init()
    glutDisplayFunc(display)
    glutMainLoop()



main()