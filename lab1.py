# Mani Dumaru
# Roll no: 15
# CE-2019
# Computer Graphics Lab-1

import math
import numpy

from sympy import symbols, Eq, solve
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

theta_range = numpy.arange(0.0, 360, 0.5)

sun_triangles = []

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
    r = 0.07
    for i in theta_range:   
        theta = 2 * 3.1415926 * float(i) / float(360)
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        glVertex2f((x + cx), (y + cy))
        if (i % 22.5 == 0):
            sun_triangles.append((x,y))
    glEnd()
    ############### Sun Triangles #################
    glBegin(GL_TRIANGLES)
    hyp = 0.035
    x3, y3 = symbols('x3 y3')
    for i in range(0, len(sun_triangles)):
        if (i < len(sun_triangles)-1):
            A = sun_triangles[i]
            B = sun_triangles[i+1]
        elif (i == len(sun_triangles)-1):
            A = sun_triangles[i]
            B = sun_triangles[0]

        x1 = A[0]
        y1 = A[1]
        x2 = B[0]
        y2 = B[1]
        
        eq1 = Eq(pow(hyp,2) - pow((x3-x1),2) - pow((y3-y1),2))
        eq2 = Eq(pow(hyp,2) - pow((x3-x2),2) - pow((y3-y2),2))
        result = solve((eq1, eq2), (x3, y3))
        result1 = result[0]
        result2 = result[1]

        if(x1 <= 0 and x2 <= 0):
            C = result1
        else:
            C = result2
        
        if(i == 4):
            C = result1
        print(C)
        a = C[0]
        b = C[1]
        glVertex2f(x1+cx,y1+cy)
        glVertex2f(x2+cx,y2+cy)
        glVertex2f(a+cx,b+cy)
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
