#!/usr/bin/python3

from PySide6.QtCore import QPropertyAnimation
from PySide6.QtWidgets import QWidget
from ..core import QObjectDec


class PropertyAnimation(QObjectDec, QPropertyAnimation):
    def __init__(self,
                 *,
                 target: QWidget,
                 running: bool = False,
                 **kwargs) -> QWidget:
        QPropertyAnimation.__init__(self)

        self.setTargetObject(target)

        super().__init__(**kwargs)

        if running:
            self.start()

        return target