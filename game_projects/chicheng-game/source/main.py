from game.objects import player
from game.objects import goomba
from game.objects import logan
from pyglet.gl import *
from game import resources
from random import randint
glEnable(GL_TEXTURE_2D)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)


game_window = pyglet.window.Window(800, 600)
main_batch = pyglet.graphics.Batch()
score_label = pyglet.text.Label(text="Score: 0", x=10, y=575, batch=main_batch)
level_label = pyglet.text.Label(text="TMCS Mario",
                                x=400, y=575, anchor_x='center', batch=main_batch)

p = player.Player(x=400, y=150, batch=main_batch)

game_window.push_handlers(p)
game_window.push_handlers(p.key_handler)
game_objects = [p]


def add_enemy():
    if randint(0, 1) == 0:
        e = goomba.Goomba(x=-50, y=150, batch=main_batch)
    else:
        e = logan.Logan(x=-50, y=150, batch=main_batch)
    return [e]

to_draw = []

timer = 0
def update(dt):
    global timer
    timer += 1
    for i in range(len(game_objects)):
        for j in range(i + 1, len(game_objects)):
            obj_1 = game_objects[i]
            obj_2 = game_objects[j]
            if not obj_1.dead and not obj_2.dead:
                if obj_1.collides_with(obj_2):
                    obj_1.handle_collision_with(obj_2)
                    obj_2.handle_collision_with(obj_1)

    for obj in game_objects:
        obj.update(dt)

    for to_remove in [obj for obj in game_objects if obj.dead]:
        to_remove.delete()
        if isinstance(to_remove, goomba.Goomba):
            sprite = pyglet.sprite.Sprite(img=resources.goombasquashed, batch=main_batch)
            sprite.x = to_remove.x
            sprite.y = to_remove.y
            sprite.scale *= 5
            to_draw.append([sprite, 120])
        game_objects.remove(to_remove)

    if timer > 120:
        game_objects.extend(add_enemy())
        timer = 0

    for draw in to_draw:
        draw[1] -= 1
    for to_remove in [obj for obj in to_draw if obj[1] == 0]:
        to_remove[0].delete()
        to_draw.remove(to_remove)

@game_window.event
def on_draw():
    global bla
    game_window.clear()
    main_batch.draw()
    if len(to_draw) != 0:
        for sprite in to_draw:
            sprite[0].draw()



if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1 / 120.0)
    pyglet.app.run()