from typing import Dict, Union
from PySide6.QtCore import Signal
from PySide6.QtGui import QCloseEvent, QShowEvent
from PySide6.QtWidgets import (
    QMainWindow,
    QSystemTrayIcon, 
    QWidget, 
    QToolBar,
    QStatusBar,
    QDockWidget,
    QStackedWidget,
    QLayout
)
from ...utils._routes import Routes
from ...core import WidgetBase


class RoutingWindow(WidgetBase, QMainWindow):
    startup_changed = Signal()

    def __init__(self, 
                 *,
                 index: str = "/",
                 routes: Dict[str, Union[QWidget, QLayout]] = None,
                 stacked_widget: QStackedWidget = None,
                 tool_bar: QToolBar = None,
                 status_bar: QStatusBar = None,
                 dock_widget: QDockWidget = None,
                 sys_tray: QSystemTrayIcon = None,
                 **kwargs):
        QMainWindow.__init__(self)
        super().__init__(**kwargs)

        self.__is_startup = False
        stacked_widget = (stacked_widget 
                          if stacked_widget is not None 
                          else QStackedWidget())

        stacked_widget.setParent(self)
        self._routes = Routes(stacked_widget, index)

        self.setAnimated(True)
        self.setUpdatesEnabled(True)
        self.setDocumentMode(True)

        if routes is not None:
            self._set_routes(routes)

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

    def _set_routes(self, routes: Dict[str, QWidget]) -> None:
        for route, child in routes.items():
            if child is not None:
                if isinstance(child, QLayout):
                    widget = QWidget(self)
                    widget.setLayout(child)
                    self._routes.add(route, widget)
                else:
                    self._routes.add(route, child)

        self.setCentralWidget(self._routes.stackedWidget())

    def _set_tool_bar(self, tool_bar: QToolBar) -> None:
        self.addToolBar(tool_bar)

    def _set_status_bar(self, status_bar: QStatusBar) -> None:
        self.setStatusBar(status_bar)

    def _set_dock_widget(self, dock_widget: QDockWidget) -> None:
        self.addDockWidget(dock_widget)

    def push(self, route: str) -> None:
        self.route.push(route)

    @property
    def route(self) -> Routes:
        return self._routes