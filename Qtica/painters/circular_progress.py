from typing import Callable
from ..core import AbstractPainter

from qtpy.QtWidgets import QWidget
from qtpy.QtCore import QRect, QTimer, Qt
from qtpy.QtGui import QColor, QPainter, QPen


class CircularProgressPaint(AbstractPainter):
    def __init__(self,
                 *,
                 child: QWidget,
                 value: int = 0,
                 max_value: int = 100,
                 pen: QPen = None,
                 bg_color: QColor = QColor(0x44475a),
                 bg_enable: bool = False,
                 finished_callback: Callable = None,
                 changed_callback: Callable = None,
                 **kwargs):

        self._value = value
        self._max_value = max_value
        self._bg_enable = bg_enable
        self._bg_color = bg_color
        self._pen = pen

        self._finished_callback = finished_callback if finished_callback is not None else lambda: ...
        self._changed_callback = changed_callback if changed_callback is not None else lambda value: ...

        if not pen:
            self._pen = QPen()
            self._pen.setCapStyle(Qt.PenCapStyle.RoundCap)
            self._pen.setColor(QColor(0x498BD1))
            self._pen.setWidth(10)

        return super().__init__(child, **kwargs)

    def _update_callback(self):
        self._changed_callback(self.value)
        if self.value >= self.max_value:
            self._finished_callback()

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, value: int) -> None:
        self._value = value
        QTimer.singleShot(0, self._update_callback)
        self.repaint()

    @property
    def max_value(self) -> int:
        return self._max_value

    @max_value.setter
    def max_value(self, value: int) -> None:
        self._max_value = value
        self.repaint()

    def setValue(self, value: int):
        self.value = value
        QTimer.singleShot(0, self._update_callback)
        self.repaint()

    def setMaxValue(self, value: int):
        self.max_value = value
        self.repaint()

    def setPen(self, pen: QPen) -> None:
        self._pen = pen
        self.repaint()

    def paint(self, event):
        self.super_paintEvent(event)

        # Set Progress Parameters
        width = self._parent.width() - self._pen.width()
        height = self._parent.height() - self._pen.width()
        margin = self._pen.width() / 2
        value = self.value * 360 / self.max_value

        paint = QPainter()
        paint.begin(self._parent)
        paint.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Create rectangle
        rect = QRect(0, 0, self._parent.width(), self._parent.height())
        paint.setPen(Qt.PenStyle.NoPen)
        paint.drawRect(rect)

        color = self._pen.color()
        if self._bg_enable:
            self._pen.setColor(QColor(0x44475a))
            paint.setPen(self._pen)
            paint.drawArc(margin, margin, width, height, 0, 360 * 16)

        # Create ARC / Circular progress
        self._pen.setColor(color)
        paint.setPen(self._pen)
        paint.drawArc(margin, margin, width, height, -90 * 16, -value * 16)
        paint.end()