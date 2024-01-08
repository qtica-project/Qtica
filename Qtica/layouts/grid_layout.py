from typing import Union
from PySide6.QtWidgets import QGridLayout, QWidget, QLayout, QLayoutItem
from ..tools.wrappers.grid_layout import GridLayoutWrapper
from ..tools.alignment import Alignment
from ..core import AbstractQObject


class GridLayout(AbstractQObject, QGridLayout):
    def __init__(self,
                 *,
                 children: list[Union[QWidget, 
                                      QLayoutItem, 
                                      GridLayoutWrapper, 
                                      Alignment]] = None,
                 **kwargs):
        QGridLayout.__init__(self)
        super().__init__(**kwargs)

        if not children:
            return

        for child in children:
            if isinstance(child, Alignment):
                _widget = child.child

                if isinstance(_widget, QWidget):
                    _func = self.addWidget
                elif isinstance(_widget, QLayoutItem):
                    _func = self.addItem

                _func(_widget)
                self.setAlignment(_widget, child.alignment)

            elif isinstance(child, GridLayoutWrapper):
                _widget = child.child

                if isinstance(_widget, QWidget):
                    _func = self.addWidget
                elif isinstance(_widget, QLayoutItem):
                    _func = self.addItem
                elif isinstance(_widget, QLayout):
                    _func = self.addLayout

                _func(_widget, 
                      child.row, 
                      child.col, 
                      child.rspan, 
                      child.cspan, 
                      child.align)

            elif isinstance(child, QLayoutItem):
                self.addItem(child)

            elif isinstance(child, QWidget):
                self.addWidget(child)