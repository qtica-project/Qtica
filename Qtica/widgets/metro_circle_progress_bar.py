#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide6.QtCore import (
    QSequentialAnimationGroup, 
    QPauseAnimation, 
    QPropertyAnimation,
    QParallelAnimationGroup, 
    QObject, 
    QSize, 
    Qt, 
    QRectF, 
    Signal, 
    Property
)
from PySide6.QtGui import QPainter, QColor
from PySide6.QtWidgets import QWidget
from ..core import WidgetBase


def _qBound(miv, cv, mxv):
    return max(min(cv, mxv), miv)


class CircleItem(QObject):
    _x: int = 0 
    _opacity: int = 1
    value_changed = Signal()

    @Property(float)
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, x: float):
        self._x = x
        self.value_changed.emit()

    @Property(float)
    def opacity(self) -> float:
        return self._opacity

    @opacity.setter
    def opacity(self, opacity: float):
        self._opacity = opacity


class _MetroCircleProgress(QWidget):
    radius: int = 5
    color = QColor(24, 189, 155)
    bg_color = QColor(Qt.GlobalColor.transparent)

    def __init__(self, 
                 radius: int = 5, 
                 color: QColor = QColor(24, 189, 155),
                 bg_color: QColor = QColor(Qt.GlobalColor.transparent)):
        super(_MetroCircleProgress, self).__init__()

        self.radius = radius
        self.color = color
        self.bg_color = bg_color
        self._items = []

        self._initAnimations()

    def setRadius(self, radius: int):
        if self.radius != radius:
            self.radius = radius

    def setColor(self, color: QColor):
        if self.color != color:
            self.color = color
            self.update()

    def setBackgroundColor(self, bg_color: QColor):
        if self.bg_color != bg_color:
            self.bg_color = bg_color
            self.update()

    def paintEvent(self, event):
        super(_MetroCircleProgress, self).paintEvent(event)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.fillRect(self.rect(), self.bg_color)
        painter.setPen(Qt.PenStyle.NoPen)

        for item, _ in self._items:
            painter.save()
            color = self.color.toRgb()
            color.setAlphaF(item.opacity)
            painter.setBrush(color)
            # 5<= radius <=10
            radius = _qBound(self.radius, self.radius / 200 *
                            self.height(), 2 * self.radius)
            diameter = 2 * radius
            painter.drawRoundedRect(
                QRectF(
                    item.x / 100 * self.width() - diameter,
                    (self.height() - radius) / 2,
                    diameter, diameter
                ), radius, radius)
            painter.restore()

    def _initAnimations(self):
        for index in range(5):
            item = CircleItem(self)
            item.value_changed.connect(self.update)

            seqAnimation = QSequentialAnimationGroup(self)
            seqAnimation.setLoopCount(-1)
            self._items.append((item, seqAnimation))

            seqAnimation.addAnimation(QPauseAnimation(150 * index, self))

            parAnimation1 = QParallelAnimationGroup(self)
            parAnimation1.addAnimation(QPropertyAnimation(
                item, b'opacity', self, duration=400, startValue=0, endValue=1.0))
            parAnimation1.addAnimation(QPropertyAnimation(
                item, b'x', self, duration=400, startValue=0, endValue=25.0))
            seqAnimation.addAnimation(parAnimation1)

            seqAnimation.addAnimation(QPropertyAnimation(
                item, b'x', self, duration=2000, startValue=25.0, endValue=75.0))

            parAnimation2 = QParallelAnimationGroup(self)
            parAnimation2.addAnimation(QPropertyAnimation(
                item, b'opacity', self, duration=400, startValue=1.0, endValue=0))
            parAnimation2.addAnimation(QPropertyAnimation(
                item, b'x', self, duration=400, startValue=75.0, endValue=100.0))
            seqAnimation.addAnimation(parAnimation2)

            seqAnimation.addAnimation(
                QPauseAnimation((5 - index - 1) * 150, self))

        for _, animation in self._items:
            animation.start()

    def sizeHint(self):
        return QSize(100, self.radius * 2)


class MetroCircleProgress(WidgetBase, _MetroCircleProgress):
    def __init__(self,
                 *,
                 radius: int = 5, 
                 color: QColor = QColor(24, 189, 155),
                 bg_color: QColor = QColor(Qt.GlobalColor.transparent), 
                 **kwargs):
        _MetroCircleProgress.__init__(self, radius, color, bg_color)
        super().__init__(**kwargs)