from pygame import *

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
SPIKE_WIDTH = 17


class Platform(sprite.Sprite):

    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load("images/platform.png")
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


class Spike(sprite.Sprite):

    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load("images/spike.png")
        self.rect = Rect(x, y, SPIKE_WIDTH, PLATFORM_HEIGHT)


class Ring(sprite.Sprite):

    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load("images/hit_box.png")
        self.rect = Rect(x, y, 1, 1)
        self.active = True

    def deactivate(self):
        self.active = False


class BackFontRing(sprite.Sprite):

    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load("images/vertical_ring_back.png")
        self.rect = Rect(x, y, 15, 64)

    def deactivate(self):
        self.image = image.load("images/vertical_ring_back_d.png")


class FrontFontRing(sprite.Sprite):

    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load("images/vertical_ring_front.png")
        self.rect = Rect(x, y, 15, 64)

    def deactivate(self):
        self.image = image.load("images/vertical_ring_front_d.png")


class Invisible(sprite.Sprite):

    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.rect = Rect(x, y, 11, 12)


class HRing(sprite.Sprite):

    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load("images/hit_box.png")
        self.rect = Rect(x, y, 1, 1)
        self.active = True

    def deactivate(self):
        self.active = False


class HBackFontRing(sprite.Sprite):

    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load("images/horizontal_ring_back.png")
        self.rect = Rect(x, y, 64, 15)

    def deactivate(self):
        self.image = image.load("images/horizontal_ring_back_d.png")


class HFrontFontRing(sprite.Sprite):

    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load("images/horizontal_ring_front.png")
        self.rect = Rect(x, y, 64, 15)

    def deactivate(self):
        self.image = image.load("images/horizontal_ring_front_d.png")


class HInvisible(sprite.Sprite):

    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.rect = Rect(x, y, 8, 14)


class SavePoint(sprite.Sprite):

    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load("images/save_point.png")
        self.X = x
        self.Y = y
        self.activeted = False
        self.rect = Rect(x, y, 32, 32)

    def get_saved(self, ball):
        ball.startX = self.X
        ball.startY = self.Y

        self.deactivate()

    def deactivate(self):
        self.activeted = True
        self.image = image.load("images/save_point_activeted.png")


class BonusLife(sprite.Sprite):

    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load("images/bonus_life.png")
        self.activeted = False
        self.rect = Rect(x, y, 32, 32)

    def deactivate(self):
        self.activeted = True
        self.image = image.load("images/hit_box.png")


class Exit(sprite.Sprite):

    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load("images/hit_box.png")
        self.rect = Rect(x, y, 64, 64)
        self.active = False

    def activate(self):
        self.active = True
        self.image = image.load("images/exit.png")

    def exit(self):
        raise SystemExit
