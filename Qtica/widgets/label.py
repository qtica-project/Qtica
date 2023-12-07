from PySide6.QtCore import Signal
from PySide6.QtWidgets import QLabel
from ..core import WidgetBase


class Label(WidgetBase, QLabel):
    textChanged = Signal(str)

    def __init__(self, **kwargs):
        QLabel.__init__(self)
        super().__init__(**kwargs)

    def setText(self, arg__1: str) -> None:
        super().setText(arg__1)
        self.textChanged.emit(arg__1)