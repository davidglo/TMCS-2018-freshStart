from . import game_object
from .. import resources
from pyglet.window import key
import random


class Goomba(game_object.GameObject):

    def __init__(self, *args, **kwargs):
        super(Goomba, self).__init__(resources.goombawalk1, *args, **kwargs)
        self.key_handler = key.KeyStateHandler()
        self.scale *= 5
        self.velocity_x = [-1,1][random.randrange(2)] * 90
        self.run_animation_tacker = 0

    def check_bounds(self):
        min_x = -75
        min_y = 150
        max_x = 875
        if self.x < min_x:
            self.x = max_x
        elif self.x > max_x:
            self.x = min_x
        if self.y <= min_y:
            self.y = min_y
            self.velocity_y = 0.0

    def update(self, dt):
        super(Goomba, self).update(dt)
        self.animate()

    def animate(self):

        if self.run_animation_tacker == 41:
            self.run_animation_tacker = 0

        if self.run_animation_tacker <= 20:
            self.image = resources.goombawalk1
        elif 20 < self.run_animation_tacker <= 40:
            self.image = resources.goombawalk2

        self.run_animation_tacker += 1
