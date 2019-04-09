#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
from blocks import (Platform, Spike, Ring,
                    BackFontRing, FrontFontRing, Invisible,
                    HRing, HBackFontRing, HFrontFontRing,
                    HInvisible, SavePoint, BonusLife, Exit)

WIDTH = 32
HEIGHT = 32
GRAVITY = 0.23


class Player(sprite.Sprite):

    def __init__(self, x_coordinate, y_coordinate):

        sprite.Sprite.__init__(self)
        self.xvel = 0
        self.startX = x_coordinate
        self.startY = y_coordinate
        self.image = image.load("images/ball.png")
        self.rect = Rect(x_coordinate, y_coordinate, WIDTH, HEIGHT)
        self.yvel = 0
        self.onGround = False
        self.Score = "0000000"
        self.ring_count = 0
        self.lifes = 3
        self.life_image = image.load("images/life_image.png")
        self.ring_image = image.load("images/ring_image.png")
        self.died_image = image.load("images/poped.png")
        self.MOVE_SPEED = 4
        self.JUMP_POWER = 7.5

    def update(self, left, right, up, platforms):

        if up:
            if self.onGround:
                self.yvel = -self.JUMP_POWER

        if left:
            self.xvel = -self.MOVE_SPEED

        if right:
            self.xvel = self.MOVE_SPEED

        if not (left or right):
            self.xvel = 0

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)

    def collide(self, xvel, yvel, platforms):

        for platform in platforms:
            if sprite.collide_rect(self, platform):

                if isinstance(platform, Spike):
                    self.die()
                    return

                if (isinstance(platform, SavePoint) and
                        not platform.activeted):
                    platform.get_saved(self)
                    new_score = str(int(self.Score) + 500)
                    self.Score = "0" * (7 - len(new_score)) + new_score

                if (isinstance(platform, BonusLife) and
                        not platform.activeted):
                    platform.deactivate()
                    new_score = str(int(self.Score) + 1000)
                    self.Score = "0" * (7 - len(new_score)) + new_score
                    self.lifes += 1

                if isinstance(platform, Ring) or isinstance(platform, HRing):
                    if platform.active:
                        new_score = str(int(self.Score) + 500)
                        self.Score = "0" * (7 - len(new_score)) + new_score
                        platform.deactivate()
                        self.ring_count -= 1
                        if self.ring_count == 0:
                            for d in platforms:
                                if isinstance(d, Exit):
                                    d.activate()
                if isinstance(platform, Exit):
                    exit(platform)

                if (isinstance(platform, FrontFontRing) or
                        isinstance(platform, HFrontFontRing)):
                    for d in platforms:
                        if (sprite.collide_rect(self, d) and
                                (isinstance(d, Ring) or
                                 isinstance(d, HRing))):
                            platform.deactivate()

                if (isinstance(platform, BackFontRing) or
                        isinstance(platform, HBackFontRing)):
                    for d in platforms:
                        if (sprite.collide_rect(self, d) and
                                (isinstance(d, Ring) or
                                 isinstance(d, HRing))):
                            platform.deactivate()

                if (isinstance(platform, Platform) or
                        isinstance(platform, Invisible) or
                        isinstance(platform, HInvisible)):
                    if xvel > 0:
                        self.rect.right = platform.rect.left

                    if xvel < 0:
                        self.rect.left = platform.rect.right

                    if yvel > 0:
                        self.rect.bottom = platform.rect.top
                        self.onGround = True
                        if self.yvel < 6:
                            self.yvel = 0
                        else:
                            self.yvel = - self.yvel / 2

                    if yvel < 0:
                        self.rect.top = platform.rect.bottom
                        self.yvel = 0

    def die(self):
        time.wait(500)
        self.lifes -= 1
        self.teleporting(self.startX, self.startY)

    def teleporting(self, go_x, go_y):
        self.rect.x = go_x
        self.rect.y = go_y

    def is_game_over(self):
        return self.lifes < 1


class FastPlayer(Player):

    def __init__(self, x, y_coordinate):
        Player.__init__(self, x, y_coordinate)
        self.MOVE_SPEED = 10
        self.image = image.load("images/fast_ball.png")


class HighJumpPlayer(Player):

    def __init__(self, x, y_coordinate):
        Player.__init__(self, x, y_coordinate)
        self.JUMP_POWER = 12
        self.image = image.load("images/high_jump_ball.png")
