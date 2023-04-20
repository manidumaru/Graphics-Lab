import numpy

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

x = (0.5,0.5)
y = (0.7,0.7)

def DDA():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,1.0,0.0)
    glPointSize(3)
    i = 0
    while (i<=1):
        glBegin(GL_POINTS)
        glVertex2f(i,0)
        glVertex2f(-i,0)
        glVertex2f(0,i)
        glVertex2f(0,-i)
        i+=0.01
        glEnd()
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(650, 650)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Mani_Dumaru_(15)_Lab3_MidPoint_Algorithm")
    size = numpy.ndarray.tolist(glGetIntegerv(GL_VIEWPORT))
    size = size[2],size[3]
    print(f"Your Window Resolution is: {size}")
    glutDisplayFunc(DDA)
    glutMainLoop()

main()


