from PySide6.QtWidgets import QToolButton
from PySide6.QtCore import Signal
from ..core import WidgetBase


class ToolButton(WidgetBase, QToolButton):
    long_press = Signal()
    long_repeat = Signal()
    long_release = Signal()
    long_click = Signal()

    def __init__(self, 
                 *,
                 enable_long_press: bool = False,
                 **kwargs):
        QToolButton.__init__(self)
        super().__init__(**kwargs)

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