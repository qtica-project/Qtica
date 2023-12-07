#!/usr/bin/python3

from PySide6.QtWidgets import QStackedWidget, QWidget


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

    def current_route(self) -> str:
        return {v: k for k, v in self._routes.items()}.get(
            self._stacked_widget.currentIndex()
        )

    def stackedWidget(self) -> QStackedWidget:
        return self._stacked_widget
