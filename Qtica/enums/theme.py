from enum import Enum, auto
from darkdetect import theme


class Theme(Enum):
    dark = auto()
    light = auto()
    system = auto()

    def system_theme(self):
        return Theme(theme().lower())