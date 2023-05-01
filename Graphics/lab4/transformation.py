
import numpy
import math

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

triangle = ((200,200), (250, 188), (261,250))

def transformation(operation, t_x = 100, t_y = 70):
    if operation == "translate":
        print(t_x, t_y)
        t_x = t_x
        t_y = t_y
        matrix = numpy.array([[1,0,t_x], [0,1,t_y], [0, 0, 1]])
    elif operation == "scale":
        s_x = 1.5
        s_y = 1.5
        matrix = numpy.array([[s_x,0,0], [0,s_y,0], [0, 0, 1]])
    elif operation == "rotate":
        theta = 20 * (math.pi/180)
        matrix = numpy.array([[math.cos(theta),-(math.sin(theta)),0], [math.sin(theta),math.cos(theta),0], [0, 0, 1]])
    elif operation == "shearX":
        ref = 200
        sh_x = 2
        matrix = numpy.array([[1,sh_x, -sh_x * ref], [0,1,0], [0, 0, 1]])
    elif operation == "shearY":
        ref = 200
        sh_y = 2
        matrix = numpy.array([[1,0,0], [sh_y,1,-sh_y * ref], [0, 0, 1]])


    translated = []
    for vertex in triangle:
        c_matrix = numpy.array([[vertex[0], vertex[1], 1]])
        initial_coordinates = c_matrix.reshape(3,1)
        product = numpy.matmul(matrix, initial_coordinates)
        translated.append((product[0], product[1]))
    
    print(translated)
    return translated

def transformations():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,1.0,1.0)

    glBegin(GL_TRIANGLES)
    for vertex in triangle:
        glVertex2f(vertex[0], vertex[1])
    glEnd()
    #### scale ####
    #### translate ####
    #### rotate ####
    #### shearX ####
    #### shearY ####
    transformed = transformation("shearY")
    print(f"result = {transformed}")
    glColor3f(1.0,1.0,0.0)
    glBegin(GL_TRIANGLES)
    for vertex in transformed:
        glVertex2f(vertex[0], vertex[1])
    glEnd()
    glFlush()
    glutSwapBuffers()



def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Mani_Dumaru_(15)_Lab4_2D_Transformation")
    gluOrtho2D(0.0,500.0,0.0,500.0)
    size = numpy.ndarray.tolist(glGetIntegerv(GL_VIEWPORT))
    size = size[2],size[3]
    print(f"Your Window Resolution is: {size}")
    glutDisplayFunc(transformations)
    glutMainLoop()

main()