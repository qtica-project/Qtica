from typing import Union
from ..core import AbstractWindow

from qtpy.QtWidgets import QLayout, QMainWindow, QWidget


class MainWindow(AbstractWindow, QMainWindow):
    def __init__(self, *, child: Union[QWidget, QLayout] = None, **kwargs):
        QMainWindow.__init__(self)
        super().__init__(child, **kwargs)