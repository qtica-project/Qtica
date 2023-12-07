from typing import Union
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLayoutItem, QSpacerItem, QVBoxLayout, QWidget, QLayout
from .item_wrapper import VLayoutItemWrapper
from ...core import QObjectBase


class VLayout(QObjectBase, QVBoxLayout):
    def __init__(self,
                 *,
                 children: list[Union[QWidget, QLayout, VLayoutItemWrapper]] = None,
                 **kwargs):
        QVBoxLayout.__init__(self)
        super().__init__(**kwargs)

        self._set_children(children)

    def _set_children(self, children: list[Union[QWidget, QLayout, 
                                                 VLayoutItemWrapper]]) -> None:
        if not children:
            return

        for child in children:
            if isinstance(child, QSpacerItem):
                self.addSpacerItem(child)

            elif isinstance(child, QLayoutItem):
                self.addItem(child)

            elif isinstance(child, QWidget):
                self.addWidget(child)

            elif isinstance(child, QLayout):
                self.addLayout(child)

            elif isinstance(child, VLayoutItemWrapper):
                if isinstance(child.child, QWidget):
                    self.addWidget(*child._yield_attr())

                elif isinstance(child.child, QLayout):
                    self.addLayout(*child._yield_attr())

    @staticmethod
    def add(
            child: QWidget | QLayout,
            stretch: int = None,
            alignment: Qt.AlignmentFlag = None
        ) -> VLayoutItemWrapper:
        return VLayoutItemWrapper(
            child,
            stretch,
            alignment
        )