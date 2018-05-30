import pyglet
import math
import numpy

class starClass:

    def __init__(self, ID, color, xcenter, ycenter, rad):
        """ initialize a star """
        self.ID = ID
        self.color = color
        self.x = xcenter
        self.y = ycenter
        self.radius = rad
        self.xvelocity = 0
        self.yvelocity = 0
        self.xaccn = 0
        self.yaccn = 0
        self.vertices = [0.0] * 20
        self.theta = 0
        self.thetaIncrement = 0
        self.kx = 1
        self.ky = 1

    def setCentreCoordinates(self,xcenter,ycenter):
        """ set the x,y coordinates of the star """
        self.x = xcenter
        self.y = ycenter

    def updateCentreCoordinates(self, width, height):
        """ updates the x,y coordinates of the star """

        if (( self.x + self.xvelocity > width) or (self.x + self.xvelocity < 0)):
            self.xvelocity *= -1
        if (( self.y + self.yvelocity > height) or (self.y + self.yvelocity < 0)):
            self.yvelocity *= -1

        self.x += self.xvelocity
        self.y += self.yvelocity

    def getColor(self):
        """ return the color of the star """
        return self.color

    def getRadius(self):
        """ return the radius of the star """
        return self.radius

    def getX(self):
        """ return the x coordinate of the star """
        return self.x

    def getY(self):
        """ return the y coordinate of the star """
        return self.y

    def getVertices(self):
        """ return the vertices of the star in pyGlet format """
        numberOfVertices = 10
        vertexList = pyglet.graphics.vertex_list(numberOfVertices, ('v2f', self.vertices))
        return vertexList

    def updateVertices(self):
        """ updates the vertices of the star """
        numberOfVertices = 10  # specify number of vertices needed for the shape
        for i in range(0, numberOfVertices):
            angle = i * (2.0 / 10.0) * math.pi
            if (i % 2) == 0:
                pointRadius = self.radius
            else:
                pointRadius = self.radius / 2
            self.vertices[2*i] = pointRadius * math.cos(angle) + self.x
            self.vertices[2*i+1] = pointRadius * math.sin(angle) + self.y

    def setVelocity(self, xvint, yvint):
        """ set the x & y velocity components """
        self.xvelocity = xvint
        self.yvelocity = yvint

    def setThetaIncrement(self, thetaInc):
        """ sets the value of the increment for theta """
        self.thetaIncrement = thetaInc

    def updateTheta(self):
        """ Increment theta """
        self.theta += self.thetaIncrement

    def rotateVertices(self):
        """function to translate a set of coordinates to the (0,0) origin & then rotate them by some angle theta"""
        dimensions = 2
        numberOfVertices = 10
        # translate vertices to the origin
        c = numpy.array(self.vertices).reshape(numberOfVertices, dimensions)
        for i in range(0, numberOfVertices):
            c[i][0] -= self.x
            c[i][1] -= self.y

        theta = (self.theta / 180.) * numpy.pi  # calculate theta in radians & the corresponding rotation matrix
        rotMatrix = numpy.array([[numpy.cos(theta), -numpy.sin(theta)],
                                 [numpy.sin(theta), numpy.cos(theta)]])

        c = numpy.matmul(c, rotMatrix)  # matrix-matrix multiplication with numpy

        for i in range(0, numberOfVertices):
            self.vertices[2*i] = c[i][0] + self.x
            self.vertices[2*i+1] = c[i][1] + self.y

    def setSpringConstants(self, xSpring, ySpring):
        self.kx = xSpring
        self.ky = ySpring

    def updateAccn(self, xcenter, ycenter):
        """ update the acceleration of the star """
        self.xaccn = - self.kx * (self.x - xcenter)
        self.yaccn = - self.ky * (self.y - ycenter)

    def updateVelocity(self):
        """ update the velocity of the star """
        self.xvelocity += self.xaccn
        self.yvelocity += self.yaccn
