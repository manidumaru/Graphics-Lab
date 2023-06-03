from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
from math import sin, cos, pi
import numpy as np


def Actual(p1, p2, p3,p4,p5,p6,p7,p8):
    glPointSize(3.0)
    glBegin(GL_QUADS)

    # LEFT
    glColor3f(0.134, 0.167, 0.29)
    glVertex3d(p1[0],p1[1],p1[2])
    glVertex3d(p2[0],p2[1],p2[2])
    glVertex3d(p3[0],p3[1],p3[2])
    glVertex3d(p4[0],p4[1],p4[2])
 
    # BOTTOM
    glColor3f(0.68, 0.87, 0.378)
    glVertex3d(p1[0],p1[1],p1[2])
    glVertex3d(p5[0],p5[1],p5[2])
    glVertex3d(p6[0],p6[1],p6[2])
    glVertex3d(p2[0],p2[1],p2[2])
    # BACK

    glColor3f(0.988, 0.211, 0.67)
    glVertex3d(p1[0],p1[1],p1[2])
    glVertex3d(p5[0],p5[1],p5[2])
    glVertex3d(p8[0],p8[1],p8[2])
    glVertex3d(p4[0],p4[1],p4[2])

    # TOP
    glColor3f(0.104, 0.232, 0.123)
    glVertex3d(p3[0],p3[1],p3[2])
    glVertex3d(p4[0],p4[1],p4[2])
    glVertex3d(p8[0],p8[1],p8[2])
    glVertex3d(p7[0],p7[1],p7[2])
    #FRONT
    glColor3f(0.89,0.49,0.06)
    glVertex3d(p2[0],p2[1],p2[2])
    glVertex3d(p3[0],p3[1],p3[2])
    glVertex3d(p7[0],p7[1],p7[2])
    glVertex3d(p6[0],p6[1],p6[2])
       # RIGHT

    glColor3f(0.334,0.61,0.96)
    glVertex3d(p5[0],p5[1],p5[2])
    glVertex3d(p6[0],p6[1],p6[2])
    glVertex3d(p7[0],p7[1],p7[2])
    glVertex3d(p8[0],p8[1],p8[2])


    glEnd()

def Translation(p1, p2, p3,p4,p5,p6,p7,p8, Tr):
    matrix= np.array([
        [p1[0], p2[0], p3[0], p4[0],p5[0], p6[0], p7[0], p8[0]],
        [p1[1], p2[1], p3[1], p4[1],p5[1], p6[1], p7[1], p8[1]],
        [p1[2], p2[2], p3[2], p4[2],p5[2], p6[2], p7[2], p8[2]],
                      [1,1,1,1,1,1,1,1]])

    Tr= np.array([
    [1,0,0,Tr[0]],
    [0,1,0,Tr[1]],
    [0,0,1,Tr[2]],
    [0,0,0,1]
])
    mul= np.matmul(Tr, matrix)
    p1d=(round(float(mul[0][0]),2),round(float(mul[1][0]),2),round(float(mul[2][0]),2))
    p2d=(round(float(mul[0][1]),2),round(float(mul[1][1]),2),round(float(mul[2][1]),2))
    p3d=(round(float(mul[0][2]),2),round(float(mul[1][2]),2),round(float(mul[2][2]),2))
    p4d=(round(float(mul[0][3]),2),round(float(mul[1][3]),2),round(float(mul[2][3]),2))
    p5d=(round(float(mul[0][4]),2),round(float(mul[1][4]),2),round(float(mul[2][4]),2))
    p6d=(round(float(mul[0][5]),2),round(float(mul[1][5]),2),round(float(mul[2][5]),2))
    p7d=(round(float(mul[0][6]),2),round(float(mul[1][6]),2),round(float(mul[2][6]),2))
    p8d=(round(float(mul[0][7]),2),round(float(mul[1][7]),2),round(float(mul[2][7]),2))


    Actual(p1d, p2d, p3d,p4d,p5d,p6d,p7d,p8d) 
def Scaling(p1, p2, p3,p4,p5,p6,p7,p8, Sx,Sy,Sz, RefPoint):
    matrix= np.array([
        [p1[0], p2[0], p3[0], p4[0],p5[0], p6[0], p7[0], p8[0]],
        [p1[1], p2[1], p3[1], p4[1],p5[1], p6[1], p7[1], p8[1]],
        [p1[2], p2[2], p3[2], p4[2],p5[2], p6[2], p7[2], p8[2]],
                      [1,1,1,1,1,1,1,1]])

    Sc= np.array([
    [Sx,0,0,(1-Sx)*RefPoint[0]],
    [0,Sy,0,(1-Sy)*RefPoint[1]],
    [0,0,Sz,(1-Sz)*RefPoint[2]],
    [0,0,0,1]
])
    mul= np.matmul(Sc, matrix)
    p1d=(round(float(mul[0][0]),2),round(float(mul[1][0]),2),round(float(mul[2][0]),2))
    p2d=(round(float(mul[0][1]),2),round(float(mul[1][1]),2),round(float(mul[2][1]),2))
    p3d=(round(float(mul[0][2]),2),round(float(mul[1][2]),2),round(float(mul[2][2]),2))
    p4d=(round(float(mul[0][3]),2),round(float(mul[1][3]),2),round(float(mul[2][3]),2))
    p5d=(round(float(mul[0][4]),2),round(float(mul[1][4]),2),round(float(mul[2][4]),2))
    p6d=(round(float(mul[0][5]),2),round(float(mul[1][5]),2),round(float(mul[2][5]),2))
    p7d=(round(float(mul[0][6]),2),round(float(mul[1][6]),2),round(float(mul[2][6]),2))
    p8d=(round(float(mul[0][7]),2),round(float(mul[1][7]),2),round(float(mul[2][7]),2))


    Actual(p1d, p2d, p3d,p4d,p5d,p6d,p7d,p8d) 

def Rotation(p1, p2, p3,p4,p5,p6,p7,p8, axis, theta):
    theta=theta * pi/180
    matrix= np.array([
        [p1[0], p2[0], p3[0], p4[0],p5[0], p6[0], p7[0], p8[0]],
        [p1[1], p2[1], p3[1], p4[1],p5[1], p6[1], p7[1], p8[1]],
        [p1[2], p2[2], p3[2], p4[2],p5[2], p6[2], p7[2], p8[2]],
                      [1,1,1,1,1,1,1,1]])

    if axis=="X":
        Rot= np.array([
        [1,0,0,0],
        [0,cos(theta),-sin(theta),0],
        [0,sin(theta),cos(theta),0],
        [0,0,0,1]
    ])
    elif axis=="Y":
        Rot= np.array([
        [cos(theta),0,sin(theta),0],
        [0,1,0,0],
        [-sin(theta),0,cos(theta),0],
        [0,0,0,1]
    ])
    elif axis=="Z":
        Rot= np.array([
        [cos(theta),-sin(theta),0,0],
        [sin(theta),cos(theta),0,0],
        [0,0,1,0],
        [0,0,0,1]
    ])
    else:
        pass
    mul= np.matmul(Rot, matrix)
    p1d=(round(float(mul[0][0]),2),round(float(mul[1][0]),2),round(float(mul[2][0]),2))
    p2d=(round(float(mul[0][1]),2),round(float(mul[1][1]),2),round(float(mul[2][1]),2))
    p3d=(round(float(mul[0][2]),2),round(float(mul[1][2]),2),round(float(mul[2][2]),2))
    p4d=(round(float(mul[0][3]),2),round(float(mul[1][3]),2),round(float(mul[2][3]),2))
    p5d=(round(float(mul[0][4]),2),round(float(mul[1][4]),2),round(float(mul[2][4]),2))
    p6d=(round(float(mul[0][5]),2),round(float(mul[1][5]),2),round(float(mul[2][5]),2))
    p7d=(round(float(mul[0][6]),2),round(float(mul[1][6]),2),round(float(mul[2][6]),2))
    p8d=(round(float(mul[0][7]),2),round(float(mul[1][7]),2),round(float(mul[2][7]),2))


    Actual(p1d, p2d, p3d,p4d,p5d,p6d,p7d,p8d) 

def threeDimension():
    glClear(GL_DEPTH_BUFFER_BIT)
    p1=(5,5,0)
    p2=(5,5,5)   
    p3=(5,10,5)
    p4=(5,10,0)
    p5=(10,5,0)
    p6=(10,5,5)
    p7=(10,10,5)
    p8=(10,10,0)
    
    glPointSize(1.0)

    glRotatef(-25,1,0,0)
    glRotatef(25,0,1,0) 
    glEnable(GL_DEPTH_TEST)

    Actual(p1,p2,p3,p4,p5,p6,p7,p8)
    Tr=(-15,-15,0)
    Translation(p1, p2, p3,p4,p5,p6,p7,p8, Tr)
    Sx,Sy,Sz=1.4,1.4,1.4
    RefPoint=(35,10,0)
    Scaling(p1, p2, p3,p4,p5,p6,p7,p8, Sx,Sy,Sz, RefPoint)
    axis="Z"
    theta=-95
    Rotation(p1, p2, p3,p4,p5,p6,p7,p8, axis, theta)

  
    glFlush()
    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_ALPHA)
    glutInitWindowSize(620, 620)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("3d transformation")
    glOrtho(-15,15,-15,15,-15,15)
    glutDisplayFunc(threeDimension)
    glutMainLoop()


main()
