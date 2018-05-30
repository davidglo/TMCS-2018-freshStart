import pyglet
import pyglet.gl
import pyglet.window as pw
import math
import random

class graphicsWindow(pyglet.window.Window):
    def __init__(self):
        self.dimensions = [640, 480]
        super(graphicsWindow, self).__init__(width=self.dimensions[0], height=self.dimensions[1], vsync=True)  # constructor for graphicsWindow class
        self.step = 20
        self.length = 10
        self.vertices = [self.step, self.step, self.step*(1+self.length), self.step]
        self.wrap = False
        self.direction = "R"
        self.thickness = 10
        self.food = self.generate_food();
        self._called = 0
        self.game_over = False

    #need arr of len 4
    def determine_direction(self, arr):
        if(arr[0] < arr[2]): return "R"
        elif(arr[0] > arr[2]): return "L"
        elif(arr[1] < arr[3]): return "U"
        elif(arr[1] > arr[3]): return "D"

    def wrap_snake(self):
        for i in range(len(self.vertices)):
            if(i % 2 == 0):
                if(self.vertices[i] > self.dimensions[0]):
                    self.vertices[i] -= self.dimensions[0]
                elif(self.vertices[i] < 0):
                    self.vertices[i] += self.dimensions[0]
            else:
                if(self.vertices[i] > self.dimensions[1]):
                    self.vertices[i] -= self.dimensions[1]
                elif(self.vertices[i] < 0):
                    self.vertices[i] += self.dimensions[1]

    def generate_food(self):
        while(True):
            rand_x = random.randrange(self.step, self.dimensions[0]-self.step, self.step)
            rand_y = random.randrange(self.step, self.dimensions[1]-self.step, self.step)
            if(not self.in_snake([rand_x, rand_y])):
                break
        return [rand_x, rand_y]

    def check_bounds(self):
        self.game_over = self.in_snake(self.vertices[-2:])
        if(not self.game_over):
            for i in range(len(self.vertices)):
                if(i % 2 == 0):
                    if(self.vertices[i] > self.dimensions[0] - self.step or self.vertices[i] < self.step):
                        self.game_over = True
                elif(self.vertices[i] > self.dimensions[1] - self.step or self.vertices[i] < self.step):
                    self.game_over = True

    #arr of dim 2
    def in_snake(self, arr):
        for i in range(2, len(self.vertices), 2):
            x2 = self.vertices[i]
            x1 = self.vertices[i-2]
            y2 = self.vertices[i+1]
            y1 = self.vertices[i-1]
            diff_x = x2 - x1
            diff_y = y2 - y1
            if((diff_x == 0 and abs(arr[0]-x1) < self.thickness and arr[1] > min(y2, y1) and arr[1] < max(y2, y1)) or
            (diff_y == 0 and abs(arr[1]-y1) < self.thickness and arr[0] > min(x2, x1) and arr[0] < max(x2, x1))
            and (arr != [x1, y1] and arr != [x2, y2])):
                return True
        return False

    def update_tail(self):
        dir_old = self.determine_direction(self.vertices[:4])
        if(dir_old == "L"):
            self.vertices[0] -= self.step
        if(dir_old == "R"):
            self.vertices[0] += self.step
        if(dir_old == "D"):
            self.vertices[1] -= self.step
        if(dir_old == "U"):
            self.vertices[1] += self.step
        if (self.vertices[:2] == self.vertices[2:4]):
            self.vertices = self.vertices[2:]

    def update_head(self):
        dir_new = self.determine_direction(self.vertices[-4:])
        if(dir_new == "L"):
            self.vertices[-2] -= self.step
        if(dir_new == "R"):
            self.vertices[-2] += self.step
        if(dir_new == "D"):
            self.vertices[-1] -= self.step
        if(dir_new == "U"):
            self.vertices[-1] += self.step

    def on_key_press(self, symbol, modifiers):
        if(self.game_over):
            if(symbol == pw.key.ENTER):
                self.__init__()
            elif(symbol == pw.key.ESCAPE):
                pyglet.app.exit()
        else:
            if(symbol == pw.key.DOWN and self.direction not in ["U", "D"]):
                self.vertices += [self.vertices[-2], self.vertices[-1] - self.step]
                self.check_bounds()
                self.update_tail()
                self.direction = "D"
            elif (symbol == pw.key.UP and self.direction not in ["U", "D"]):
                self.vertices += [self.vertices[-2], self.vertices[-1] + self.step]
                self.check_bounds()
                self.update_tail()
                self.direction = "U"
            elif (symbol == pw.key.LEFT and self.direction not in ["R", "L"]):
                self.vertices += [self.vertices[-2] - self.step, self.vertices[-1]]
                self.check_bounds()
                self.update_tail()
                self.direction = "L"
            elif (symbol == pw.key.RIGHT and self.direction not in ["R", "L"]):
                self.vertices += [self.vertices[-2] + self.step, self.vertices[-1]]
                self.check_bounds()
                self.update_tail()
                self.direction = "R"

    def on_draw(self):
        # clear the graphics buffer
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)

        if(not self.game_over):
            # convert the vertices list to pyGlet vertices format
            vertexList = pyglet.graphics.vertex_list(len(self.vertices) // 2, ('v2f', self.vertices))
            pointList = pyglet.graphics.vertex_list(1, ('v2f', self.food))
            head = pyglet.graphics.vertex_list(1, ('v2f', self.vertices[-2:]))
            score = pyglet.text.Label('Logans Eaten: %d' % (self.length - 10),
                                      font_name='Arial',
                                      font_size=13,
                                      x=0, y = self.dimensions[1],
                                      anchor_x='left', anchor_y='top')
            score.draw()
            pyglet.gl.glLineWidth(self.thickness)
            pyglet.gl.glPointSize(self.thickness)
            # now use pyGlet commands to draw lines between the vertices
            pyglet.gl.glColor3f(0, 1, 0)  # specify colors
            vertexList.draw(pyglet.gl.GL_LINE_STRIP)  # draw
            pyglet.gl.glColor3f(1, 0, 0)
            pointList.draw(pyglet.gl.GL_POINTS)
            pyglet.gl.glColor3f(1, 1, 1)
            head.draw(pyglet.gl.GL_POINTS)
            pic = pyglet.image.load('david-logan-posing-left.png')
            pic.anchor_x = pic.width // 2
            pic.anchor_y = pic.height // 2
            pic.blit(self.food[0], self.food[1])
        else:
            label = pyglet.text.Label('GAME OVER',
                                      font_name='Arial',
                                      font_size=36,
                                      x=self.dimensions[0] // 2, y = 2 * self.dimensions[1] // 3,
                                      anchor_x='center', anchor_y='center')
            prompt = pyglet.text.Label('Press ENTER to eat more Logans, ESC if this game is too trivial',
                                      font_name='Arial',
                                      font_size=12,
                                      x=self.dimensions[0] // 2, y=self.dimensions[1] // 3,
                                      anchor_x='center', anchor_y='center')
            score = pyglet.text.Label("You renormalised %d Logans. Well done!" % (self.length - 10),
                                      font_name='Arial',
                                      font_size=12,
                                      x=self.dimensions[0] // 2, y=self.dimensions[1] // 2,
                                      anchor_x='center', anchor_y='center')
            self.clear()
            label.draw()
            prompt.draw()
            score.draw()
            #pyglet.app.exit()

    def update(self, dt):
        self._called += 1
        if(self.length >= 30 or self._called % (30 - self.length) == 0):
            self.called = 0;
            if(tuple(self.food) in zip(*[iter(self.vertices)]*2)):
                self.update_head()
                self.food = self.generate_food()
                self.length += 1
            else:
                self.update_tail()
                self.update_head()
            if(self.wrap):
                self.wrap_snake()
            if(not self.game_over):
                self.check_bounds()
            self.on_draw()

# this is the main game engine loop
if __name__ == '__main__':
    snake = graphicsWindow()  # initialize a window class
    pyglet.clock.schedule_interval(snake.update, 1 / 60)  # tell pyglet the on_draw() & update() timestep
    pyglet.app.run()  # run pyglet
