from typing import Any, Union, Optional
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QRgba64
from ..core.base import BehaviorDeclarative
from ..enums.colors import Colors


class Color(BehaviorDeclarative):
    '''
    e.g Color(Colors.red) -> QColor
    '''
    def __init__(self,
                 color: Union[QColor, 
                              QRgba64, 
                              Any,
                              Qt.GlobalColor, 
                              Colors,
                              str, 
                              int, 
                              tuple[int, int, int, Optional[int]],
                              tuple[QColor.Spec, 
                                    int, 
                                    int, 
                                    int, 
                                    int, 
                                    Optional[int]]]) -> QColor:

        if isinstance(color, Colors):
            return color.value

        if isinstance(color, (list, tuple)):
            return QColor(*color)

        if type(color) == QColor:
            return color

        return QColor(color)