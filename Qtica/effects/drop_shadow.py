from PySide6.QtWidgets import QGraphicsDropShadowEffect
from ..core import QObjectBase


class DropShadowEffect(QObjectBase, QGraphicsDropShadowEffect):
    def __init__(self, **kwargs):
        QGraphicsDropShadowEffect.__init__(self)
        super().__init__(**kwargs)