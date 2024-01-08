#!/usr/bin/python3

from PySide6.QtWidgets import QLayoutItem, QWidget, QWidgetItem
from ...enums.position import Positions


class BorderLayoutWrapper:
    def __init__(self, 
                 child: QWidget | QLayoutItem, 
                 pos: Positions = Positions.left):

        self.pos = pos
        self.item = child

        if isinstance(child, QWidget):
            self.item = QWidgetItem(child)