#!/usr/bin/python3
# -*- coding: utf-8 -*-

from typing import Union
from PySide6.QtWidgets import QWidget, QLayout, QGroupBox
from ..core import AbstractWidget


class GroupBox(AbstractWidget, QGroupBox):
    def __init__(self, 
                 *, 
                 child: Union[QWidget, QLayout, list[QWidget]] = None, 
                 **kwargs):
        QGroupBox.__init__(self)
        super().__init__(**kwargs)

        if child is not None:
            if isinstance(child, QLayout):
                child.setProperty("parent", self)
                self.setLayout(child)
            elif isinstance(child, (list, tuple, set)):
                for wg in child:
                    wg.setParent(self)
            else:
                child.setParent(self)