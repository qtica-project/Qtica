from typing import TypeAlias, Union
from ...utils.alignment import Alignment
from .._qobject import AbstractQObject
from ..objects import BoxLayoutWrapper

from qtpy.QtWidgets import QLayoutItem, QSpacerItem, QWidget, QLayout


BoxLayoutChildrenType: TypeAlias = list[Union[QWidget, QLayout, BoxLayoutWrapper, Alignment]]


class AbstractBoxLayout(AbstractQObject):
    def __init__(self, children: BoxLayoutChildrenType = None, **kwargs):
        super().__init__(**kwargs)

        if not children:
            return

        for child in children:
            self._add_child(child)

    def _add_child(self, child):
        if isinstance(child, Alignment):
            _widget = child.child

            if isinstance(_widget, QWidget):
                self.addWidget(_widget)
            elif isinstance(_widget, QLayoutItem):
                self.addItem(_widget)

            self.setAlignment(_widget, child.alignment)

        elif isinstance(child, BoxLayoutWrapper):
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