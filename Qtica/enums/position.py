from enum import IntEnum, auto


class Positions(IntEnum):
    """
    left   => West
    top    => North
    bottom => South
    right  => East
    center => Center
    """

    left = auto()
    top = auto()
    bottom = auto()
    right = auto()
    center = auto()

    west = left
    north = top
    south = bottom
    east = right
