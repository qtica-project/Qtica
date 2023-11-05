from typing import Tuple, Union
from PySide6.QtCore import QMargins, Qt
from PySide6.QtWidgets import QFrame, QLayout, QWidget

from ..enums.events import EventTypeVar
from ..enums.signals import SignalTypeVar
from ..core.base import WidgetBase


class Container(WidgetBase, QFrame):
    def __init__(self, 
                 child: Union[QWidget, QLayout] = None,
                 padding: Union[QMargins, Tuple[int, int, int, int]] = None,
                 uid: str = None, 
                 signals: SignalTypeVar = None, 
                 events: EventTypeVar = None, 
                 qss: str | dict = None, 
                 attrs: list[Qt.WidgetAttribute] | dict[Qt.WidgetAttribute, bool] = None, 
                 flags: list[Qt.WindowType] | dict[Qt.WindowType, bool] = None, 
                 **kwargs):
        QFrame.__init__(self)
        super().__init__(uid, signals, events, qss, attrs, flags, **kwargs)

        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setFrameShadow(QFrame.Shadow.Plain)

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