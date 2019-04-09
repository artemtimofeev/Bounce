from ball import *


def choose():
    print("Choose your ball: 1 - usual, 2 - fast, 3 - high jump")

    choose = int(input())

    if choose == 1:
        return Player
    if choose == 2:
        return FastPlayer
    if choose == 3:
        return HighJumpPlayer
