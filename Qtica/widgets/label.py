from ..core import AbstractWidget

from qtpy.QtCore import Signal
from qtpy.QtGui import QMovie
from qtpy.QtWidgets import QLabel


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