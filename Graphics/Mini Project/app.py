from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import * 
import numpy as np 
import time 
 
 
def draw_point(x, y,rx, ry): 
    glPointSize(5.0) 
    glBegin(GL_POINTS) 
    glColor3f(0.0, 1.0, 1.0) 
    glVertex2f(x+rx, y+ry) 
    glEnd() 

def draw_Sun(x,y):
    glPointSize(10.0) 
    glBegin(GL_POINTS) 
    glColor3f(1.0, 1.0, 0.0) 
    glVertex2f(x, y) 
    glEnd() 
 
 
def main(): 
    # Set up PyOpenGL environment 
    glutInit() 
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB) 
    glutInitWindowSize(700, 700) 
    glutInitWindowPosition(200, 50)
    glutCreateWindow("Animating a Point in PyOpenGL") 
    # Set up viewport 
    # glViewport(0, 0, 800, 600) 
    glMatrixMode(GL_PROJECTION) 
    # glLoadIdentity() 
    gluOrtho2D(0.0,800.0,0.0,800.0)
    glMatrixMode(GL_MODELVIEW) 
    glLoadIdentity() 
    # Set initial position of point 
    r_x = 350
    r_y = 350
    x = 0
    y = 350
    while True: 
        # Draw the point at its current position 
        p_k = r_y**2 - ((r_x**2) * r_y) + ((1/4)*r_x**2)

        while(x <= r_x and y >= 0):
            # Clear the screen 
            glClear(GL_COLOR_BUFFER_BIT) 
            draw_Sun(r_x,r_y)
            draw_point(x, y, r_x, r_y)
            

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
 
            # Swap the buffers to update the display 
            glutSwapBuffers() 
    
            # Sleep for a short time to control the animation speed 
            time.sleep(0.01) 
    
main()