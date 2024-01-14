#!/usr/bin/python3
# -*- coding: utf-8 -*-

from typing import Union
from PySide6.QtCore import Signal
from PySide6.QtGui import QShowEvent, QCloseEvent
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget, 
    QToolBar,
    QDockWidget,
    QLayout
)
from ...tools.wrappers import (
    DockWidgetWrapper, 
    ToolBarBreakWrapper, 
    ToolBarWrapper
)


class BaseWindow(QMainWindow):
    startup_changed = Signal()

    def __init__(self, 
                 *,
                 home: Union[QWidget, QLayout] = None,
                 toolbars: list[ToolBarWrapper, ToolBarBreakWrapper, QToolBar, str] = None,
                 dockwidgets: list[DockWidgetWrapper] = None,
                 **kwargs):
        QMainWindow.__init__(self)

        self.setAnimated(True)
        self.setUpdatesEnabled(True)

        self.__is_startup = False

        if home is not None:
            self._set_home(home)
        
        if toolbars is not None:
            self._set_toolbars(toolbars)

        if dockwidgets is not None:
            self._set_dockwidgets(dockwidgets)

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

    def _set_toolbars(self, toolbars) -> None:
        for bar in toolbars:
            if isinstance(bar, ToolBarWrapper):
                self.addToolBar(*[bar.area, bar.toolbar])
            elif isinstance(bar, ToolBarBreakWrapper):
                if bar.area is not None:
                    self.addToolBarBreak(bar.area)
                else:
                    self.addToolBarBreak()
            else:
                self.addToolBar(bar)

    def _set_dockwidgets(self, dockwidgets: QDockWidget) -> None:
        for dock in dockwidgets:
            self.addDockWidget(*[arg for arg in dock._args() if arg is not None])