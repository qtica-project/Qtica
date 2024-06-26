from ..core import AbstractQObject
from PySide6.QtWidgets import (
    QWidget,
    QGraphicsBlurEffect,
    QGraphicsColorizeEffect,
    QGraphicsDropShadowEffect,
    QGraphicsOpacityEffect
)


class BlurEffect(AbstractQObject, QGraphicsBlurEffect):
    def __init__(self,  **kwargs) -> QWidget:
        QGraphicsBlurEffect.__init__(self)
        super().__init__(**kwargs)


class ColorizeEffect(AbstractQObject, QGraphicsColorizeEffect):
    def __init__(self, **kwargs) -> QWidget:
        QGraphicsColorizeEffect.__init__(self)
        super().__init__(**kwargs)


class DropShadowEffect(AbstractQObject, QGraphicsDropShadowEffect):
    def __init__(self, **kwargs):
        QGraphicsDropShadowEffect.__init__(self)
        super().__init__(**kwargs)


class OpacityEffect(AbstractQObject, QGraphicsOpacityEffect):
    def __init__(self, **kwargs) -> QWidget:
        QGraphicsOpacityEffect.__init__(self)
        super().__init__(**kwargs)