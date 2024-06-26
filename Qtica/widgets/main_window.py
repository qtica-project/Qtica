from typing import Union
from PySide6.QtWidgets import QLayout, QMainWindow, QWidget
from ..core import AbstractWindow


class MainWindow(AbstractWindow, QMainWindow):
    def __init__(self, *, child: Union[QWidget, QLayout] = None, **kwargs):
        QMainWindow.__init__(self)
        super().__init__(child, **kwargs)