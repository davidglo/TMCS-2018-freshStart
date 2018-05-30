import math
import pyglet
import numpy


class triangleClass:

    def __init__(self,ID,color,xcenter,ycenter,rad):
        """ initialize a triangle """
        self.ID = ID
        self.color = color
        self.x = xcenter
        self.y = ycenter
        self.radius = rad
        self.xvelocity = 0
        self.yvelocity = 0
        self.vertices = [0.0] * 6
        self.theta = 0.0
        self.thetaIncrement = 0.0

    def setCentreCoordinates(self,xcenter,ycenter):
        """ set the x,y coordinates of the triangle """
        self.x = xcenter
        self.y = ycenter

    def getColor(self):
        """ return the color of the triangle """
        return self.color

    def getRadius(self):
        """ return the radius of the triangle """
        return self.radius

    def getX(self):
        """ return the x coordinate of the triangle """
        return self.x

    def getY(self):
        """ return the y coordinate of the triangle """
        return self.y

    def updateVertices(self):
        """This function generates the x and y coordinates for the three vertices of the triangle and converts them to pyglet format"""
        n_vertices = 3
        for i in range(n_vertices):
            angle = i * (2.0 / 3.0) * math.pi
            x = self.radius * math.cos(angle) + self.x
            y = self.radius * math.sin(angle) + self.y
            self.vertices[2*i] = x
            self.vertices[(2*i) + 1] = y

    def getVertices(self):
        n_vertices = 3
        vertexList = pyglet.graphics.vertex_list(n_vertices, ('v2f', self.vertices))
        return vertexList


    def velocity(self, xvel, yvel):
        self.xvelocity = xvel
        self.yvelocity = yvel

    def new_coords(self, windowWidth, windowHeight):
        if (( self.x + self.xvelocity > windowWidth ) or (self.x + self.xvelocity < 0)):
            self.xvelocity = -1 * self.xvelocity

        if (( self.y + self.yvelocity > windowHeight ) or (self.y + self.yvelocity < 0)):
            self.yvelocity = -1 * self.yvelocity

        self.x = self.x + self.xvelocity
        self.y = self.y + self.yvelocity

    def rotateVertices(self):
        """function to translate a set of coordinates to the (0,0) origin & then rotate them by some angle theta"""

        # translate vertices to the origin
        c = numpy.array([[self.vertices[0] - self.x, self.vertices[1] - self.y],
                         [self.vertices[2] - self.x, self.vertices[3] - self.y],
                         [self.vertices[4] - self.x, self.vertices[5] - self.y]])

        theta = (self.theta / 180.) * numpy.pi  # calculate theta in radians & the corresponding rotation matrix
        rotMatrix = numpy.array([[numpy.cos(theta), -numpy.sin(theta)],
                                 [numpy.sin(theta), numpy.cos(theta)]])

        c = numpy.matmul(c, rotMatrix)  # matrix-matrix multiplication with numpy

        self.vertices = [c[0][0] + self.x, c[0][1] + self.y,  # translate the rotated vertices back to the center
                         c[1][0] + self.x, c[1][1] + self.y,
                         c[2][0] + self.x, c[2][1] + self.y]

    def setThetaIncrement(self, theta_step):
        self.thetaIncrement = theta_step

    def updateTheta(self):
        self.theta = self.theta + self.thetaIncrement

