import pyglet
import pyglet.gl
import math
from random import randint

color = {}
color['Honeydew'] = [0.941, 1.0, 0.941]
color['NavajoWhite'] = [1.0, 0.871, 0.678]
color['LightCyan'] = [0.878, 1.0, 1.0]
color['Plum'] = [0.867, 0.627, 0.867]
color['Moccasin'] = [1.0, 0.894, 0.710]


# Calculate triangle vertices

def calcTriangleVertices(r,xcenter,ycenter):
    numberOfVertices = 3
    vertices = []

    for i in range(0, numberOfVertices):
        angle = i * (2.0 / 3.0) * math.pi
        x = r * math.cos(angle) + xcenter
        y = r * math.sin(angle) + ycenter
        vertices.append(x)
        vertices.append(y)

    vertexList = pyglet.graphics.vertex_list(numberOfVertices, ('v2f', vertices))
    return vertexList


class graphicsWindow(pyglet.window.Window):
    def __init__(self):
        super(graphicsWindow, self).__init__()  # constructor for graphicsWindow class
        self.center1 = [self.width / 2, self.height / 2]  # initialize the centre of the first triangle
        self.center2 = [self.width / 2, self.height / 2]  # initialize the centre of the second triangle

    def update(self, dt):
        print("Updating the center of the triangle")
        self.center1 = [self.width / 2 + randint(-200, 200), self.height / 2 + randint(-200, 200)]
        self.center2 = [self.width / 2 + randint(-200, 200), self.height / 2 + randint(-200, 200)]

    def on_draw(self):
        # clear the graphics buffer
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)

        # now we will calculate the list of vertices required to draw the triangle
        radius = 20  # specify the radius of each point from the center
        vertexList = calcTriangleVertices(radius, self.center1[0], self.center1[1])  # initialize a list of vertices
 

        # now use pyGlet commands to draw lines between the vertices

        lineColor = 'LightCyan'
        pyglet.gl.glColor3f(color[lineColor][0], color[lineColor][1], color[lineColor][2])  # specify colors
        vertexList.draw(pyglet.gl.GL_LINE_LOOP)  # draw

        radius = 20  # specify the radius of each point from the center
        vertexList = calcTriangleVertices(radius, self.center2[0], self.center2[1])  # initialize a list of vertices

        lineColor = 'Plum'
        pyglet.gl.glColor3f(color[lineColor][0], color[lineColor][1], color[lineColor][2])  # specify colors
        vertexList.draw(pyglet.gl.GL_LINE_LOOP)  # draw


# this is the main game engine loop
if __name__ == '__main__':
    window = graphicsWindow()  # initialize a window class
    pyglet.clock.schedule_interval(window.update, 1 / 50.0)  # tell pyglet the on_draw() & update() timestep
    pyglet.app.run()  # run pyglet
