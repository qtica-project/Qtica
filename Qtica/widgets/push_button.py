from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QPushButton
from ..enums.events import EventTypeVar
from ..enums.signals import SignalTypeVar
from ..core.base import WidgetBase


class PushButton(WidgetBase, QPushButton):
    long_press = Signal()
    long_repeat = Signal()
    long_release = Signal()
    long_click = Signal()

    def __init__(self, 
                 enable_long_press: bool = False,
                 uid: str = None, 
                 signals: SignalTypeVar = None, 
                 events: EventTypeVar = None, 
                 qss: str | dict = None, 
                 attrs: list[Qt.WidgetAttribute] | dict[Qt.WidgetAttribute, bool] = None, 
                 flags: list[Qt.WindowType] | dict[Qt.WindowType, bool] = None, 
                 **kwargs):
        QPushButton.__init__(self)
        super().__init__(uid, signals, events, qss, attrs, flags, **kwargs)

        self._state = 0

        if enable_long_press:
            self.setAutoRepeat(True)
            self.setAutoRepeatDelay(1000)
            self.setAutoRepeatInterval(200)

        self.clicked.connect(self._handleLongClicked)

    def _handleLongClicked(self):
        if self.isDown():
            if self._state == 0:
                self._state = 1
                self.setAutoRepeatInterval(50)
                self.long_press.emit()
            else:
                self.long_repeat.emit()

        elif self._state == 1:
            self._state = 0
            self.setAutoRepeatInterval(200)
            self.long_release.emit()

        else:
            self.long_click.emit()