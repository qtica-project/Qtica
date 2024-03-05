from typing import Union
from PySide6.QtWidgets import QStackedLayout, QWidget, QLayoutItem
from ..utils.alignment import Alignment
from ..core import AbstractQObject, Routes


class StackedLayout(AbstractQObject, QStackedLayout):
    def __init__(self,
                 *,
                 children: Union[list[Union[QWidget, QLayoutItem, Alignment]], Routes, dict] = None,
                 **kwargs):
        QStackedLayout.__init__(self)
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
                if isinstance(child, Alignment):
                    _widget = child.child

                    if isinstance(_widget, QWidget):
                        _func = self.addWidget
                    elif isinstance(_widget, QLayoutItem):
                        _func = self.addItem

                    _func(_widget)
                    self.setAlignment(_widget, child.alignment)

                elif isinstance(child, QLayoutItem):
                    self.addItem(child)

                elif isinstance(child, QWidget):
                    self.addWidget(child)