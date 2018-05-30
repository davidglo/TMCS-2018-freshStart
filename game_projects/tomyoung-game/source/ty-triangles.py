import pyglet
import pyglet.gl
import math
import colours
from math import pi
import numpy as np

class triangleClass:

    def __init__(self,ID,color,xcenter,ycenter,rad, xvelocity, yvelocity):
        """ initialize a triangle """
        self.ID = ID
        self.color = colours.dic[color]
        self.x = xcenter
        self.y = ycenter
        self.radius = rad
        self.xvelocity = xvelocity
        self.yvelocity = yvelocity

    def setVelocity(self, xvel, yvel):
        self.xvelocity = xvel
        self.yvelocity = yvel

    def setCentreCoordinates(self,xcenter,ycenter):
        """ set the x,y coordinates of the triangle """
        self.x = xcenter
        self.y = ycenter

    def getColour(self):
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

    def getXVelocity(self):
        return self.xvelocity

    def getYVelocity(self):
        return self.yvelocity


class graphicsWindow(pyglet.window.Window):
    def __init__(self):
        """
        Initalise the window. Center the triangles in the center
        """
        super(graphicsWindow, self).__init__()  # constructor for graphicsWindow class

        window_center = [self.width / 2, self.height / 2]

        self.triangles = []
        self.triangles.append(triangleClass(0, 'red', window_center[0], window_center[1], 20, 100.0, 100.0))
        self.triangles.append(triangleClass(1, 'white', window_center[0], window_center[1], 20, -100.0, -100.0))
        self.triangles.append(triangleClass(2, 'yellow', window_center[0], window_center[1], 20, -100.0, 300.0))
        self.triangles.append(triangleClass(3, 'blue', window_center[0], window_center[1], 20, -500.0, -100.0))


    def update(self, dt):
        """
        Update the triangle centers
        :param dt: some frequnecy
        """

        def update_coords_and_velociities(height, width, trinagle, dt):

            newX = trinagle.getX() + dt * (trinagle.getXVelocity() + np.random.uniform(-10.0, 10.0))
            newY = trinagle.getY() + dt * (trinagle.getYVelocity() + np.random.uniform(-10.0, 10.0))

            trinagle.setCentreCoordinates(newX, newY)

            if newX > width or newY > height:
                trinagle.setVelocity(-trinagle.getXVelocity(), -trinagle.getYVelocity())

            if newX < 0 or newY < 0:
                trinagle.setVelocity(-trinagle.getXVelocity(), -trinagle.getYVelocity())


        for triangle in self.triangles:
            update_coords_and_velociities(self.height, self.width, triangle, dt)


    def on_draw(self):
        """
        Draw the triangles, by generating verticies from the centers
        :return: vertexes
        """

        # clear the graphics buffer
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)

        def add_vertecies(triangle):

            vertices = []  # initialize a list of vertices
            angles = [0.0, ((2.0 / 3.0) * pi), ((4.0 / 3.0) * pi)]

            for j in range(len(angles)):
                vertices.append(triangle.radius * math.cos(angles[j]) + triangle.getX())  # append the x value to the vertex list
                vertices.append(triangle.radius * math.sin(angles[j]) + triangle.getY())  # append the y value to the vertex list

            return vertices


        def draw_trinagle(trinagle):
            # now we will calculate the list of vertices required to draw the triangle
            numberOfVertices = 3  # specify the number of vertices we need for the shape

            # convert the vertices list to pyGlet vertices format
            vertexList = pyglet.graphics.vertex_list(numberOfVertices, ('v2f', add_vertecies(trinagle)))

            # now use pyGlet commands to draw lines between the vertices
            colour = trinagle.getColour()
            pyglet.gl.glColor3f(colour[0], colour[1], colour[2])  # specify colors
            vertexList.draw(pyglet.gl.GL_LINE_LOOP)  # draw


        for triangle in self.triangles:
            draw_trinagle(triangle)


# this is the main game engine loop
if __name__ == '__main__':
    window = graphicsWindow()  # initialize a window class
    pyglet.clock.schedule_interval(window.update, 1 / 60.0)  # tell pyglet the on_draw() & update() timestep
    pyglet.app.run()  # run pyglet
