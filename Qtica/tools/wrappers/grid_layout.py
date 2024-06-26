from typing import Union

from qtpy.QtWidgets import QWidget, QLayout, QLayoutItem
from qtpy.QtCore import Qt


class GridLayoutWrapper:
    def __init__(
        self,
        *,
        child: Union[QWidget, QLayout, QLayoutItem],
        row: int,
        column: int,
        rspan: int = 1,
        cspan: int = 1,
        align: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignCenter
    ) -> None:

        self.child = child
        self.row = row
        self.column = column
        self.rspan = rspan
        self.cspan = cspan
        self.align = align