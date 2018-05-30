import pyglet
import math

class triangleClass:

    def __init__(self,ID,color,xcenter,ycenter,rad):
        """ initialize a triangle """
        self.ID = ID
        self.color = color
        self.x = xcenter
        self.y = ycenter
        self.radius = rad
#        self.xvelocity = 0
 #       self.yvelocity = 0

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

    """function for multiple triangles to move around the screen"""

    # function to define where triangles move to
    def calculateTriangleVertices(self):
        """specifications for the triangle angles and movements"""
        numberOfVertices = 3  # specify the number of vertices we need for the shape
        vertices = []

        for i in range(0, numberOfVertices):
            angle = i * (2.0 / 3.0) * math.pi
            x = self.radius * math.cos(angle) + self.x
            y = self.radius * math.sin(angle) + self.y
            vertices.append(x)
            vertices.append(y)

            # convert the vertices list to pyGlet vertices format for the first triangle & return this list
        vertexList = pyglet.graphics.vertex_list(numberOfVertices, ('v2f', vertices))
        return vertexList

 #   def setVelocity(self, xvel, yvel):
 #       self.xvelocity = xvel
 #       self.yvelocity = yvel

 #   def updateCoordinates(self, windowwidth, windowheight):
 #       if (self.x + self.xvelocity) > windowwidth or (self.x + self.velocity) < 0):
 #           self.velocity = self.velocity*-1

  #      if (self.y + self.velocity)



