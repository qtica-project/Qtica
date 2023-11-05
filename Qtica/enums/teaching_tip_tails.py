from enum import IntEnum


class TeachingTipTailPositions(IntEnum):
    top = 0
    bottom = 1
    left = 2
    right = 3

    top_left = 4
    top_right = 5

    bottom_left = 6
    bottom_right = 7

    left_top = 8
    left_bottom = 9

    right_top = 10
    right_bottom = 11

    none = 12