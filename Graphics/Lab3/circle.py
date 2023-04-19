import numpy
import math

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# center = (0.1, 0.1)
radius = 0.4
stepSize = 0.01

def circleMidPoint():
    glClear(GL_COLOR_BUFFER_BIT)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,1.0,1.0)
    glPointSize(3)
    x = 0
    y = radius

    while(x<=y):
        plot(x,y)
        x = x + stepSize
        fv = (pow(x,2) + pow((y-(0.01/2)),2) - pow(radius,2))
        # print(x, y, fv)

        if(fv < 0):
            # print("fv thulo xa")
            y = y - stepSize

    glFlush()
    
def plot(x,y):
    print(x,y)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()
    

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(650, 650)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Mani_Dumaru_(15)_Lab3_MidPoint_Algorithm")
    size = numpy.ndarray.tolist(glGetIntegerv(GL_VIEWPORT))
    size = size[2],size[3]
    print(f"Your Window Resolution is: {size}")
    glutDisplayFunc(circleMidPoint)
    glutMainLoop()

main()