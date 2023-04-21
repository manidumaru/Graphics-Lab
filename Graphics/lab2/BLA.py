import numpy

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def BLA():
    x1 = 300
    y1 = 370
    x2 = 300
    y2 = 100
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,1.0,1.0)
    glPointSize(3)
    slope = (y2-y1)/(x2-x1)
    print(slope)
    c = y1 - (slope*x1)

    if (slope < 1):
        while(x1 != x2):
            glBegin(GL_POINTS)
            glVertex2f(x1,y1)
            glEnd()
            if (x1 < x2):
                x1 += 1
            else:
                x1 -= 1
            actual_y = (slope*x1) + c
            if (x1 > x2):
                d1 = y1 - actual_y
                d2 = actual_y - (y1-1)
                if(d1-d2 > 0):
                    y1 -= 1
            else:
                d1 = (y1+1) - actual_y
                d2 = actual_y - y1
                if((d1-d2) < 0):
                    y1 += 1
            glFlush()
    else:
        while(y1 != y2):
            glBegin(GL_POINTS)
            glVertex2f(x1,y1)
            glEnd()
            if(y1 > y2):
                y1 -= 1
            else:
                y1 += 1
            actual_x = (y1 - c)/slope
            if (y1 > y2):
                d1 = x1 - actual_x
                d2 = actual_x - (x1-1)
                if((d1-d2 > 0)):
                   x1 -= 1
            else:
                d1 = (x1+1) - actual_x
                d2 = actual_x - x1
                if((d1-d2) < 0):
                    x1 += 1
            glFlush()
    glutSwapBuffers()
    return

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
    glutDisplayFunc(BLA)
    glutMainLoop()

main()
