from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit
from ..enums.events import EventTypeVar
from ..enums.signals import SignalTypeVar
from ..core.base import WidgetBase


class LineEdit(WidgetBase, QLineEdit):
    def __init__(self, 
                 uid: str = None, 
                 signals: SignalTypeVar = None, 
                 events: EventTypeVar = None, 
                 qss: str | dict = None, 
                 attrs: list[Qt.WidgetAttribute] | dict[Qt.WidgetAttribute, bool] = None, 
                 flags: list[Qt.WindowType] | dict[Qt.WindowType, bool] = None, 
                 **kwargs):
        QLineEdit.__init__(self)
        super().__init__(uid, signals, events, qss, attrs, flags, **kwargs)