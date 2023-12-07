from PySide6.QtWidgets import QGraphicsBlurEffect, QWidget
from ..core import QObjectBase


class BlurEffect(QObjectBase, QGraphicsBlurEffect):
    def __init__(self,  **kwargs) -> QWidget:
        QGraphicsBlurEffect.__init__(self)
        super().__init__(**kwargs)
