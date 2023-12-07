#!/usr/bin/python3


from typing import Union
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenu
from ..tools._widgets.menu import MenuSimpleAction, MenuSection, MenuSeparator
from ..core import WidgetBase


class Menu(WidgetBase, QMenu):
    def __init__(self, 
                 *,
                 children: Union[str, int],
                 **kwargs):
        QMenu.__init__(self)
        super().__init__(**kwargs)

        self._set_children(children)

    def _set_children(self, children):
        if children is not None:
            for child in children:
                if isinstance(child, MenuSeparator):
                    self.addSeparator()

                elif isinstance(child, MenuSection):
                    self.addSection(*child)

                elif isinstance(child, QMenu):
                    child.setParent(self)
                    self.addMenu(child)

                elif isinstance(child, (QAction, MenuSimpleAction)):
                    child.setParent(self)
                    self.addAction(child)