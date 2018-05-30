from . import game_object


class Enemy(game_object.GameObject):

    def __init__(self,image , *args, **kwargs):
        super(Enemy, self).__init__(img=image, *args, **kwargs)

    def update(self, dt):
        super(Enemy, self).update(dt)
