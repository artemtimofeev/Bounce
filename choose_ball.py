from ball import *


def choose():
    print("Choose your ball: 1 - usual, 2 - fast, 3 - high jump")

    n = int(input())

    if n == 1:
        return Player
    if n == 2:
        return FastPlayer
    if n == 3:
        return HighJumpPlayer
