from typing import Union
from PySide6.QtWidgets import QLayoutItem, QSpacerItem, QWidget, QLayout
from ..tools.wrappers.layout import LayoutWrapper
from ..utils.alignment import Alignment
from ..core import AbstractQObject



class VHLayout(AbstractQObject):
    def __init__(self,
                 *,
                 children: list[Union[QWidget, 
                                      QLayout, 
                                      LayoutWrapper,
                                      Alignment]] = None,
                 **kwargs):
        super().__init__(**kwargs)

        if not children:
            return

        for child in children:
            self._add_child(child)

    def _add_child(self, child):
        if isinstance(child, Alignment):
            _widget = child.child

            if isinstance(_widget, QWidget):
                _func = self.addWidget
            elif isinstance(_widget, QLayoutItem):
                _func = self.addItem

            _func(_widget)
            self.setAlignment(_widget, child.alignment)

        elif isinstance(child, LayoutWrapper):
            _widget = child.child

            if isinstance(_widget, QWidget):
                _func = self.addWidget
            elif isinstance(_widget, QLayout):
                _func = self.addLayout

            _func(*child._yield_attr())

        elif isinstance(child, QSpacerItem):
            self.addSpacerItem(child)

        elif isinstance(child, QLayoutItem):
            self.addItem(child)

        elif isinstance(child, QWidget):
            self.addWidget(child)

        elif isinstance(child, QLayout):
            self.addLayout(child)


    def __iadd__(self, other):
        self._add_child(other)
        return self