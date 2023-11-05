from typing import Any, Union, Tuple, Optional
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QRgba64
from ..core.base import BehaviorDeclarative
from ..enums.colors import Colors


class Color(BehaviorDeclarative):
    '''
    Color(Colors.red) -> QColor
    '''
    def __init__(self, 
                 color: Union[QColor, 
                              QRgba64, 
                              Any,
                              Qt.GlobalColor, 
                              Colors,
                              str, int, 
                              Tuple[int, int, int, Optional[int]],
                              Tuple[QColor.Spec, int, int, int, int, Optional[int]]]) -> QColor:
        super().__init__()

        if isinstance(color, Colors):
            return color.value
 
        if isinstance(color, (list, tuple)):
            return QColor(*color)

        if type(color) == QColor:
            return color

        return QColor(color)