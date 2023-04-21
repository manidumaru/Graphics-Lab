import numpy

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def DDA():
    x1 = 126
    y1 = 267
    x2 = 306
    y2 = 410
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,1.0,0.0)
    glPointSize(3)

    slope = (y2-y1)/(x2-x1)
    print(slope)

    if (slope < 1):
        while(x1 != x2):
            glBegin(GL_POINTS)
            glVertex2f(x1,y1)
            glEnd()
            if (x1<x2):
                x1 += 1
                y1 += slope
            else:
                x1 -= 1
                y1 -= slope
            glFlush()
    else:
        while(y1 != y2):
            glBegin(GL_POINTS)
            glVertex2f(x1,y1)
            glEnd()
            if (x1<x2):
                y1 += 1
                x1 -= 1/slope
            else:
                y1 -= 1
                x1 -= 1/slope
            glFlush()
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Mani_Dumaru_(15)_Lab2_DDA")
    gluOrtho2D(0.0,500.0,0.0,500.0)
    size = numpy.ndarray.tolist(glGetIntegerv(GL_VIEWPORT))
    size = size[2],size[3]
    print(f"Your Window Resolution is: {size}")
    glutDisplayFunc(DDA)
    glutMainLoop()

main()


