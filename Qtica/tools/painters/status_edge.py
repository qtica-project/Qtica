#!/usr/bin/python3

from PySide6.QtGui import QBrush, QColor, QPaintEvent, QPainter, QPen
from PySide6.QtCore import QPointF, QRectF, QSize, Qt
from PySide6.QtWidgets import QWidget
from ...core import PainterBase


class StatusEdgePaint(PainterBase):
    def __init__(self,
                 *,
                 child: QWidget,
                 corner: Qt.Corner = Qt.Corner.BottomRightCorner,
                 status_color: QColor = None,
                 border_color: QColor = None,
                 padding: float = 1.5,
                 width: int = None
                 ) -> QWidget:
        super().__init__(child)

        self._padding = padding
        self._corner = corner

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
            width 
            if width is not None
            else 13
        )

        return self._parent

    def set_status_color(self, color: QColor):
        self._status_color = color
        self.update()

    def update_state(self, color: QColor):
        self._status_color = color
        self.update()

    def _paint(self, event: QPaintEvent):
        # self._parent.__class__.paintEvent(self._parent, event)
        self._super_paintEvent(event)

        painter = QPainter(self._parent)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        pen = QPen()
        pen.setWidth(3)
        pen.setColor(self._border_color)
        painter.setPen(pen)

        # BRUSH/STATUS COLOR
        painter.setBrush(QBrush(QColor(self._status_color)))

        # DRAW
        if self._corner == Qt.Corner.BottomRightCorner:
            point = QPointF((self._parent.width() - self._width) - self._padding,
                            (self._parent.height() - self._width) - self._padding)
        elif self._corner == Qt.Corner.BottomLeftCorner:
            point = QPointF(self._padding, (self._parent.height() - self._width) - self._padding)
        elif self._corner == Qt.Corner.TopRightCorner:
            point = QPointF((self._parent.width() - self._width) - self._padding, self._padding)
        elif self._corner == Qt.Corner.TopLeftCorner:
            point = QPointF(self._padding, self._padding)

        painter.drawEllipse(QRectF(point, QSize(self._width, self._width)))