import numpy

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def ellipse():
    center = (250, 250)
    r_x = 80
    r_y = 50
    x = 0
    y = r_y
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,1.0,1.0)
    glPointSize(2)

    p_k = r_y**2 - ((r_x**2) * r_y) + ((1/4)*r_x**2)
    
    while(x <= r_x and y >= 0):
        print(x,y)
        glBegin(GL_POINTS)
        glVertex2f(x + center[0], y + center[1])
        glVertex2f(x + center[0], -y + center[1])
        glVertex2f(-x + center[0], y + center[1])
        glVertex2f(-x + center[0], -y + center[1])
        glEnd()
        glFlush()
        glutSwapBuffers()
        
        if (2*(r_y**2)*x < 2*(r_x**2)*y):
            x += 1
            if p_k < 0:
                p_k = p_k + (2* r_y**2 * x) + (r_y**2)
            else:
                y -= 1
                p_k = p_k + (2* r_y**2 * x) - (2* r_x**2 * y) + (r_y**2)
        else:
            y -= 1
            if p_k <= 0:
                x += 1
                p_k = p_k + (2* r_y**2 * x) - (2* r_x**2 * y) + (r_x**2)
            else:
                p_k = p_k - (2* r_x**2 * y) + (r_x**2)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Mani_Dumaru_(15)_Lab3_Ellipse_MidPoint")
    gluOrtho2D(0.0,500.0,0.0,500.0)
    size = numpy.ndarray.tolist(glGetIntegerv(GL_VIEWPORT))
    size = size[2],size[3]
    print(f"Your Window Resolution is: {size}")
    glutDisplayFunc(ellipse)
    glutMainLoop()

main()