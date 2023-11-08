from enum import Enum, auto
from darkdetect import theme


class Theme(Enum):
    dark = auto()
    light = auto()
    system = auto()

    @staticmethod
    def system_theme():
        return Theme(theme().lower())