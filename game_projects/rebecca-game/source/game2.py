import pyglet
import pyglet.gl
import math
from random import randint
import colors
from triangleClass import triangleClass


# initialize a list of triangles
triangles = []

# populate the list of triangles
triangles.append(triangleClass('triangle1', 'blue',    0, 0, 20))
triangles.append(triangleClass('triangle2', 'yellow', 0, 0, 20))
triangles.append(triangleClass('triangle3', 'red',    0, 0, 20))
triangles.append(triangleClass('triangle4', 'green', 0, 0, 20))
triangles.append(triangleClass('triangle5', 'sienna', 0, 0, 20))


class graphicsWindow(pyglet.window.Window):
    def __init__(self):
        """This function initializes the graphics window and the position of the triangle"""
        super(graphicsWindow, self).__init__()  # constructor for graphicsWindow class
        for i in range(0, len(triangles)):
            triangles[i].setCentreCoordinates(self.width / 2, self.height / 2)
            triangles[i].updateVertices()
            triangles[i].setVelocity(i + 1, i + 2)
            triangles[i].setThetaIncrement(5 * i)


    def update(self, dt):
        """This function updates the center of the triangle"""
        print("Updating the center of the triangle")
        for i in range(0, len(triangles)):
            triangles[i].updateCoordinates(self.width, self.height)
            triangles[i].updateVertices()
            triangles[i].updateTheta()
            triangles[i].rotateVertices()


    def on_draw(self):
        """This function draws lines between the vertices calculated using the calculateTriangleVertices function and allows the user to specify the color of each triangle"""
        # clear the graphics buffer
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)

        # now we will calculate the list of vertices required to draw the triangle
        for i in range(0, len(triangles)):
            vertexlist = triangles[i].getVertices()
            lineColor = triangles[i].getColor()
            pyglet.gl.glColor3f(colors.color[lineColor][0], colors.color[lineColor][1],
                                colors.color[lineColor][2])  # specify colors
            vertexlist.draw(pyglet.gl.GL_LINE_LOOP)


# this is the main game engine loop
if __name__ == '__main__':
    """This function is the main game engine loop"""
    window = graphicsWindow()  # initialize a window class
    pyglet.clock.schedule_interval(window.update, 1 / 20.0)  # tell pyglet the on_draw() & update() timestep
    pyglet.app.run()  # run pyglet