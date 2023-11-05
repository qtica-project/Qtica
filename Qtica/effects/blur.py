from PySide6.QtWidgets import QGraphicsBlurEffect, QWidget
from ..core import ObjectDeclarative


class BlurEffect(ObjectDeclarative, QGraphicsBlurEffect):
    def __init__(self, 
                 child: QWidget,
                 radius: float = None,
                 hints: QGraphicsBlurEffect.BlurHint = None,
                 **kwargs) -> QWidget:
        QGraphicsBlurEffect.__init__(self, child)
        super().__init__(**kwargs)

        self._set_radius(radius)
        self._set_hints(hints)
        self._set_child(child)

        return child

    def _set_child(self, child: QWidget):
        child.setGraphicsEffect(self)

    def _set_radius(self, radius: float):
        if radius is not None:
            self.setBlurRadius(radius)

    def _set_hints(self, hints: QGraphicsBlurEffect.BlurHint):
        if hints is not None:
            self.setBlurHints(hints)