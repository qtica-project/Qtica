from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtWidgets import QLabel
from ..enums.events import EventTypeVar
from ..enums.signals import SignalTypeVar
from ..core.base import WidgetBase


class Label(WidgetBase, QLabel):
    textChanged = Signal(str)

    def __init__(self, 
                 uid: str = None, 
                 signals: SignalTypeVar = None, 
                 events: EventTypeVar = None, 
                 qss: str | dict = None, 
                 attrs: list[Qt.WidgetAttribute] | dict[Qt.WidgetAttribute, bool] = None, 
                 flags: list[Qt.WindowType] | dict[Qt.WindowType, bool] = None, 
                 **kwargs):
        QLabel.__init__(self)
        super().__init__(uid, signals, events, qss, attrs, flags, **kwargs)

    @Slot(str)
    def setText(self, arg__1: str) -> None:
        super().setText(arg__1)
        self.textChanged.emit(arg__1)