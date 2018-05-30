"""this program is a graphical representation of two randomly moving triangles"""

import pyglet
import pyglet.gl
import colors
import random
from triangleClass import triangleClass

# initialise a list of triangles
triangles = []

# populate the list of triangles
triangles.append(triangleClass('triangle1', 'hotpink', 0, 0, 20))
triangles.append(triangleClass('triangle2', 'green', 0, 0, 20))
triangles.append(triangleClass('triangle3', 'cyan', 0, 0, 20))
triangles.append(triangleClass('triangle4', 'red', 0, 0, 20))
triangles.append(triangleClass('triangle5', 'yellow', 0, 0, 20))

class graphicsWindow(pyglet.window.Window):
    def __init__(self):
        vmax = 10 # Maximum velocity for rng
        thetaParameter = 10 # Maximum theta
        super(graphicsWindow, self).__init__()  # constructor for graphicsWindow class

        for i in range(0, len(triangles)):
            # set inital coordinates of the centre of the triangles
            triangles[i].setCentreCoordinates(self.width / 2, self.height / 2)
            triangles[i].updateVertices()
            # set initial velocities of each triangle
            triangles[i].setVelocity(random.randint(-vmax, vmax), random.randint(-vmax, vmax))
            triangles[i].setThetaIncrement(random.gauss(0, thetaParameter))
            triangles[i].setSpringConstants(random.uniform(0.0001, 0.01), random.uniform(0.0001, 0.01))

    def update(self, dt):
        #print ("Updating the center of the triangles")
        for i in range(0, len(triangles)):
            triangles[i].updateCentreCoordinates(self.width, self.height)
            triangles[i].updateVertices()
            triangles[i].updateTheta()
            triangles[i].rotateVertices()
            triangles[i].updateAccn(self.width / 2, self.height / 2)
            triangles[i].updateVelocity()

    def on_draw(self):
        # clear the graphics buffer
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)

        for i in range(0, len(triangles)):
            # calculate list of vertices to draw triangle
            vertexList = triangles[i].getVertices()
            # use pyGlet to draw lines between the vertices
            lineColor = triangles[i].getColor()
            pyglet.gl.glColor3f(colors.color[lineColor][0],colors.color[lineColor][1],colors.color[lineColor][2])  # specify colors
            vertexList.draw(pyglet.gl.GL_LINE_LOOP)  # draw

# this is the main game engine loop
if __name__ == '__main__':
    window = graphicsWindow()  # initialize a window class
    pyglet.clock.schedule_interval(window.update, 1 / 60.0)  # tell pyglet the on_draw() & update() timestep
    pyglet.app.run()  # run pyglet