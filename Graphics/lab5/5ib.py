from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


windowSize = (500, 500)


def Plot(x, y, g):
    if g == 'p':

        glColor3f(0.0, 1.0, 1.0)
        glPointSize(3.0)
    else:
        glColor3f(1.0, 1.0, 0.0)
        glPointSize(5.0)

    glBegin(GL_POINTS)

    glVertex2f(x, y)
    glEnd()




def Window(Wp1, Wp2, Wp3, Wp4):
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(3.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(Wp1[0], Wp1[1] )
    glVertex2f(Wp2[0], Wp2[1] )
    glVertex2f(Wp3[0], Wp3[1] )
    glVertex2f(Wp4[0], Wp4[1] )
    glEnd()



def Polygon(V, c=""):    
    glColor3f(1.0, .0, .0)     
    if c=="b":
        glColor3f(1.0, 1.0, 0.0)  
    glPointSize(3.0)
    glBegin(GL_LINE_LOOP)

    for point in V:
        glVertex2f(point[0],point[1])
  
    glEnd()
def LeftClip(x1,y1,x2,y2,c,xwmin,m):
    if x1 <xwmin and x2>=xwmin:
            x=xwmin
            y=y1+m*(x-x1)
            c.append((x,y))
            c.append((x2,y2))
    if x1 >=xwmin and x2>=xwmin:
        
        c.append((x1,y1))
        c.append((x2,y2))
    if x1 >=xwmin and x2<xwmin:
        
        x=xwmin
        y=y1+m*(x-x1)
        c.append((x1,y1))
        c.append((x,y))
    else:
        pass
    return c

def RightClip(x1,y1,x2,y2,c,xwmax,m):
    if x1 <=xwmax and x2>xwmax:
            x=xwmax
            y=y1+m*(x-x1)
            c.append((x1,y1))
            c.append((x,y))
    if x1 <=xwmax and x2<=xwmax:
        
        c.append((x1,y1))
        c.append((x2,y2))
    if x1 >xwmax and x2<=xwmax:
        
        x=xwmax
        y=y1+m*(x-x1)
        c.append((x,y))
        c.append((x2,y2))
    else:
        pass
    return c
def TopClip(x1,y1,x2,y2,c,ywmax,m):
    if y1 <=ywmax and y2>ywmax:
            y=ywmax
            x=(y-y1)/m + x1 if m!=0 else x1
            c.append((x1,y1))
            c.append((x,y))
    if y1 <=ywmax and y2<=ywmax:
        
        c.append((x1,y1))
        c.append((x2,y2))
    if y1 >ywmax and y2<=ywmax:
        
        y=ywmax
        x=(y-y1)/m + x1 if m!=0 else x1
        c.append((x,y))
        c.append((x2,y2))
    else:
        pass
    return c
def BottomClip(x1,y1,x2,y2,c,ywmin,m):
    if y1 >=ywmin and y2<ywmin:
            y=ywmin
            x=(y-y1)/m + x1 if m!=0 else x1
            c.append((x1,y1))
            c.append((x,y))
    if y1 >=ywmin and y2>=ywmin:
        
        c.append((x1,y1))
        c.append((x2,y2))
    if y1 <ywmin and y2>=ywmin:
        
        y=ywmin
        x=(y-y1)/m + x1 if m!=0 else x1
        c.append((x,y))
        c.append((x2,y2))
    else:
        pass
    return c
        

def Clip(V,xwmin,ywmin,xwmax,ywmax,j=0):
    c=[]
    if j ==4:
        Polygon(V,"b")
        return
    
    for i in range(0,len(V)):
        x1=V[i][0]
        y1=V[i][1]
        x2=V[(i+1) % len(V)][0]
        y2=V[(i+1) % len(V)][1]
        dely= y2-y1
        delx= x2-x1
        if delx!=0:
            m=dely/delx
        else:
            m=0
        if j==0:
            c=LeftClip(x1,y1,x2,y2,c,xwmin,m)
            print(c)
        if j==1:
            c=RightClip(x1,y1,x2,y2,c,xwmax,m)
        if j==2:
            c=TopClip(x1,y1,x2,y2,c,ywmax,m)
        if j==3:
            c=BottomClip(x1,y1,x2,y2,c,ywmin,m)
    s=c
    Clip(s,xwmin,ywmin,xwmax,ywmax,j+1)

def Triangle():
    Wp1=(-5,-5)
    Wp2= (-5,+5)
    Wp3= (5,5)
    Wp4=(5,-5)
    V=[(-8,-3),(3,6),(8,1)]
    
    Window(Wp1, Wp2, Wp3, Wp4) 
    Polygon(V)
    Clip(V,Wp1[0],Wp1[1],Wp3[0],Wp3[1])

    
    

   
def Transformations():
    glClear(GL_COLOR_BUFFER_BIT)
    Triangle()
    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(windowSize[0], windowSize[1])
    glutInitWindowPosition(600, 100)
    glutCreateWindow("Sutherland Hodgeman")
    glutDisplayFunc(Transformations)
    gluOrtho2D(-15,15,-15,15)
    glutMainLoop()


main()

