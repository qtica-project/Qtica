from typing import Tuple, Union
from PySide6.QtCore import QMargins
from PySide6.QtWidgets import QFrame, QLayout, QWidget
from ..core import WidgetBase


class Container(WidgetBase, QFrame):
    def __init__(self, 
                 *,
                 child: Union[QWidget, QLayout] = None,
                 padding: Union[QMargins, Tuple[int, int, int, int]] = None,
                 **kwargs):
        QFrame.__init__(self)
        super().__init__(**kwargs)

        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setFrameShadow(QFrame.Shadow.Raised)

        if child is not None:
            if isinstance(child, QWidget):
                child.setParent(self)
                if padding is not None:
                    self.setContentsMargins(*padding
                                            if isinstance(padding, (tuple, list))
                                            else padding)

            elif isinstance(child, QLayout):
                child.setProperty("parent", self)
                self.setLayout(child)
                if padding is not None:
                    self.setContentsMargins(*padding 
                                            if isinstance(padding, (tuple, list)) 
                                            else padding)
            else:
                raise ValueError("the 'child' argument must be one of the QWidget or QLayout instance.")


class Frame(Container):
    pass