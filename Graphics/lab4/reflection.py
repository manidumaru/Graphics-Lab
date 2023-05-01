
import numpy

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

triangle = ((200,350), (400, 300), (300,500))

def reflection():
    matrixX = numpy.array([[1,0,0], [0,-1,0], [0, 0, 1]])
    matrixY = numpy.array([[-1,0,0], [0,1,0], [0, 0, 1]])
    matrix_origin = numpy.array([[-1,0,0], [0,-1,0], [0, 0, 1]])
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,1.0,1.0)
    glPointSize(2)
    glBegin(GL_TRIANGLES)
    for vertex in triangle:
        glVertex2f(vertex[0]/1000, vertex[1]/1000)
    glEnd()  

    reflectedX = []
    reflectedY = []
    for vertex in triangle:
        c_matrix = numpy.array([[vertex[0]/1000, vertex[1]/1000, 1]])
        initial_coordinates = c_matrix.reshape(3,1)
        product = numpy.matmul(matrixX, initial_coordinates)
        reflectedX.append((product[0], product[1]))
        print(reflectedX)
    glColor3f(1.0,1.0,0.0)
    glBegin(GL_TRIANGLES)
    for vertex in reflectedX:
        glVertex2f(vertex[0], vertex[1])
    glEnd()  

    for vertex in triangle:
        c_matrix = numpy.array([[vertex[0]/1000, vertex[1]/1000, 1]])
        initial_coordinates = c_matrix.reshape(3,1)
        product = numpy.matmul(matrixY, initial_coordinates)
        reflectedY.append((product[0], product[1]))
        print(reflectedY)
    
    glBegin(GL_TRIANGLES)
    for vertex in reflectedY:
        glVertex2f(vertex[0], vertex[1])
    glEnd() 
    
    ##################################### AXIS ###########################################
    glColor3f(0.0,1.0,1.0)
    x = 0
    while(x <= 1):
        glBegin(GL_POINTS)
        glVertex2f(x,0)
        glVertex(-x,0)
        glEnd()
        x += 0.001
    y = 0
    while(y <= 1):
        glBegin(GL_POINTS)
        glVertex2f(0,y)
        glVertex(0,-y)
        glEnd()
        y += 0.001
    glFlush()



def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(650, 650)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Mani_Dumaru_(15)_Lab4_reflection")
    size = numpy.ndarray.tolist(glGetIntegerv(GL_VIEWPORT))
    size = size[2],size[3]
    print(f"Your Window Resolution is: {size}")
    glutDisplayFunc(reflection)
    glutMainLoop()

main()