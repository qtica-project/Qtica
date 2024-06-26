from typing import Union
from ..core import AbstractWidget
from ..core.objects.routes import Routes

from qtpy.QtWidgets import QStackedWidget, QWidget


class StackedWidget(AbstractWidget, QStackedWidget):
    def __init__(self, 
                 *,
                 children: Union[list[QWidget], Routes, dict] = None,
                 **kwargs):
        QStackedWidget.__init__(self)
        super().__init__(**kwargs)

        if not children:
            return

        if isinstance(children, (Routes, dict)):
            self.routes = Routes("/", **children) if isinstance(children, dict) else children
            self.routes._set_stacked(self)
            for route, child in children.items():
                self.routes.add(route, child)
        else:
            for child in children:
                self.addWidget(child)