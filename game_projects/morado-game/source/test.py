import pyglet
import random
from pyglet.window import key, mouse
from modules import *


# Create pyglet window and add background image
window = pyglet.window.Window()
bg = pyglet.resource.image("bg1.png")
bg.width = window.width
bg.height = window.height


def solid_box(field, ball):
    """
    Solid boundary conditions.
    :param field:
    :param ball:
    :return:
    """

    if (ball.x >= field.width) or (ball.x <= 0):
        # The ball hits the left or right edges
        ball.x = window.width // 2
        ball.y = window.height // 2
        ball.velx = 2 * float(random.choice(['+1', '-1']))
        ball.vely = 2 * float(random.choice(['+1', '-1']))

        # Update the score
        score["right"] += 1

    elif (ball.y >= field.height) or (ball.y <= 0):
        ball.vely *= -1
        score["left"] += 1



    return None




def update(dt):
    print("Time elapsed: " + str(dt))
    pass

@window.event
def on_draw():
    window.clear()
    bg.blit(0,0)


    # Boundary conditions
    solid_box(field, ball)

    # Hit the rectangle/brick

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


# Create players instances
y_player = window.height // 2
left_player = Player("Joao1", 20, y_player, 0.0, 0.0)
right_player = Player("Joao2", 610, y_player, 0.0, 0.0)

# Game's score
score = dict(left=0,right=0)

# Create ball's instance
ball = Ball("Pong's ball", window.height // 2, window.width // 2, 1, 1)

print(ball.x, ball.y)
# Create game field instance
field = GameField(window.width, window.height)

# Run game loop
pyglet.clock.schedule(update)
pyglet.app.run()