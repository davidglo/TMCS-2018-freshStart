import pyglet
import pyglet.gl
import math
from random import randint
import colours
from triangleClass import triangleClass

triangles = []

triangles.append(triangleClass('triangle1', 'blue', 0, 0, 20))
triangles.append(triangleClass('triangle2', 'hotpink', 0, 0, 20))
triangles.append(triangleClass('triangle3', 'orange', 0, 0, 20))
triangles.append(triangleClass('triangle4', 'white', 0, 0, 20))
triangles.append(triangleClass('triangle5', 'peru', 0, 0, 20))

"""makes two triangles that float around"""

class graphicsWindow(pyglet.window.Window):
    def __init__(self):
        """initialises the window and centers of the two triangles"""
        super(graphicsWindow, self).__init__()          # constructor for graphicsWindow class
        for i in range(len(triangles)):
            triangles[i].setCentreCoordinates(self.width / 2, self.height/ 2)
            triangles[i].updateVertices()
            triangles[i].velocity(randint(-10, 10), randint(-10, 10))
            triangles[i].setThetaIncrement(randint(0, 60))


    def update(self, dt):
        """generates random translations for the triangles at each timestep"""
        print("Updating the centre of the triangle")
        for i in range(len(triangles)):
            triangles[i].new_coords(self.width, self.height)
            triangles[i].updateVertices()
            triangles[i].updateTheta()
            triangles[i].rotateVertices()

    def on_draw(self):
        """draws the two triangles with selected colours"""
        #clear the graphics buffer
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)

        # now we will calculate the list of vertices required to draw the triangle
        for i in range(len(triangles)):
            vertexList = triangles[i].getVertices()
            linecolour = triangles[i].getColor()
            pyglet.gl.glColor3f(colours.colours[linecolour][0], colours.colours[linecolour][1],
                                colours.colours[linecolour][2])  # specify colours
            vertexList.draw(pyglet.gl.GL_LINE_LOOP)


# this is the main game engine loop
if __name__ == '__main__':
    window = graphicsWindow()   # initialise a window class
    pyglet.clock.schedule_interval(window.update, 1 / 30.0)      # tell pyglet the on_draw() & update() timestep
    pyglet.app.run()    #run pyglet