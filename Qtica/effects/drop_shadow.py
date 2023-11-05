from PySide6.QtCore import QPoint, QPointF
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QWidget
from typing import Union, Tuple
from ..tools import Color
from ..core import ObjectDeclarative


class DropShadowEffect(ObjectDeclarative, QGraphicsDropShadowEffect):
    def __init__(self,
                 child: QWidget,
                 blur_radius: float = None,
                 color: Color = None,
                 offset: Union[QPointF, QPoint, Tuple[float, float], float] = None,
                 **kwargs):
        QGraphicsDropShadowEffect.__init__(self, child)
        super().__init__(**kwargs)

        if blur_radius is not None:
            self.setBlurRadius(blur_radius)

        if color is not None:
            self.setColor(color)

        if offset is not None:
            self.setOffset(*offset 
                           if isinstance(offset, (tuple, list, set)) 
                           else offset)

        return child
