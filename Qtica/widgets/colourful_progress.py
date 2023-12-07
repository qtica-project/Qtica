#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PySide6.QtCore import QRect, Qt, QRectF, QLineF
from PySide6.QtGui import QColor, QPainter, QPen, QTransform, QPainterPath
from PySide6.QtWidgets import QProgressBar, QStyleOptionProgressBar
from ..animation.style_animation import ProgressStyleAnimation
from ..core import WidgetBase


class _ColourfulProgressBar(QProgressBar):
    def __init__(self, 
                 color: QColor = QColor(43, 194, 83),
                 fps: int = 60,
                 line_width: int = 50,
                 radius: int = None):
        super(_ColourfulProgressBar, self).__init__()

        self._color = color
        self._fps = fps
        self._lineWidth = line_width
        self._radius = radius
        self._animation = None

    def setColor(self, color: QColor):
        self._color = color
        self.update()

    def setFps(self, fps: int):
        self._fps = max(int(fps), 1)
        self.update()

    def setLineWidth(self, width: int):
        self._lineWidth = max(int(width), 0)
        self.update()

    def setRadius(self, radius: int):
        self._radius = max(int(radius), 1)
        self.update()

    def paintEvent(self, _):
        option = QStyleOptionProgressBar()
        self.initStyleOption(option)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.translate(0.5, 0.5)

        rect = self.rect()
        vertical = self.orientation() == Qt.Orientation.Vertical
        inverted = self.invertedAppearance()
        indeterminate = ((self.minimum() == self.maximum()) 
                         or (self.minimum() < self.value() < self.maximum()))

        if vertical:
            rect = QRect(rect.left(), rect.top(), rect.height(),rect.width())
            m = QTransform.fromTranslate(rect.height(), 0)
            m.rotate(90.0)
            painter.setTransform(m, True)

        maxWidth = rect.width()
        progress = max(self.value(), self.minimum())
        totalSteps = max(1, self.maximum() - self.minimum())
        progressSteps = progress - self.minimum()
        progressBarWidth = int(progressSteps * maxWidth / totalSteps)
        width = progressBarWidth
        radius = max(1, (min(width,
                             self.width() if vertical else self.height()) //
                         4) if self._radius is None else self._radius)

        reverse = (not vertical and
                   self.layoutDirection() == Qt.LayoutDirection.RightToLeft) or vertical
        if inverted:
            reverse = not reverse

        path = QPainterPath()
        if not reverse:
            progressBar = QRectF(rect.left(), rect.top(), width, rect.height())
        else:
            progressBar = QRectF(rect.right() - width, rect.top(), width,
                                 rect.height())

        path.addRoundedRect(progressBar, radius, radius)
        painter.setClipPath(path)

        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(self._color)
        painter.drawRoundedRect(progressBar, radius, radius)

        if not indeterminate:
            if self._animation:
                self._animation.stop()
                self._animation = None
        else:
            color = self._color.lighter(320)
            color.setAlpha(80)
            painter.setPen(QPen(color, self._lineWidth))

            if self._animation:
                step = int(self._animation.animationStep() % self._lineWidth)
            else:
                step = 0
                self._animation = ProgressStyleAnimation(self._fps, self)
                self._animation.start()

            startX = int(progressBar.left() - rect.height() - self._lineWidth)
            endX = int(rect.right() + self._lineWidth)

            if (not inverted and not vertical) or (inverted and vertical):
                lines = [
                    QLineF(x + step, progressBar.bottom(),
                           x + rect.height() + step, progressBar.top())
                    for x in range(startX, endX, self._lineWidth)
                ]
            else:
                lines = [
                    QLineF(x - step, progressBar.bottom(),
                           x + rect.height() - step, progressBar.top())
                    for x in range(startX, endX, self._lineWidth)
                ]
            painter.drawLines(lines)


class ColourfulProgressBar(WidgetBase, _ColourfulProgressBar):
    def __init__(self, 
                 *,
                 color: QColor = QColor(43, 194, 83),
                 fps: int = 60,
                 line_width: int = 50,
                 radius: int = None,
                 **kwargs):
        _ColourfulProgressBar.__init__(self, color, fps, line_width, radius)
        super().__init__(**kwargs)