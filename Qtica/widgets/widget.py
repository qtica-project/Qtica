from typing import Union
from PySide6.QtWidgets import QWidget, QLayout
from ..core import AbstractWidget


class Widget(AbstractWidget, QWidget):
    def __init__(self, *, child: Union[QWidget, QLayout] = None, **kwargs):
        QWidget.__init__(self)
        super().__init__(**kwargs)

        if child is not None:
            if isinstance(child, QWidget):
                child.setParent(self)

            elif isinstance(child, QLayout):
                child.setProperty("parent", self)
                self.setLayout(child)