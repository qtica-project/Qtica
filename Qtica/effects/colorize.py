from PySide6.QtWidgets import QGraphicsColorizeEffect, QWidget
from ..core import ObjectDeclarative
from ..tools.color import Color


class ColorizeEffect(ObjectDeclarative, QGraphicsColorizeEffect):
    def __init__(self, 
                 child: QWidget,
                 color: Color = None,
                 strength: float = None, 
                 **kwargs) -> QWidget:
        QGraphicsColorizeEffect.__init__(self, child)
        super().__init__(**kwargs)

        self._set_child(child)
        self._set_color(color)
        self._set_strength(strength)

        return child

    def _set_child(self, child: QWidget):
        child.setGraphicsEffect(self)

    def _set_color(self, color: float):
        if color is not None:
            self.setColor(color)

    def _set_strength(self, strength: float):
        if strength is not None:
            self.setStrength(strength)