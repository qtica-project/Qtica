from PySide6.QtWidgets import QGraphicsDropShadowEffect
from ..core import ObjectBase


class DropShadowEffect(ObjectBase, QGraphicsDropShadowEffect):
    def __init__(self, **kwargs):
        QGraphicsDropShadowEffect.__init__(self)
        super().__init__(**kwargs)