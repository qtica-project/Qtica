from typing import Union
from PySide6.QtWidgets import QHBoxLayout, QLayoutItem, QSpacerItem, QWidget, QLayout
from ..tools.wrappers.h_layout import HLayoutWrapper, ColumnLayoutWrapper
from ..utils.alignment import Alignment
from ..core import AbstractQObject


class HLayout(AbstractQObject, QHBoxLayout):
    def __init__(self,
                 *,
                 children: list[Union[QWidget, 
                                      QLayout, 
                                      HLayoutWrapper,
                                      ColumnLayoutWrapper,
                                      Alignment]] = None,
                 **kwargs):
        QHBoxLayout.__init__(self)
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

            elif isinstance(child, HLayoutWrapper):
                if isinstance(child.child, QWidget):
                    _func = self.addWidget
                elif isinstance(child.child, QLayout):
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


class ColumnLayout(HLayout):
    ...