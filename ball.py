#!/usr/bin/env python
# -*- coding: utf-8 -*-

from blocks import *

WIDTH = 32
HEIGHT = 32
GRAVITY = 0.23


class Player(sprite.Sprite):

    def __init__(self, x, y):

        sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х
        self.startY = y
        self.image = image.load("images/ball.png")
        self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.Score = "0000000"  # количество очков
        self.ring_count = 0
        self.lifes = 3
        self.life_image = image.load("images/life_image.png")
        self.ring_image = image.load("images/ring_image.png")
        self.died_image = image.load("images/poped.png")
        self.MOVE_SPEED = 4
        self.JUMP_POWER = 7.5

    def update(self, left, right, up, platforms):

        if up:
            # прыгаем, только когда можем оттолкнуться от земли
            if self.onGround:
                self.yvel = -self.JUMP_POWER

        if left:
            self.xvel = -self.MOVE_SPEED  # Лево = x - n

        if right:
            self.xvel = self.MOVE_SPEED  # Право = x + n

        if not (left or right):  # стоим, когда нет указаний идти
            self.xvel = 0

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False  # Мы не знаем, когда мы на земле
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)

    def collide(self, xvel, yvel, platforms):

        for p in platforms:
            # если есть пересечение платформы с игроком
            if sprite.collide_rect(self, p):

                if isinstance(p, Spike):
                    self.die()
                    return

                if (isinstance(p, SavePoint) and
                        not p.activeted):
                    p.get_saved(self)
                    new_score = str(int(self.Score) + 500)
                    self.Score = "0" * (7 - len(new_score)) + new_score

                if (isinstance(p, BonusLife) and
                        not p.activeted):
                    p.deactivate()
                    new_score = str(int(self.Score) + 1000)
                    self.Score = "0" * (7 - len(new_score)) + new_score
                    self.lifes += 1

                if isinstance(p, Ring) or isinstance(p, HRing):
                    if p.active:
                        new_score = str(int(self.Score) + 500)
                        self.Score = "0" * (7 - len(new_score)) + new_score
                        p.deactivate()
                        self.ring_count -= 1
                        if self.ring_count == 0:
                            for d in platforms:
                                if isinstance(d, Exit):
                                    d.activate()
                if isinstance(p, Exit):
                    exit(p)

                if (isinstance(p, FrontFontRing) or
                        isinstance(p, HFrontFontRing)):
                    for d in platforms:
                        if (sprite.collide_rect(self, d) and
                                (isinstance(d, Ring) or
                                 isinstance(d, HRing))):
                            p.deactivate()

                if (isinstance(p, BackFontRing) or
                        isinstance(p, HBackFontRing)):
                    for d in platforms:
                        if (sprite.collide_rect(self, d) and
                                (isinstance(d, Ring) or
                                 isinstance(d, HRing))):
                            p.deactivate()

                if (isinstance(p, Platform) or
                        isinstance(p, Invisible) or
                        isinstance(p, HInvisible)):
                    if xvel > 0:  # если движется вправо
                        self.rect.right = p.rect.left  # то не движется вправо

                    if xvel < 0:  # если движется влево
                        self.rect.left = p.rect.right  # то не движется влево

                    if yvel > 0:  # если падает вниз
                        self.rect.bottom = p.rect.top  # то не падает вниз
                        self.onGround = True  # и становится на что-то твердое
                        if self.yvel < 6:  # и энергия падения пропадает
                            self.yvel = 0
                        else:
                            self.yvel = - self.yvel / 2

                    if yvel < 0:  # если движется вверх
                        self.rect.top = p.rect.bottom  # то не движется вверх
                        self.yvel = 0  # и энергия прыжка пропадает

    def die(self):
        time.wait(500)
        self.lifes -= 1
        # перемещаемся в начальные координаты
        self.teleporting(self.startX, self.startY)

    def teleporting(self, go_x, go_y):
        self.rect.x = go_x
        self.rect.y = go_y

    def is_game_over(self):
        return self.lifes < 1


class FastPlayer(Player):

    def __init__(self, x, y):
        Player.__init__(self, x, y)
        self.MOVE_SPEED = 10
        self.image = image.load("images/fast_ball.png")


class HighJumpPlayer(Player):

    def __init__(self, x, y):
        Player.__init__(self, x, y)
        self.JUMP_POWER = 12
        self.image = image.load("images/high_jump_ball.png")
