from typing import Union
from PySide6.QtCore import Signal
from PySide6.QtGui import QShowEvent, QCloseEvent
from PySide6.QtWidgets import (
    QWidget,
    QLayout
)
from .widget import AbstractWidget


class AbstractWindow(AbstractWidget):
    startup_changed = Signal()

    def __init__(self, child: Union[QWidget, QLayout] = None, **kwargs):
        super().__init__(**kwargs)

        self.__is_startup = False

        self._set_child(child)

    def closeEvent(self, event: QCloseEvent) -> None:
        super().closeEvent(event)
        self.__is_startup = False

    def showEvent(self, event: QShowEvent) -> None:
        super().showEvent(event)
        if not self.__is_startup:
            self.__is_startup = True
            self.startup_changed.emit()

    def _set_child(self, child) -> None:
        if isinstance(child, QLayout):
            self.centralwidget = QWidget(self)
            # self.centralwidget.setObjectName("centralwidget")
            child.setProperty("parent", self.centralwidget)
            self.centralwidget.setLayout(child)
            self.setCentralWidget(self.centralwidget)
        elif isinstance(child, QWidget):
            child.setParent(self)
            self.setCentralWidget(child)