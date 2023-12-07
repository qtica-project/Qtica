from PySide6.QtWidgets import QStackedLayout, QWidget, QLayoutItem
from ..core import QObjectBase
from typing import Union


class StackedLayout(QObjectBase, QStackedLayout):
    def __init__(self,
                 *,
                 children: list[Union[QWidget, QLayoutItem]] = None,
                 **kwargs):
        QStackedLayout.__init__(self)
        super().__init__(**kwargs)

        self._set_children(children)

    def _set_children(self, children: list[Union[QWidget, QLayoutItem]]) -> None:
        if not children:
            return

        for child in children:
            if isinstance(child, QLayoutItem):
                self.addItem(child)

            elif isinstance(child, QWidget):
                self.addWidget(child)