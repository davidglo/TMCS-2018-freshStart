"""this program is a graphical representation of moving stars"""

import pyglet
import pyglet.gl
import colors
import random
from starClass import starClass

# initialise a list of stars
stars = []

# populate the list of stars
stars.append(starClass('star1', 'hotpink', 0, 0, 30))
stars.append(starClass('star2', 'green', 0, 0, 30))
stars.append(starClass('star3', 'cyan', 0, 0, 30))
stars.append(starClass('star4', 'red', 0, 0, 30))
stars.append(starClass('star5', 'yellow', 0, 0, 30))
stars.append(starClass('star6', 'white', 0, 0, 30))
stars.append(starClass('star7', 'gold', 0, 0, 30))

class graphicsWindow(pyglet.window.Window):
    def __init__(self):
        vmaxStars = 10 # Maximum velocity for rng
        thetaMax = 5 # Maximum theta
        super(graphicsWindow, self).__init__()  # constructor for graphicsWindow class

        for i in range(0, len(stars)):
            # set inital coordinates of the centre of the stars
            stars[i].setCentreCoordinates(random.uniform(0, self.width), random.uniform(0, self.height))
            stars[i].updateVertices()
            # set initial velocities of each star
            #stars[i].setVelocity(random.uniform(-vmaxStars, vmaxStars), random.uniform(-vmaxStars, vmaxStars))
            stars[i].setThetaIncrement(random.uniform(-thetaMax, thetaMax))
            #stars[i].setSpringConstants(random.uniform(0.0001, 0.01), random.uniform(0.0001, 0.01))

    def update(self, dt):
        #print ("Updating the center of the stars")
        for i in range(0, len(stars)):
            #stars[i].updateCentreCoordinates(self.width, self.height)
            #stars[i].updateVertices()
            stars[i].updateTheta()
            stars[i].rotateVertices()
            #stars[i].updateAccn(self.width / 2, self.height / 2)
            #stars[i].updateVelocity()

    def on_draw(self):
        # clear the graphics buffer
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)

        for i in range(0, len(stars)):
            # calculate list of vertices to draw star
            vertexList = stars[i].getVertices()
            # use pyGlet to draw lines between the vertices
            lineColor = stars[i].getColor()
            pyglet.gl.glColor3f(colors.color[lineColor][0],colors.color[lineColor][1],colors.color[lineColor][2])  # specify colors
            vertexList.draw(pyglet.gl.GL_LINE_LOOP)  # draw

# this is the main game engine loop
if __name__ == '__main__':
    window = graphicsWindow()  # initialize a window class
    pyglet.clock.schedule_interval(window.update, 1 / 60.0)  # tell pyglet the on_draw() & update() timestep
    pyglet.app.run()  # run pyglet