from PySide6.QtWidgets import QGraphicsOpacityEffect, QWidget
from ..core import ObjectDeclarative


class OpacityEffect(ObjectDeclarative, QGraphicsOpacityEffect):
    def __init__(self,
                 child: QWidget,
                 opacity: float = None,
                 **kwargs) -> QWidget:
        QGraphicsOpacityEffect.__init__(self, child)
        super().__init__(**kwargs)

        self._set_opacity(opacity)
        self._set_child(child)

        return child

    def _set_child(self, child: QWidget):
        child.setGraphicsEffect(self)

    def _set_opacity(self, opacity: float):
        if opacity is not None:
            self.setOpacity(opacity)