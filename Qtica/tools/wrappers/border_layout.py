from ...enums.position import Positions
from qtpy.QtWidgets import QLayoutItem, QWidget, QWidgetItem


class BorderLayoutWrapper:
    def __init__(self, 
                 child: QWidget | QLayoutItem, 
                 pos: Positions = Positions.left):

        self.pos = pos
        self.item = child

        if isinstance(child, QWidget):
            self.item = QWidgetItem(child)