import pyglet
import pyglet.gl
import colors
from hexagonclass import hexagonClass

# initialize a list of triangles
cutieshapes = []
# populate the list of triangles
cutieshapes.append(hexagonClass('baby1', 'blue',    0, 0, 20))
cutieshapes.append(hexagonClass('baby2', 'hotpink', 0, 0, 10))
cutieshapes.append(hexagonClass('baby3', 'coral',  0, 0, 40))
cutieshapes.append(hexagonClass('baby4', 'red',     0, 0, 50))
cutieshapes.append(hexagonClass('baby5', 'green',   0, 0, 20))

class graphicsWindow(pyglet.window.Window):
    def __init__(self):
        super(graphicsWindow, self).__init__()  # constructor for graphicsWindow class

        for i in range(0,len(cutieshapes)):
            cutieshapes[i].setCentreCoordinates(self.width / 2, self.height / 2)
            cutieshapes[i].updateVertices()
            cutieshapes[i].setVelocity(i + 1, i + 2)
            cutieshapes[i].setThetaIncrement(5 * i)

    def update(self, dt):
        # print "Updating the center "
        for i in range(0,len(cutieshapes)):
            cutieshapes[i].updateCoordinates(self.width, self.height)
            cutieshapes[i].updateVertices()
            cutieshapes[i].updateTheta()
            cutieshapes[i].rotateVertices()

    def on_draw(self):
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)    # clear the graphics buffer

        for i in range(0,len(cutieshapes)):
            # calculate the list of vertices required to draw
            vertexList = cutieshapes[i].getVertices()
            #  use pyGlet commands to draw lines between the vertices
            lineColor = cutieshapes[i].getColor()  # openGL color specification
            pyglet.gl.glColor3f(colors.color[lineColor][0], colors.color[lineColor][1], colors.color[lineColor][2])
            vertexList.draw(pyglet.gl.GL_LINE_LOOP)  # draw
# this is the main game engine loop
if __name__ == '__main__':
    window = graphicsWindow()  # initialize a window class
    pyglet.clock.schedule_interval(window.update, 1 / 50.0)  # tell pyglet the on_draw() & update() timestep
    pyglet.app.run()  # run the infinite pyglet loop