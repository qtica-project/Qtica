from typing import Union
from PySide6.QtWidgets import QStackedLayout, QWidget, QLayoutItem
from ..tools.alignment import Alignment
from ..core import AbstractQObject


class StackedLayout(AbstractQObject, QStackedLayout):
    def __init__(self,
                 *,
                 children: list[Union[QWidget, QLayoutItem, Alignment]] = None,
                 **kwargs):
        QStackedLayout.__init__(self)
        super().__init__(**kwargs)

        if not children:
            return

        for child in children:
            if isinstance(child, Alignment):
                _widget = child.child

                if isinstance(child.child, QWidget):
                    _func = self.addWidget
                elif isinstance(child.child, QLayoutItem):
                    _func = self.addItem

                _func(_widget)
                self.setAlignment(_widget, child.alignment)

            elif isinstance(child, QLayoutItem):
                self.addItem(child)

            elif isinstance(child, QWidget):
                self.addWidget(child)