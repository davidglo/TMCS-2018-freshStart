import pyglet
from . import player
from .. import util


class GameObject(pyglet.sprite.Sprite):
    """A sprite with physical properties such as velocity"""

    def __init__(self, *args, **kwargs):
        super(GameObject, self).__init__(*args, **kwargs)
        self.velocity_x = 0.0
        self.velocity_y = 0.0
        self.force_x = 0.0
        self.force_y = - 2500
        self.dead = False

    def update(self, dt):
        self.x += self.velocity_x * dt + self.force_x * dt**2 / 2
        self.y += self.velocity_y * dt + self.force_y * dt**2 / 2
        self.velocity_x += self.force_x * dt
        self.velocity_y += self.force_y * dt
        self.check_bounds()

    def collides_with(self, other_object):
        collision_distance = self.image.width * self.scale / 2 + other_object.image.width * other_object.scale / 2
        actual_distance = util.distance(self.position, other_object.position)
        return (actual_distance <= collision_distance)

    def handle_collision_with(self, other_object):
        if isinstance(self, player.Player) and self.velocity_y < - 1 :
            self.dead = False
            self.velocity_y += 1450
        elif other_object.__class__ == self.__class__:
            self.dead = False
        else:
            self.dead = True
