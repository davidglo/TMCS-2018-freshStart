import pyglet
import random
from pyglet.window import key, mouse

window = pyglet.window.Window()
bg = pyglet.resource.image("bg1.png")
bg.width = window.width
bg.height = window.height
image = pyglet.resource.image('logan.png')
image.width = 40
image.height = 40
image.anchor_x = image.width // 2       # X coordinate of anchor, relative to left edge of image data
image.anchor_y = image.height // 2      # Y coordinate of anchor, relative to bottom edge of image data

image.x = window.width // 2
image.y = window.height // 2

label_center = pyglet.text.Label("SCORE", x=window.width // 2, y=window.height // 2,
                               anchor_x='center', anchor_y='center', font_size=20)

explosion = pyglet.resource.media('explosion.wav', streaming=False)
beep = pyglet.resource.media('Beep1.wav', streaming=False)


# Loop the background music
#player = pyglet.media.Player()
#player.queue(pyglet.media.load('8bit.wav'))
#player.eos_action = 'loop'
#player.play()
#music = pyglet.resource.media('debussy.mp3')
#music.play()


def draw_rect(x, y, width, height, color):
    width = int(round(width))
    height = int(round(height))
    image_pattern = pyglet.image.SolidColorImagePattern(color=color)
    image = image_pattern.create_image(width, height)
    image.blit(x, y)

    return image

def update(dt):
    #print(dt) # time elapsed since last time we were called
    pass

@window.event
def on_draw():
    window.clear()
    bg.blit(0,0)

    if (image.x > window.width) or (image.x < 0):
        velocity["dx"] *= -1
        explosion.play()
        image.x = window.width // 2
        image.y = window.height // 2
        velocity["dx"] = 2 * float(random.choice(['+1', '-1']))
        velocity["dy"] = 2 * float(random.choice(['+1', '-1']))

    if (image.y > window.height) or (image.y < 0):
        velocity["dy"] *= -1


    if (image.x == pos_right["x"]-10) and ((image.y-pos_right["y"]) < 100) and ((image.y-pos_right["y"]) > 0):
        velocity["dx"] *= -1
        beep.play()
    if (image.x == pos_left["x"]+30) and ((image.y-pos_left["y"]) < 100) and ((image.y-pos_left["y"]) > 0):
        velocity["dx"] *= -1
        beep.play()




    image.x += velocity["dx"]
    image.y += velocity["dy"]

    image.blit(image.x,image.y)

    left_player = draw_rect(pos_left["x"],pos_left["y"],20,100,(0,255,0,1))
    right_player = draw_rect(pos_right["x"],pos_right["y"], 20,100,(0,255,0,1))


    # Update the scores
    if image.x == 0:
        score["right"] += 1
    if image.x == window.width:
        score["left"] +=1


    if score["right"] == 5:
        window.clear()
        label_left = pyglet.text.Label("Player 2 won... That was trivial!", x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center', font_size=20)
        label_left.draw()
    elif score["left"] == 5:
        window.clear()
        label_left = pyglet.text.Label("Player 2 won... That was trivial!", x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center', font_size=20)
        label_left.draw()
    else:
        label_left = pyglet.text.Label(str(score["left"]//1), x=window.width//4, y=window.height//2,
                          anchor_x='center', anchor_y='center', font_size=20)
        label_right = pyglet.text.Label(str(score["right"]//1), x=3*window.width//4, y=window.height//2,
                          anchor_x='center', anchor_y='center', font_size=20)

        label_left.draw()
        label_right.draw()
        label_center.draw()



@window.event
def on_key_press(symbol, modifiers):
    # Left player
    if symbol == key.UP and pos_left["y"] < window.height - 100:
        pos_left["y"] += 40
    if symbol == key.DOWN and pos_left["y"] > 0:
        pos_left["y"] -= 40

    # Right player
    if symbol == key.LEFT and pos_right["y"] < window.height - 100:
        pos_right["y"] += 40
    if symbol == key.RIGHT and pos_right["y"] > 0:
        pos_right["y"] -= 40





score = dict(left=0,right=0)
pos_left = dict(x=20,y=window.height // 2 - 50)
pos_right = dict(x=window.width - 30 ,y=window.height // 2 - 50)
velocity = dict(dx=3*float(random.choice(['+1', '-1'])),dy=3*float(random.choice(['+1', '-1'])))

# Run game loop
pyglet.clock.schedule(update)
pyglet.app.run()