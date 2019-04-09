#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pygame
from pygame import (Surface, Color, KEYDOWN, KEYUP,
                    K_LEFT, K_RIGHT, K_UP, QUIT)
from blocks import (Platform, Spike, Ring,
                    BackFontRing, FrontFontRing, Invisible,
                    HRing, HBackFontRing, HFrontFontRing,
                    HInvisible, SavePoint, BonusLife, Exit)
from levels import level_1
from camera import Camera, camera_configure

WIN_WIDTH = 9 * 32
WIN_HEIGHT = 10 * 32
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#93e6fe"
SCORE_GROUND_COLOR = "#0f56a4"
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32


def play(player):
    pygame.init()

    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Bounce")

    background = Surface((WIN_WIDTH, WIN_HEIGHT))
    background.fill(Color(BACKGROUND_COLOR))

    score_ground = Surface((WIN_WIDTH, WIN_HEIGHT - 3 * 32))
    score_ground.fill(Color(SCORE_GROUND_COLOR))

    ball = player(64, 32)
    up = left = right = False

    my_font = pygame.font.SysFont('Arial', 30)

    entities_back = pygame.sprite.Group()
    entities_front = pygame.sprite.Group()
    platforms = []

    level = level_1

    x = y = 0
    for row in level:
        for col in row:
            if col == "-":
                pf = Platform(x, y)
                entities_back.add(pf)
                platforms.append(pf)
            if col == "i":
                pf = Spike(x + 7, y)
                entities_back.add(pf)
                platforms.append(pf)
            if col == "s":
                pf = SavePoint(x, y)
                entities_back.add(pf)
                platforms.append(pf)
            if col == "b":
                pf = BonusLife(x, y)
                entities_back.add(pf)
                platforms.append(pf)
            if col == "e":
                pf = Exit(x, y)
                entities_back.add(pf)
                platforms.append(pf)
            if col == "r":
                ball.ring_count += 1

                pf = Ring(x + 17, y)
                entities_back.add(pf)
                platforms.append(pf)

                pf = BackFontRing(x + 17, y - 32)
                entities_back.add(pf)
                platforms.append(pf)

                pf = FrontFontRing(x + 8, y - 32)
                entities_front.add(pf)
                platforms.append(pf)

                pf = Invisible(x + 12, y - 32)
                platforms.append(pf)

                pf = Invisible(x + 12, y + 22)
                platforms.append(pf)

            if col == "v":
                ball.ring_count += 1

                pf = HRing(x + 32, y + 17)
                entities_back.add(pf)
                platforms.append(pf)

                pf = HBackFontRing(x, y + 9)
                entities_front.add(pf)
                platforms.append(pf)

                pf = HFrontFontRing(x, y)
                entities_back.add(pf)
                platforms.append(pf)

                pf = HInvisible(x + 2, y + 8)
                platforms.append(pf)

                pf = HInvisible(x + 54, y + 8)
                platforms.append(pf)

            x += PLATFORM_WIDTH
        y += PLATFORM_HEIGHT
        x = 0

    total_level_width = len(level[0]) * PLATFORM_WIDTH
    total_level_height = len(level) * PLATFORM_HEIGHT

    camera = Camera(camera_configure, total_level_width, total_level_height)
    timer = pygame.time.Clock()

    while True:

        timer.tick(60)

        for e in pygame.event.get():
            if e.type == QUIT:
                raise SystemExit
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYUP and e.key == K_UP:
                up = False

        screen.blit(background, (0, 0))
        ball.update(left, right, up, platforms)
        camera.update(ball)

        for e in entities_back:
            screen.blit(e.image, camera.apply(e))

        screen.blit(ball.image, camera.apply(ball))

        for e in entities_front:
            screen.blit(e.image, camera.apply(e))

        screen.blit(score_ground, (0, 8 * 32))
        score = my_font.render(ball.Score, True, (255, 255, 255))
        screen.blit(score, (5 * 32, 8 * 32 + 5))

        x = 10
        y = 8 * 32 + 3
        for i in range(ball.lifes):
            screen.blit(ball.life_image, (x, y))
            x += 26

        x = 10
        y = 9 * 32
        for i in range(ball.ring_count):
            screen.blit(ball.ring_image, (x, y))
            x += 18

        if ball.is_game_over():
            raise SystemExit

        pygame.display.update()
