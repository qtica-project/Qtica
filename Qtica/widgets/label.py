from PySide6.QtCore import Signal
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QLabel
from ..core import AbstractWidget


class Label(AbstractWidget, QLabel):
    textChanged = Signal(str)

    def __init__(self, **kwargs):
        QLabel.__init__(self)
        super().__init__(**kwargs)

    def setMovie(self, movie: QMovie) -> None:
        movie.setParent(self)
        super().setMovie(movie)

    def setText(self, arg__1: str) -> None:
        super().setText(arg__1)
        self.textChanged.emit(arg__1)