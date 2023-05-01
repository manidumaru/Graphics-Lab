import numpy

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def circle():
    center = (250,250)
    radius = 70
    x = 0
    y = radius
    radius 
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,1.0,1.0)
    glPointSize(3)

    p_k = 1-radius
    while(x < y):
        glBegin(GL_POINTS)
        glVertex2f(x + center[0], y + center[1])
        glVertex2f(x + center[0], -y + center[1])
        glVertex2f(-x + center[0], y + center[1])
        glVertex2f(-x + center[0], -y + center[1])
        glVertex2f(y + center[1], x + center[0])
        glVertex2f(-y + center[1], x + center[0])
        glVertex2f(y + center[1], -x + center[0])
        glVertex2f(-y + center[1], -x + center[0])
        glEnd()
        x += 1
        if (p_k < 0):
            p_k = p_k + 2*x + 1
        else:
            y -= 1
            p_k = p_k + 2*x + 1 - 2*y
        glFlush()
        glutSwapBuffers()

    

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Mani_Dumaru_(15)_Lab3_Circle_MidPoint")
    gluOrtho2D(0.0,500.0,0.0,500.0)
    size = numpy.ndarray.tolist(glGetIntegerv(GL_VIEWPORT))
    size = size[2],size[3]
    print(f"Your Window Resolution is: {size}")
    glutDisplayFunc(circle)
    glutMainLoop()

main()