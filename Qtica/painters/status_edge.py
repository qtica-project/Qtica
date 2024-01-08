#!/usr/bin/python3

# from enum import Enum, auto
from PySide6.QtGui import QBrush, QColor, QPaintEvent, QPainter, QPen
from PySide6.QtCore import QPointF, QRectF, QSize, Qt
from PySide6.QtWidgets import QWidget
from ..core import AbstractPainter


class StatusEdgePaint(AbstractPainter):
    # class Style(Enum):
    #     ellipse = auto()
    #     rectangle = auto()

    def __init__(self,
                 *,
                 child: QWidget,
                 corner: Qt.Corner = Qt.Corner.BottomRightCorner,
                 pen: QPen = None,
                 brush: QBrush = None,
                 padding: float = 1.5,
                 width: int = 13,
                #  style: Style = Style.ellipse,
                 **kwargs) -> QWidget:

        self._width = width
        self._corner = corner
        self._padding = padding
        # self._style = style

        self._brush = brush
        self._pen = pen

        if not pen:
            self._pen = QPen()
            self._pen.setWidth(3)
            self._pen.setColor(0x151617)

        if not brush:
            self._brush = QBrush()
            self._brush.setColor(Qt.GlobalColor.white)

        return super().__init__(child, **kwargs)

    def set_pen(self, pen: QPen) -> None:
        self._pen = pen
        self.update()

    def set_brush(self, brush: QBrush) -> None:
        self._brush = brush
        self.update()

    def paint(self, event: QPaintEvent) -> None:
        self.super_paintEvent(event)

        painter = QPainter(self._parent)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setPen(self._pen)
        painter.setBrush(self._brush)

        # print(painter.brush().color().name())

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