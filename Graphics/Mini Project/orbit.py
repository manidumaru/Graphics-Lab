
from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import * 
import time 
import math
import numpy
    

G = 6.67 * 10**-11
AU = 1.496 * 10**11
timestep = 86400
earth_route = []

def velocity_calculator(sun, planet):
    force_e = (G * sun["mass"] * planet["mass"]) / (planet["distance"] * 10**9) **2
    theta = math.atan2(planet["y"], planet["x"])
    angle = theta * (180/math.pi)

    if (angle > 0):
        fx = -force_e * math.cos(theta)
    else:
        fx = force_e * math.cos(theta)
        fx *= -1
    fy = force_e * math.sin(-theta)
    velX = (fx * timestep) / planet["mass"]
    velY = (fy * timestep) / planet["mass"]
    return velX, velY

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    counter = 0
    sun = {
        "mass": 1.989 * 10**30,
        "radius": (6.96 * 10**5) * 1000,
        "x": 0,
        "y": 0
    }
    earth = {
        "mass": 5.97219 * 10**24,
        "radius": 6400 * 1000,
        "distance": 149.6,
        "x": AU / 10**9,
        "y": 0,
        "vy": 29.783 * 1000, # m/s
        "vx": 0
    }
    venus = {
        "mass": 4.867 * 10**24,
        "radius": 6051 * 1000,
        "distance": 104.7,
        "x": 0.7*AU / 10**9,
        "y": 0,
        "vy": 35.02 * 1000,
        "vx": 0
    } 
    mercury = {
        "mass": 3.285 * 10**23,
        "radius": 2439.7 * 1000,
        "distance": 59.84,
        "x": 0.4*AU / 10**9,
        "y": 0,
        "vy": 47.36 * 1000,
        "vx": 0
    } 
    
    mars = {
        "mass": 6.39 * 10**23,
        "radius": 3389.5 * 1000,
        "distance": 224.4,
        "x": 1.5*AU / 10**9,
        "y": 0,
        "vy": 24.08 * 1000,
        "vx": 0
    } 



    while(True):
        glClear(GL_COLOR_BUFFER_BIT) 
        ################# Sun ####################
        glColor3f(1.0,1.0,0.0)
        glLineWidth(2)
        glBegin(GL_TRIANGLE_FAN)
        r = 17
        for i in range(0,360):   
            theta = 3.1415926 * float(i) / float(180)
            x = r * math.cos(theta)
            y = r * math.sin(theta)
            glVertex2f(x, y)
        glEnd()
        glFlush()
        ################# Mercury ####################
        glColor3f(0.905,0.910,0.940)
        glLineWidth(2)
        glBegin(GL_TRIANGLE_FAN)
        r = mercury["radius"] / 10**6
        for i in range(0,360):   
            theta = 3.1415926 * float(i) / float(180)
            x = r * math.cos(theta)
            y = r * math.sin(theta)
            pox = x + mercury["x"]
            poy = y + mercury["y"]
            glVertex2f(pox , poy)
        glEnd()
        glFlush()
        ################# Venus ####################
        glColor3f(0.647,0.486,0.105)
        glLineWidth(2)
        glBegin(GL_TRIANGLE_FAN)
        r = venus["radius"] / 10**6
        for i in range(0,360):   
            theta = 3.1415926 * float(i) / float(180)
            x = r * math.cos(theta)
            y = r * math.sin(theta)
            pox = x + venus["x"]
            poy = y + venus["y"]
            glVertex2f(pox , poy)
        glEnd()
        glFlush()
        ################# Earth ####################
        glColor3f(0.419,0.576,0.839)
        glLineWidth(2)
        glBegin(GL_TRIANGLE_FAN)
        r = earth["radius"] / 10**6
        for i in range(0,360):   
            theta = 3.1415926 * float(i) / float(180)
            x = r * math.cos(theta)
            y = r * math.sin(theta)
            pox = x + earth["x"]
            poy = y + earth["y"]
            glVertex2f(pox , poy)
        glEnd()
        glFlush()
        ################# mars ####################
        glColor3f(0.756,0.266,0.054)
        glLineWidth(2)
        glBegin(GL_TRIANGLE_FAN)
        r = mars["radius"] / 10**6
        for i in range(0,360):   
            theta = 3.1415926 * float(i) / float(180)
            x = r * math.cos(theta)
            y = r * math.sin(theta)
            pox = x + mars["x"]
            poy = y + mars["y"]
            glVertex2f(pox , poy)
        glEnd()
        glFlush()

        mercury_velocity = velocity_calculator(sun, mercury)
        mercury["vy"] += mercury_velocity[1]
        mercury["vx"] += mercury_velocity[0]
        dx = (mercury["vx"] * timestep) / 10**9
        dy = (mercury["vy"] * timestep) / 10**9

        mercury["x"] += dx
        mercury["y"] += dy

        venus_velocity = velocity_calculator(sun, venus)
        venus["vy"] += venus_velocity[1]
        venus["vx"] += venus_velocity[0]
        dx = (venus["vx"] * timestep) / 10**9
        dy = (venus["vy"] * timestep) / 10**9

        venus["x"] += dx
        venus["y"] += dy

        earth_velocity = velocity_calculator(sun, earth)
        earth["vy"] += earth_velocity[1]
        earth["vx"] += earth_velocity[0]
        dx = (earth["vx"] * timestep) / 10**9
        dy = (earth["vy"] * timestep) / 10**9

        earth["x"] += dx
        earth["y"] += dy

        earth_position = (earth["x"], earth["y"])
        if counter % 30 == 0:
            earth_route.append(earth_position)
        counter += 1
        if (len(earth_route) > 12):
            earth_route.clear()
        for position in earth_route:
            glColor3f(1.0,1.0,1.0)
            glPointSize(2)
            glBegin(GL_POINTS)
            glVertex2f(position[0], position[1])
            glEnd()
            glFlush()

        mars_velocity = velocity_calculator(sun, mars)
        mars["vy"] += mars_velocity[1]
        mars["vx"] += mars_velocity[0]
        dx = (mars["vx"] * timestep) / 10**9
        dy = (mars["vy"] * timestep) / 10**9

        mars["x"] += dx
        mars["y"] += dy
        glutSwapBuffers()
        time.sleep(0.01)
        

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(800, 800)
    glutInitWindowPosition(450, 20)
    glutCreateWindow("Mani_Dumaru_(15)_Lab3_Ellipse_MidPoint")
    gluOrtho2D(-350.,350.0,-350.0,350.0)
    size = numpy.ndarray.tolist(glGetIntegerv(GL_VIEWPORT))
    size = size[2],size[3]
    print(f"Your Window Resolution is: {size}")
    glutDisplayFunc(draw)
    glutMainLoop()

main()