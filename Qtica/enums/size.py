from enum import IntEnum, auto


class Sizes(IntEnum):
    maximum = auto()
    minimum = auto()
    hint = auto()

    max = maximum
    min = minimum