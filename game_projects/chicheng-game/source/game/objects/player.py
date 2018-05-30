from . import game_object
from .. import resources
from pyglet.window import key


class Player(game_object.GameObject):

    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(img=resources.mario, *args, **kwargs)
        self.key_handler = key.KeyStateHandler()
        self.scale *= 5
        self.direction = 'right'
        self.run_animation_tacker = 0

    def check_bounds(self):
        min_x = 0
        min_y = 150
        max_x = 800
        if self.x < min_x:
            self.x = max_x
        elif self.x > max_x:
            self.x = min_x
        if self.y <= min_y:
            self.y = min_y
            self.velocity_y = 0.0

    def update(self, dt):
        super(Player, self).update(dt)

        if self.key_handler[key.LEFT]:
            self.velocity_x = -350
            self.direction = 'left'
        if self.key_handler[key.RIGHT]:
            self.velocity_x = 350
            self.direction = 'right'

        if self.velocity_x < -25:
            self.force_x = 750
        if self.velocity_x > 25:
            self.force_x = - 750
        if -25 < self.velocity_x < 25:
            self.velocity_x = 0
            self.force_x = 0

        self.animate()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE and self.y == 150:
            self.jump()
            resources.mariojumpsound.play()
            self.animate()

    def jump(self):
        self.velocity_y = 1000.0

    def animate(self):

        if self.y == 150 and -25 < self.velocity_x < 25:

            if self.direction == 'right':
                self.image = resources.marioright
            else:
                self.image = resources.marioleft

            self.run_animation_tacker = 0

        elif self.y == 150:

            if self.run_animation_tacker == 16:
                self.run_animation_tacker = 0

            if self.run_animation_tacker <= 5:
                if self.direction == 'right':
                    self.image = resources.mariorunright1
                else:
                    self.image = resources.mariorunleft1
            elif 5 < self.run_animation_tacker <= 10:
                if self.direction == 'right':
                    self.image = resources.mariorunright2
                else:
                    self.image = resources.mariorunleft2
            elif 10 < self.run_animation_tacker <= 15:
                if self.direction == 'right':
                    self.image = resources.mariorunright3
                else:
                    self.image = resources.mariorunleft3

            self.run_animation_tacker += 1

        else:

            if self.direction == 'right':
                self.image = resources.mariorightjump
            else:
                self.image = resources.marioleftjump

            self.run_animation_tacker = 0
