from PySide6.QtWidgets import QGraphicsOpacityEffect, QWidget
from ..core import QObjectBase


class OpacityEffect(QObjectBase, QGraphicsOpacityEffect):
    def __init__(self, **kwargs) -> QWidget:
        QGraphicsOpacityEffect.__init__(self)
        super().__init__(**kwargs)