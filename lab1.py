# Mani Dumaru
# Roll no: 15
# CE-2019
# Computer Graphics Lab-1

import math
import numpy

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def clearScreen():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-0.5,1.0,-0.5,1.0)

vertices1 = (
    (0.0,0.4),
    (0,0.8),
    (0.6,0.4),
) 

upper_vertices = (
    (-0.01,0.39),
    (-0.01,0.82),
    (0.63,0.39),
)

vertices2 = (
    (0.0,0.0),
    (0.0,0.55),
    (0.6,0.0),
)

lower_vertices = (
    (-0.01, -0.01),
    (-0.01, 0.57),
    (0.63,-0.01),
)

circle_moon = (
    (0.17, 0.535)
)

circle_sun = (
    (0.17, 0.18)
)

def flag():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,0.0,1.0)
    ############### Border Triangles ###################
    glBegin(GL_TRIANGLES)
    for vertex in upper_vertices:
        x = vertex[0]
        y = vertex[1]
        glVertex2f(x,y)
    glEnd()

    glBegin(GL_TRIANGLES)
    for vertex in lower_vertices:
        x = vertex[0]
        y = vertex[1]
        glVertex2f(x,y)
    glEnd()

    glColor3f(1.0,0.0,0.0)
    ################ Upper Triangle ##################
    glBegin(GL_TRIANGLES)
    for vertex in vertices1:
        x = vertex[0]
        y = vertex[1]
        glVertex2f(x,y)
    glEnd()
    ################ Lower Triangle ##################
    glBegin(GL_TRIANGLES)
    for vertex in vertices2:
        x = vertex[0]
        y = vertex[1]
        glVertex2f(x,y)
    glEnd()
    ################ Moon #################
    glColor3f(1.0,1.0,1.0)
    glLineWidth(2)
    glBegin(GL_TRIANGLE_FAN)
    cx = circle_moon[0]
    cy = circle_moon[1]
    r = 0.08
    for i in range(180,360):   
        theta = 3.1415926 * float(i) / float(180)
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        glVertex2f((x + cx), (y + cy))
    glEnd()
    glBegin(GL_TRIANGLE_FAN)
    cx = circle_moon[0]
    cy = circle_moon[1]
    r = 0.045
    for i in range(0,360):   
        theta = 3.1415926 * float(i) / float(360)
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        glVertex2f((x + cx), (y + cy))
    glEnd()
    ############### Sun #####################
    glBegin(GL_TRIANGLE_FAN)
    cx = circle_sun[0]
    cy = circle_sun[1]
    r = 0.08
    for i in range(0,360):   
        theta = 2 * 3.1415926 * float(i) / float(360)
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        glVertex2f((x + cx), (y + cy))
    glEnd()
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(650, 650)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Mani_Dumaru_(15)_Lab1_Nepal_Flag")
    size = numpy.ndarray.tolist(glGetIntegerv(GL_VIEWPORT))
    size = size[2],size[3]
    print(f"Your Window Resolution is: {size}")
    glutDisplayFunc(flag)
    clearScreen()
    glutMainLoop()

main()
