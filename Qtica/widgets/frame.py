from typing import Tuple, Union
from PySide6.QtWidgets import QFrame, QLayout, QWidget
from PySide6.QtCore import QMargins
from ..core import AbstractWidget


class Frame(AbstractWidget, QFrame):
    def __init__(self, 
                 *,
                 child: Union[QWidget, QLayout] = None,
                 padding: Union[QMargins, Tuple[int, int, int, int]] = None,
                 **kwargs):
        QFrame.__init__(self)

        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setFrameShadow(QFrame.Shadow.Raised)

        super().__init__(**kwargs)

        if child is not None:
            if isinstance(child, QWidget):
                child.setParent(self)

            elif isinstance(child, QLayout):
                child.setProperty("parent", self)
                self.setLayout(child)

            if padding is not None:
                self.setContentsMargins(*padding if isinstance(padding, (tuple, list)) else padding)


class Container(Frame):
    ...