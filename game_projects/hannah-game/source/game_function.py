import pyglet
import pyglet.gl
import math
from random import randint
import colors
from triangleClass import triangleClass

# initialise triangles
triangle1 = triangleClass('triangle1', 'red', 0, 0, 20)
triangle2 = triangleClass('triangle2', 'yellow', 0, 0, 20)
triangle3 = triangleClass('triangle3', 'green', 0, 0, 20)

class graphicsWindow(pyglet.window.Window):
    """creates graphics"""
    def __init__(self):
        super(graphicsWindow, self).__init__()  # constructor for graphicsWindow class
        triangle1.setCentreCoordinates(self.width / 2, self.height / 2)
        triangle2.setCentreCoordinates(self.width / 2, self.height / 2)
        triangle3.setCentreCoordinates(self.width / 2, self.height / 2)
        colors.printAvailableColors()

    def update(self, dt):
        """updates the position of the triangle"""
        print("Updating the center of the triangle")
        triangle1.setCentreCoordinates(self.width / 2 + randint(-200, 200), self.height / 2 + randint(-200, 200))
        triangle2.setCentreCoordinates(self.width / 2 + randint(-200, 200), self.height / 2 + randint(-200, 200))
        triangle3.setCentreCoordinates(self.width / 2 + randint(-200, 200), self.height / 2 + randint(-200, 200))

    def on_draw(self):
        """depicts the colors of triangles"""
        # clear the graphics buffer
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)

        # details to draw first triangle
        radius = 20
        vertexList = triangle1.calculateTriangleVertices()

        # now use pyGlet commands to draw lines between the vertices
        lineColor = triangle1.getColor()
        pyglet.gl.glColor3f(colors.color[lineColor][0], colors.color[lineColor][1], colors.color[lineColor][2])  # specify colors
        vertexList.draw(pyglet.gl.GL_LINE_LOOP)  # draw

        # details to draw first triangle
        radius = 20
        vertexList = triangle2.calculateTriangleVertices()

        # now use pyGlet commands to draw lines between the vertices
        lineColor = triangle2.getColor()
        pyglet.gl.glColor3f(colors.color[lineColor][0], colors.color[lineColor][1], colors.color[lineColor][2])  # specify colors
        vertexList.draw(pyglet.gl.GL_LINE_LOOP)  # draw

        # details to draw first triangle
        radius = 20
        vertexList = triangle3.calculateTriangleVertices()

        # now use pyGlet commands to draw lines between the vertices
        lineColor = triangle3.getColor()
        pyglet.gl.glColor3f(colors.color[lineColor][0], colors.color[lineColor][1], colors.color[lineColor][2])  # specify colors
        vertexList.draw(pyglet.gl.GL_LINE_LOOP)  # draw




# this is the main game engine loop
if __name__ == '__main__':
    window = graphicsWindow()  # initialize a window class
    pyglet.clock.schedule_interval(window.update, 1 / 20.0)  # tell pyglet the on_draw() & update() timestep
    pyglet.app.run()  # run pyglet