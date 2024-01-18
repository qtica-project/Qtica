#!/usr/bin/python3

from typing import Union
from PySide6.QtWidgets import QStackedLayout, QStackedWidget, QWidget


class Routes:
    '''
    :Return: dict[str, int]
    '''
    def __init__(self, /, index: str = "/", **kwargs: QWidget) -> None:
        self._index = index
        self._widgets = kwargs

    def _set_stacked(self, stacked: Union[QStackedWidget, QStackedLayout]):
        self._stacked = stacked

    def add(self, route: str, widget: QWidget) -> None:
        self.widgets.__setitem__(route, self._stacked.addWidget(widget))

    def push(self, route: str) -> None:
        self._stacked.setCurrentIndex(self.widgets.__getitem__(route))

    def home(self) -> None:
        self._stacked.setCurrentIndex(self.widgets.__getitem__(self._index))

    def remove(self, route: str) -> None:
        self._stacked.removeWidget(self._stacked.widget(self.widgets.pop(route)))

    def current_route(self) -> str:
        return {v: k for k, v in self.widgets.items()}.get(self._stacked.currentIndex())

    @property
    def stacked(self) -> Union[QStackedWidget, QStackedLayout]:
        return self._stacked
    
    @stacked.setter
    def stacked(self, stacked: Union[QStackedWidget, QStackedLayout]) -> None:
        self._stacked = stacked
    
    @property
    def widgets(self) -> dict:
        return self._widgets