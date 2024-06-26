from ..core import AbstractTool
from ..enums.colors import Colors

from qtpy.QtGui import QColor


class Color(AbstractTool, QColor):
    def __init__(self, *color, **kwargs):
        if color.__len__() and isinstance(color[0], Colors):
            color = (color.value,)

        QColor.__init__(self, *color)
        super().__init__(**kwargs)