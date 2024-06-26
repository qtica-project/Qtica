from PySide6.QtCore import QPropertyAnimation
from ..core import AbstractQObject


class PropertyAnimation(AbstractQObject, QPropertyAnimation):
    def __init__(self, *, running: bool = True, **kwargs):
        QPropertyAnimation.__init__(self)
        super().__init__(**kwargs)

        self._running = running