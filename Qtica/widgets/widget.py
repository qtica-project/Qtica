from PySide6.QtWidgets import QWidget, QLayout

from ..enums.events import EventTypeVar
from ..enums.signals import SignalTypeVar
from ..core.base import WidgetBase


class Widget(WidgetBase, QWidget):
    def __init__(self, 
                 uid: str = None, 
                 signals: SignalTypeVar = None, 
                 events: EventTypeVar = None, 
                 child: QWidget | QLayout = None,
                 **kwargs):
        QWidget.__init__(self)
        super().__init__(uid, signals, events, **kwargs)

        self._set_child(child)

    def _set_child(self, child: QWidget | QLayout):
        if child is not None:
            if isinstance(child, QWidget):
                child.setParent(self)

            elif isinstance(child, QLayout):
                child.setProperty("parent", self)
                self.setLayout(child)
            else:
                raise ValueError("the 'child' argument must be one of the QWidget or QLayout instance.")