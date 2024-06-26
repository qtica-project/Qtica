from typing import Union
from ..tools import MenuAction
from ..core import AbstractWidget
from ..tools.wrappers.menu import (
    MenuSectionWrapper, 
    MenuSeparatorWrapper
)

from qtpy.QtGui import QAction
from qtpy.QtWidgets import QMenu


class Menu(AbstractWidget, QMenu):
    def __init__(self, 
                 *,
                 children: list[Union[MenuSeparatorWrapper, 
                                      MenuSectionWrapper, 
                                      MenuAction,
                                      QMenu, 
                                      QAction]],
                 **kwargs):
        QMenu.__init__(self)
        super().__init__(**kwargs)

        if not children:
            return

        for child in children:
            if isinstance(child, MenuSeparatorWrapper):
                self.addSeparator()

            elif isinstance(child, MenuSectionWrapper):
                self.addSection(*child)

            elif isinstance(child, (QAction, MenuAction)):
                child.setParent(self)
                self.addAction(child)

            elif isinstance(child, QMenu):
                child.setParent(self)
                self.addMenu(child)