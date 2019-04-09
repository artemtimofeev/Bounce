#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *

WIN_WIDTH = 9 * 32
WIN_HEIGHT = 8 * 32


class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


def camera_configure(camera, target_rect):
    x_coordinate, y_coordinate, abs, abs = target_rect
    abs, abs, weight, height = camera
    x_coordinate, y_coordinate = (-x_coordinate
                                  + WIN_WIDTH / 2,
                                  -y_coordinate + WIN_HEIGHT / 2)

    x_coordinate = min(0, x_coordinate)
    x_coordinate = max(-(camera.width - WIN_WIDTH), x_coordinate)
    y_coordinate = max(-(camera.height - WIN_HEIGHT), y_coordinate)
    y_coordinate = min(0, y_coordinate)

    return Rect(x_coordinate, y_coordinate, weight, height)
