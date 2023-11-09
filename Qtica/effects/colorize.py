from PySide6.QtWidgets import QGraphicsColorizeEffect, QWidget
from ..core import ObjectBase


class ColorizeEffect(ObjectBase, QGraphicsColorizeEffect):
    def __init__(self, **kwargs) -> QWidget:
        QGraphicsColorizeEffect.__init__(self)
        super().__init__(**kwargs)