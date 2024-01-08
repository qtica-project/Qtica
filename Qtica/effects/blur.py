from PySide6.QtWidgets import QGraphicsBlurEffect, QWidget
from ..core import AbstractQObject


class BlurEffect(AbstractQObject, QGraphicsBlurEffect):
    def __init__(self,  **kwargs) -> QWidget:
        QGraphicsBlurEffect.__init__(self)
        super().__init__(**kwargs)