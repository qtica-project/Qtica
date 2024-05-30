from typing import Union
from PySide6.QtWidgets import QFrame, QLayout, QWidget
from ..core import AbstractWidget


class AbstractContainer(AbstractWidget):
    def __init__(self, child: Union[QWidget, QLayout, list[QWidget]] = None, **kwargs):
        super().__init__(**kwargs)

        if child is not None:
            if isinstance(child, QWidget):
                child.setParent(self)
            elif isinstance(child, QLayout):
                child.setProperty("parent", self)
                self.setLayout(child)
            elif isinstance(child, (list, tuple, set)):
                for sub in child:
                    sub.setParent(self)


class FrameContainer(AbstractContainer, QFrame):
    def __init__(self, *, child: Union[QWidget, QLayout, list[QWidget]] = None, **kwargs):
        QFrame.__init__(self)

        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setFrameShadow(QFrame.Shadow.Raised)

        super().__init__(child, **kwargs)


class WidgetContainer(AbstractContainer, QWidget):
    def __init__(self, *, child: Union[QWidget, QLayout, list[QWidget]] = None, **kwargs):
        QWidget.__init__(self)
        super().__init__(child, **kwargs)


class Container(FrameContainer):
    pass