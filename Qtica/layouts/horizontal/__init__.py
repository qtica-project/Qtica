from typing import Union
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QLayoutItem, QSpacerItem, QWidget, QLayout
from .item_wrapper import HLayoutItemWrapper
from ...core import QObjectBase


class HLayout(QObjectBase, QHBoxLayout):
    def __init__(self,
                 *,
                 children: list[Union[QWidget, QLayout, HLayoutItemWrapper]] = None,
                 **kwargs):
        QHBoxLayout.__init__(self)
        super().__init__(**kwargs)

        self._set_children(children)

    def _set_children(self, children: list[Union[QWidget, QLayout, 
                                                 HLayoutItemWrapper]]) -> None:
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

            elif isinstance(child, HLayoutItemWrapper):
                if isinstance(child.child, QWidget):
                    self.addWidget(*child._yield_attr())

                elif isinstance(child.child, QLayout):
                    self.addLayout(*child._yield_attr())

    @staticmethod
    def wrapper(
            child: QWidget | QLayout,
            stretch: int = None,
            alignment: Qt.AlignmentFlag = None
        ) -> HLayoutItemWrapper:
        return HLayoutItemWrapper(
            child,
            stretch,
            alignment
        )