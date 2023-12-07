from typing import Union
from PySide6.QtGui import QShowEvent, QCloseEvent
from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QMainWindow,
    QSystemTrayIcon, 
    QWidget, 
    QToolBar,
    QStatusBar,
    QDockWidget,
    QLayout
)
from ...core import WidgetBase


class MainWindow(WidgetBase, QMainWindow):
    startup_changed = Signal()

    def __init__(self, 
                 *,
                 home: Union[QWidget, QLayout] = None,
                 tool_bar: QToolBar = None,
                 status_bar: QStatusBar = None,
                 dock_widget: QDockWidget = None,
                 sys_tray: QSystemTrayIcon = None,
                 **kwargs):
        QMainWindow.__init__(self)
        super().__init__(**kwargs)

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

        if sys_tray is not None:
            sys_tray.setParent(self)
            sys_tray.show()

    def closeEvent(self, event: QCloseEvent) -> None:
        super().closeEvent(event)
        self.__is_startup = False

    def showEvent(self, event: QShowEvent) -> None:
        super().showEvent(event)
        if not self.__is_startup:
            self.__is_startup = True
            self.startup_changed.emit()

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
