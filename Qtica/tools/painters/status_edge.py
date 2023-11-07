#!/usr/bin/python3

from PySide6.QtGui import QBrush, QColor, QPaintEvent, QPainter, QPen
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QRect
from ..painter import Painter


class PaintStatusEdge(Painter):
    def __init__(self, 
            child: QWidget, 
            status_color: QColor = None,
            border_color: QColor = None,
            width: int = None) -> QWidget:

        self._status_color = (
            status_color 
            if status_color is not None 
            else QColor("white")
        )

        self._border_color = (
            border_color 
            if border_color is not None 
            else QColor("#151617")
        )

        self._width = (
            width if width is not None
            else 13
        )

        return super().__init__(child)

    def set_status_color(self, color: QColor):
        self._status_color = color
        self.update()

    def _paint(self, event: QPaintEvent):
        self._parent.__class__.paintEvent(self._parent, event)

        painter = QPainter(self._parent)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        pen = QPen()
        pen.setWidth(3)
        pen.setColor(self._border_color)
        painter.setPen(pen)

        # BRUSH/STATUS COLOR
        painter.setBrush(QBrush(QColor(self._status_color)))

        # DRAW
        rect = QRect(
                self._parent.width() - self._width,
                self._parent.height() - self._width,
                self._width,
                self._width
            )
        painter.drawEllipse(rect)