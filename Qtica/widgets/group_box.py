#!/usr/bin/python3
# -*- coding: utf-8 -*-

from typing import Union
from PySide6.QtWidgets import QWidget, QLayout, QGroupBox
from ..core import AbstractWidget


class GroupBox(AbstractWidget, QGroupBox):
    def __init__(self, 
                 *, 
                 child: Union[QWidget, QLayout], 
                 **kwargs):
        QGroupBox.__init__(self)
        super().__init__(**kwargs)

        if isinstance(child, QLayout):
            child.setProperty("parent", self)
            self.setLayout(child)
        else:
            child.setParent(self)