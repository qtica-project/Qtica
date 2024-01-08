#!/usr/bin/python3

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from enum import IntFlag


class Alignment:
    Flag: IntFlag = Qt.AlignmentFlag

    def __init__(self,
                 *,
                 child: QWidget,
                 alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignCenter):

        self.child = child
        self.alignment = alignment