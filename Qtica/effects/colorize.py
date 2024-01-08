from PySide6.QtWidgets import QGraphicsColorizeEffect, QWidget
from ..core import AbstractQObject


class ColorizeEffect(AbstractQObject, QGraphicsColorizeEffect):
    def __init__(self, **kwargs) -> QWidget:
        QGraphicsColorizeEffect.__init__(self)
        super().__init__(**kwargs)