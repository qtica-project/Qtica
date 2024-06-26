from enum import IntFlag

from qtpy.QtCore import Qt
from qtpy.QtWidgets import QWidget


class Alignment:
    Flag: IntFlag = Qt.AlignmentFlag

    def __init__(self,
                 *,
                 child: QWidget,
                 alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignCenter):

        self.child = child
        self.alignment = alignment