from enum import IntEnum, auto


class Positions(IntEnum):
    left = auto()
    top = auto()
    bottom = auto()
    right = auto()
    center = auto()

    west = left
    north = top
    south = bottom
    east = right