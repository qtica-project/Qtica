from typing import Union
from PySide6.QtWidgets import QStackedWidget, QWidget
from ...utils._routes import Routes
from ...core import WidgetBase


class StackedWidget(WidgetBase, QStackedWidget):
    def __init__(self, 
                 *,
                 children: Union[list[QWidget], dict[str, QWidget]] = None,
                 **kwargs):
        QStackedWidget.__init__(self)
        super().__init__(**kwargs)

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
                if child is not None:
                    self._routes.add(route, child)