from typing import Union
from PySide6.QtGui import QShowEvent, QCloseEvent
from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QMainWindow, 
    QWidget, 
    QToolBar,
    QStatusBar,
    QDockWidget,
    QLayout
)
from ...enums.events import EventTypeVar
from ...enums.signals import SignalTypeVar
from ...core.base import WidgetBase


class MainWindow(WidgetBase, QMainWindow):
    startup_changed = Signal()

    def __init__(self, 
                 uid: str = None, 
                 signals: SignalTypeVar = None, 
                 events: EventTypeVar = None, 
                 home: Union[QWidget, QLayout] = None,
                 tool_bar: QToolBar = None,
                 status_bar: QStatusBar = None,
                 dock_widget: QDockWidget = None,
                 **kwargs):
        QMainWindow.__init__(self)
        super().__init__(uid, signals, events, **kwargs)

        self.__is_startup = False

        self.setAnimated(True)
        self.setUpdatesEnabled(True)

        if home is not None:
            self._set_home(home)
        
        if tool_bar is not None:
            self._set_tool_bar(tool_bar)

        if status_bar is not None:
            self._set_status_bar(status_bar)

        if dock_widget is not None:
            self._set_dock_widget(dock_widget)

    def closeEvent(self, event: QCloseEvent) -> None:
        self.__is_startup = False
        return super().closeEvent(event)

    def showEvent(self, event: QShowEvent) -> None:
        if not self.__is_startup:
            self.__is_startup = True
            self.startup_changed.emit()

        return super().showEvent(event)

    def _set_home(self, home: QWidget) -> None:
        if isinstance(home, QLayout):
            self.centralwidget = QWidget(self)
            self.centralwidget.setObjectName("centralwidget")
            home.setProperty("parent", self.centralwidget)
            self.centralwidget.setLayout(home)
            self.setCentralWidget(self.centralwidget)

        elif isinstance(home, QWidget):
            home.setParent(self)
            self.setCentralWidget(home)

        else:
            raise ValueError("the 'home' argument must be one of \
                the QWidget or QLayout instance.")

    def _set_tool_bar(self, tool_bar: QToolBar) -> None:
        self.addToolBar(tool_bar)

    def _set_status_bar(self, status_bar: QStatusBar) -> None:
        self.setStatusBar(status_bar)

    def _set_dock_widget(self, dock_widget: QDockWidget) -> None:
        self.addDockWidget(dock_widget)
