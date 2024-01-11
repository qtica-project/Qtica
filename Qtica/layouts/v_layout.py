from typing import Union
from PySide6.QtWidgets import QLayoutItem, QSpacerItem, QVBoxLayout, QWidget, QLayout
from ..tools.wrappers.v_layout import VLayoutWrapper, RowLayoutWrapper
from ..utils.alignment import Alignment
from ..core import AbstractQObject


class VLayout(AbstractQObject, QVBoxLayout):
    def __init__(self,
                 *,
                 children: list[Union[QWidget, 
                                      QLayout, 
                                      VLayoutWrapper,
                                      RowLayoutWrapper,
                                      Alignment]] = None,
                 **kwargs):
        QVBoxLayout.__init__(self)
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

            elif isinstance(child, VLayoutWrapper):
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


class RowLayout(VLayout):
    ...