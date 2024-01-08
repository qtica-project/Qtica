from PySide6.QtWidgets import QWidget, QLayout, QLayoutItem
from PySide6.QtCore import Qt
from typing import Union


class GridLayoutWrapper:
    def __init__(
        self,
        *,
        child: Union[QWidget, QLayout, QLayoutItem],
        row: int,
        col: int,
        rspan: int = 1,
        cspan: int = 1,
        align: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignCenter
    ) -> None:

        self.child = child
        self.row = row
        self.col = col
        self.rspan = rspan
        self.cspan = cspan
        self.align = align