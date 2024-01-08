#!/usr/bin/python3

from PySide6.QtGui import QColor
from ..core import AbstractTool
from ..enums.colors import Colors


class Color(AbstractTool, QColor):
    def __init__(self, *color, **kwargs):
        if color.__len__() and isinstance(color[0], Colors):
            color = (color.value,)

        QColor.__init__(self, *color)
        super().__init__(**kwargs)