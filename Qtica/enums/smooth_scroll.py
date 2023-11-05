from enum import IntEnum


class SmoothMode(IntEnum):
    """ Smooth mode """

    normal = 0
    constant = 1
    linear = 2
    quadrati = 3
    cosine = 4