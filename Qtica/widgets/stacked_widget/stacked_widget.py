from PySide6.QtWidgets import QStackedWidget, QWidget
from ...core.base import WidgetBase
from ...enums.events import EventTypeVar
from ...enums.signals import SignalTypeVar
from typing import Union


class Routes:
    def __init__(self, 
                 stacked_widget: QStackedWidget = None,
                 index: str = "/") -> None:

        self._stacked_widget = stacked_widget
        self._index = index
        self._routes: dict = {}

    def add(self, route: str, widget: QWidget) -> None:
        self._routes[route] = self._stacked_widget.addWidget(widget)

    def push(self, route: str) -> None:
        self._stacked_widget.setCurrentIndex(self._routes[route])

    def pop(self) -> None:
        self._stacked_widget.setCurrentIndex(self._routes[self._index])

    def remove(self, route: str) -> None:
        index = self._routes.pop(route)
        self._stacked_widget.removeWidget(self.widget(index))

    def stackedWidget(self) -> QStackedWidget:
        return self._stacked_widget


class StackedWidget(WidgetBase, QStackedWidget):
    def __init__(self, 
                 uid: str = None,
                 children: Union[list[QWidget], dict[str, QWidget]] = None,
                 signals: SignalTypeVar = None,
                 events: EventTypeVar = None,
                 **kwargs):
        QStackedWidget.__init__(self)
        super().__init__(uid, signals, events, **kwargs)

        if isinstance(children, dict):
            self._routes = Routes(self, "/")
            self.__setattr__("route", self._routes)
            self.__setattr__("push", lambda route: self._routes.push(route))

        if children is not None:
            self._set_children(children)

    def _set_children(self, children) -> None:
        if not isinstance(children, dict):
            for child in children:
                self.addWidget(child)
        else:
            for route, child in children.items():
                self._routes.add(route, child)