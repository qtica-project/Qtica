from PySide6.QtWidgets import QPushButton, QToolButton
from PySide6.QtCore import Signal
from ..core import AbstractWidget

class _Button(AbstractWidget):
    long_press = Signal()
    long_repeat = Signal()
    long_release = Signal()
    long_click = Signal()

    def __init__(self, **kwargs):
        self._state = 0

        self.setAutoRepeat(True)
        self.setAutoRepeatDelay(1000)
        self.setAutoRepeatInterval(200)

        super().__init__(**kwargs)

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


class PushButton(_Button, QPushButton):
    def __init__(self, **kwargs):
        QPushButton.__init__(self)
        super().__init__(**kwargs)


class ToolButton(_Button, QToolButton):
    def __init__(self, **kwargs):
        QToolButton.__init__(self)
        super().__init__(**kwargs)