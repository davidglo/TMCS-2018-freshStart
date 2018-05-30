"""This 'game' creates a specified number of triangles of different colours which blink around the screen at random"""
import pyglet
import pyglet.gl
import math
from random import randint,choice
import colourlist

class graphicsWindow(pyglet.window.Window):
    def __init__(self):
        super(graphicsWindow, self).__init__()  # constructor for graphicsWindow class
        self.center = [self.width / 2, self.height / 2]  # initialize the centre of the triangle
        print(colourlist.print_available_colours(colourlist.colours))

    def update(self, dt):
        print
        "Updating the center of the triangle"
        self.center = [self.width / 2 + randint(-200, 200), self.height / 2 + randint(-200, 200)]

    def calculate_triangle_vertices(self,radius,x_center,y_center):
        numberOfVertices = 3 # number of vertices in the shape
        vertices = []
        for multiple in range(0,5,2): # loop through the three angles in a triangle
            angle = (float(multiple) / 3.0) * math.pi
            x = radius * math.sin(angle) + x_center
            y = radius * math.cos(angle) + y_center
            vertices.append(x)  # append the x value to the vertex list
            vertices.append(y)  # append the y value to the vertex list
        vertexList = pyglet.graphics.vertex_list(numberOfVertices, ('v2f', vertices))
        return vertexList

    def generate_triangles(self,n_shapes):
        triangles = []
        for shape in range(n_shapes):
            self.update(1)
            vertices = self.calculate_triangle_vertices(20,self.center[0],self.center[1])
            triangles.append(vertices)
        return triangles

    def on_draw(self):
        # clear the graphics buffer
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)

        n_shapes = 5
        triangles = self.generate_triangles(n_shapes)



        for shape in range(n_shapes):
            # now use pyGlet commands to draw lines between the vertices
            linecolour = choice(list(colourlist.colours))
            pyglet.gl.glColor3f(colourlist.colours[linecolour][0], colourlist.colours[linecolour][1], colourlist.colours[linecolour][2])  # specify colors
            vertexList = triangles[shape]
            vertexList.draw(pyglet.gl.GL_LINE_LOOP)  # draw



# this is the main game engine loop
if __name__ == '__main__':
    window = graphicsWindow()  # initialize a window class
    pyglet.clock.schedule_interval(window.update, 1 / 2.0)  # tell pyglet the on_draw() & update() timestep
    pyglet.app.run()  # run pyglet