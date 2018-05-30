import pyglet
import math
import numpy
class hexagonClass:
    def __init__(self, ID, color, xcenter, ycenter, rad):
        """ initialize a triangle """
        self.ID = ID
        self.color = color
        self.x = xcenter
        self.y = ycenter
        self.radius = rad
        self.xvelocity = 0
        self.yvelocity = 0
        self.vertices = [0.0] * 12
        self.thetaIncrement = 0
        self.theta = 0

    def setCentreCoordinates(self, xcenter, ycenter):
        """ set the x,y coordinates """
        self.x = xcenter
        self.y = ycenter
    def getColor(self):
        """ return the color  """
        return self.color
    def getRadius(self):
        """ return the radius """
        return self.radius
    def getX(self):
        """ return the x coordinate  """
        return self.x
    def getY(self):
        """ return the y coordinate  """
        return self.y
    def getVertices(self):
        """convert the vertices list to pyGlet vertices format for the first triangle & return this list"""
        numberOfVertices = 6
        vertexList = pyglet.graphics.vertex_list(numberOfVertices, ('v2f', self.vertices))
        return vertexList
    def updateVertices(self):
        """ function which calculates the vertex list required to draw an equilateral triangle """
        numberOfVertices = 6 # specify the number of vertices we need for the shape
        vertices = []  # initialize a list of vertices
        for i in range(0, numberOfVertices):
            angle = i * (2.0 / 6.0) * math.pi  # specify a vertex of the triangle (x,y values)
            x = self.radius * math.cos(angle) + self.x
            y = self.radius * math.sin(angle) + self.y
            self.vertices[2*i]   = x    # append the x value to the vertex list
            self.vertices[2*i+1] = y  # append the y value to the vertex list
    def setVelocity(self,xvel,yvel):
        """set the x & y velocity components"""
        self.xvelocity = xvel
        self.yvelocity = yvel
    def updateCoordinates(self,windowWidth,windowHeight):

        if ((self.x + self.xvelocity > windowWidth) or (self.x + self.xvelocity < 0)):
            self.xvelocity = -1*self.xvelocity

        if ((self.y + self.yvelocity > windowHeight) or (self.y + self.yvelocity < 0)):
            self.yvelocity = -1*self.yvelocity

        self.x = self.x + self.xvelocity
        self.y = self.y + self.yvelocity


    def rotateVertices(self):
        #function that translates a set of coordinates to some origin & then rotates them
        c = numpy.array([[self.vertices[0] - self.x,self.vertices[1] - self.y],
                         [self.vertices[2] - self.x,self.vertices[3] - self.y],
                         [self.vertices[4] - self.x,self.vertices[5] - self.y],
                         [self.vertices[6] - self.x,self.vertices[7] - self.y],
                         [self.vertices[8] - self.x,self.vertices[9] - self.y],
                         [self.vertices[10] - self.x,self.vertices[11] - self.y]])

        theta = (self.theta / 180.) * numpy.pi
        rotMatrix = numpy.array([[numpy.cos(theta), -numpy.sin(theta)],
                                 [numpy.sin(theta), numpy.cos(theta)]])

        c = numpy.matmul(c,rotMatrix)

        self.vertices = [c[0][0] + self.x,c[0][1] + self.y,
                         c[1][0] + self.x,c[1][1] + self.y,
                         c[2][0] + self.x,c[2][1] + self.y,
                         c[3][0] + self.x,c[3][1] + self.y,
                         c[4][0] + self.x,c[4][1] + self.y,
                         c[5][0] + self.x,c[5][1] + self.y
                         ]

    def setThetaIncrement(self,value):
        self.thetaIncrement = value

    def updateTheta(self):
        self.theta = self.theta + self.thetaIncrement
