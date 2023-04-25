import numpy
import pygame
from pygame.locals import *

from bst import BinarySearchTree
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def tree():
    pygame.init()
    font = pygame.font.Font("arial.ttf", 20)
    text = font.render("50", True, (255, 255, 0))
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    pixels = pygame.image.tostring(text, "RGBA", True)
    print(pixels)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, text.get_width(), text.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, pixels)

    x = 200
    y = 200

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,0.0,1.0)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex2f(x, y)
    glTexCoord2f(1, 0)
    glVertex2f(x + text.get_width(), y)
    glTexCoord2f(1, 1)
    glVertex2f(x + text.get_width(), y + text.get_height())
    glTexCoord2f(0, 1)
    glVertex2f(x, y + text.get_height())
    glEnd()
    glutSwapBuffers()



def main():


    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    # glTranslatef(0.0, 0.0, -5.0)

    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(700, 700)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Mani_Dumaru_(15)_Mini_Project")
    gluOrtho2D(0.0,700.0,0.0,700.0)
    size = numpy.ndarray.tolist(glGetIntegerv(GL_VIEWPORT))
    size = size[2],size[3]
    print(f"Your Window Resolution is: {size}")
    glutDisplayFunc(tree)
    glutMainLoop()

main()
