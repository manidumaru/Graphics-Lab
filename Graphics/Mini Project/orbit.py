
from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import * 
import time, math, data

def display(planet, x, y, z):
    glColor3f(x,y,z)
    glBegin(GL_TRIANGLE_FAN)
    r = planet["radius"]
    for i in range(0,360):   
        theta = 3.1415926 * float(i) / float(180)
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        position_x = x + planet["x"]
        position_y = y + planet["y"]
        glVertex2f(position_x , position_y)
    glEnd()
    glFlush()

def displacement_calculator(planet):
    force_e = (data.G * data.sun["mass"] * planet["mass"]) / (planet["distance"] * 10**9) **2
    theta = math.atan2(planet["y"], planet["x"])
    angle = theta * (180/math.pi)
    if (angle > 0):
        fx = -force_e * math.cos(theta)
    else:
        fx = force_e * math.cos(theta)
        fx *= -1
    fy = force_e * math.sin(-theta)
    velX = (fx * data.timestep) / planet["mass"]
    velY = (fy * data.timestep) / planet["mass"]
    planet["vx"] += velX
    planet["vy"] += velY
    dx = (planet["vx"] * data.timestep) / 10**9
    dy = (planet["vy"] * data.timestep) / 10**9

    return dx, dy

def draw():
    counter = 0
    while(True):
        glClear(GL_COLOR_BUFFER_BIT)
        display(data.sun, 0.98, 0.83, 0.25)
        display(data.mercury,0.81, 0.86, 0.83)
        display(data.venus, 0.64, 0.48, 0.105)
        display(data.earth, 0.42, 0.58, 0.84)
        display(data.mars, 0.75, 0.26, 0.055)
        display(data.jupiter, 0.84, 0.79, 0.61)

        mercury_displacement = displacement_calculator(data.mercury)
        data.mercury["x"] += mercury_displacement[0]
        data.mercury["y"] += mercury_displacement[1]  

        venus_displacement = displacement_calculator(data.venus)
        data.venus["x"] += venus_displacement[0]
        data.venus["y"] += venus_displacement[1]

        earth_displacement = displacement_calculator(data.earth)
        data.earth["x"] += earth_displacement[0]
        data.earth["y"] += earth_displacement[1]

        mars_displacement = displacement_calculator(data.mars)
        data.mars["x"] += mars_displacement[0]
        data.mars["y"] += mars_displacement[1]

        jupiter_displacement = displacement_calculator(data.jupiter)
        data.jupiter["x"] += jupiter_displacement[0]
        data.jupiter["y"] += jupiter_displacement[1]

        ################################################################# Tracing Earth Path ##################################################################
        # earth_position = (data.earth["x"], data.earth["y"])
        # if counter % 45 == 0:
        #     data.earth_route.append(earth_position)
        # counter += 1
        # if (len(data.earth_route) > 8):
        #     data.earth_route.pop()
        # for position in data.earth_route:
        #     glColor3f(0.419,0.576,0.839)
        #     glPointSize(2)
        #     glBegin(GL_POINTS)
        #     glVertex2f(position[0], position[1])
        #     glEnd()
        #     glFlush()

        glutSwapBuffers()
        time.sleep(0.01)
        

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(1500, 750)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Mani_Dumaru_(15)_Orbit_Simulation")
    gluOrtho2D(-800.0,800.0,-375.0,375.0)
    glutDisplayFunc(draw)
    glutMainLoop()

main()