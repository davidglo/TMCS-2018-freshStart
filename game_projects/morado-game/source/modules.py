import math
import numpy as np
import pyglet
from pyglet.window import key, mouse


class Player:
    def __init__(self, name, x, y, velx, vely):
        self.name = str(name)
        self.x = x
        self.y = y
        self.velx = velx
        self.vely = vely


    def __str__(self):
        return "This is player's " + self.name + " object."

    def __repr__(self):
        return self.name

    def draw_rect(self, x, y, width, height, color):
        width = int(round(width))
        height = int(round(height))
        image_pattern = pyglet.image.SolidColorImagePattern(color=color)
        image = image_pattern.create_image(width, height)
        image.blit(x, y)

        return image


class Ball:
    def __init__(self, name, x, y, velx, vely):
        self.name = str(name)
        self.x = x
        self.y = y
        self.velx = velx
        self.vely = vely

    def __str__(self):
        return "This is player's " + self.name + " object."

    def __repr__(self):
        return self.name


class GameField:
    def __init__(self, width, height):
        self.name = "Field"
        self.width = width
        self.height = height

    def __str__(self):
        return "This is Pong's field object."
