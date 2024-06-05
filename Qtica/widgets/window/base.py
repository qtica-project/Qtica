#!/usr/bin/python3
# -*- coding: utf-8 -*-

from typing import Union
from PySide6.QtCore import Signal
from PySide6.QtGui import QShowEvent, QCloseEvent
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLayout
)


class BaseWindow(QMainWindow):
    startup_changed = Signal()

    def __init__(self, *, child: Union[QWidget, QLayout] = None, **kwargs):
        QMainWindow.__init__(self)

        self.setAnimated(True)
        self.setUpdatesEnabled(True)

        self.__is_startup = False

        if (home := kwargs.get("home", child)) is not None:
            self._set_home(home)

    def closeEvent(self, event: QCloseEvent) -> None:
        super().closeEvent(event)
        self.__is_startup = False

    def showEvent(self, event: QShowEvent) -> None:
        super().showEvent(event)
        if not self.__is_startup:
            self.__is_startup = True
            self.startup_changed.emit()

    def _set_home(self, home) -> None:
        if isinstance(home, QLayout):
            self.centralwidget = QWidget(self)
            self.centralwidget.setObjectName("centralwidget")
            home.setProperty("parent", self.centralwidget)
            self.centralwidget.setLayout(home)
            self.setCentralWidget(self.centralwidget)
        elif isinstance(home, QWidget):
            home.setParent(self)
            self.setCentralWidget(home)