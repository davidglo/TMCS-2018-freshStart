import pyglet


def center_image(image):
    image.anchor_x = image.width / 2
    image.anchor_y = 0

pyglet.resource.path = ['./resources']
pyglet.resource.reindex()

mario = marioright = pyglet.resource.image("mario.png")
marioleft = pyglet.resource.image("mario.png", flip_x=True)
mariorightjump = pyglet.resource.image("mariojump.png")
marioleftjump = pyglet.resource.image("mariojump.png", flip_x=True)
mariorunright1 =  pyglet.resource.image("mariorun1.png")
mariorunleft1 =  pyglet.resource.image("mariorun1.png", flip_x=True)
mariorunright2 =  pyglet.resource.image("mariorun2.png")
mariorunleft2 =  pyglet.resource.image("mariorun2.png", flip_x=True)
mariorunright3 =  pyglet.resource.image("mariorun3.png")
mariorunleft3 =  pyglet.resource.image("mariorun3.png", flip_x=True)

center_image(mario)
center_image(marioright)
center_image(marioleft)
center_image(mariorightjump)
center_image(marioleftjump)
center_image(mariorunright1)
center_image(mariorunright2)
center_image(mariorunright3)
center_image(mariorunleft1)
center_image(mariorunleft2)
center_image(mariorunleft3)

davidloganleft = pyglet.resource.image("david-logan-left.png")
davidloganright = pyglet.resource.image("david-logan-right.png")
goombawalk1 = pyglet.resource.image("goombawalk1.png")
goombawalk2 = pyglet.resource.image("goombawalk2.png")
goombasquashed = pyglet.resource.image("goombasquashed.png")
center_image(goombawalk1)
center_image(goombawalk2)
center_image(goombasquashed)

center_image(davidloganleft)
center_image(davidloganright)

mariojumpsound = pyglet.media.StaticSource(pyglet.resource.media('mariojump.wav'))
