#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math

from PySide6.QtCore import QPoint, QRect, QSizeF, QTimer, Qt, QRectF, QSize
from PySide6.QtGui import QPainter, QPainterPath, QColor
from PySide6.QtWidgets import QProgressBar


class _WaterRippleProgressBar(QProgressBar):
    water_height: int = 1
    water_density: int = 1
    style_type: int = 1
    border_radius: int = 8
    text_color: Qt.GlobalColor = Qt.GlobalColor.white
    bg_color: Qt.GlobalColor = Qt.GlobalColor.gray
    fg_water_color: QColor = QColor(33, 178, 148)
    bg_water_color: QColor = QColor(33, 178, 148, 100)

    def __init__(self) -> None:
        super(_WaterRippleProgressBar, self).__init__()

        self._offset = 0

        self._updateTimer = QTimer(self, timeout=self.update)
        self._updateTimer.start(100)

    def setRange(self, min: int, max: int):
        if min == max == 0:
            return

        super(_WaterRippleProgressBar, self).setRange(min, max)

    def setMinimum(self, value: int):
        if value == self.maximum() == 0:
            return

        super(_WaterRippleProgressBar, self).setMinimum(value)

    def setMaximum(self, value):
        if value == self.minimum() == 0:
            return

        super(_WaterRippleProgressBar, self).setMaximum(value)

    def setWaterHeight(self, height):
        self.water_height = height
        self.update()

    def setWaterDensity(self, density):
        self.water_density = density
        self.update()

    def setStyleType(self, style):
        self.style_type = style
        self.update()

    def setBorderRadius(self, border_radius: int):
        self.border_radius = border_radius
        self.update()

    def sizeHint(self):
        return QSize(100, 100)

    def paintEvent(self, event):
        if self.minimum() == self.maximum() == 0:
            return

        percent = 1 - (self.value() - self.minimum()) / \
                  (self.maximum() - self.minimum())

        w = 6 * self.water_density * math.pi / self.width()
        A = self.height() * self.water_height * 1 / 26
        k = self.height() * percent

        waterPath1 = QPainterPath()
        waterPath1.moveTo(0, self.height())
        waterPath2 = QPainterPath()
        waterPath2.moveTo(0, self.height())

        self._offset += 0.6
        if self._offset > self.width() / 2:
            self._offset = 0

        for i in range(self.width() + 1):
            y = A * math.sin(w * i + self._offset) + k
            waterPath1.lineTo(i, y)

            y = A * math.sin(w * i + self._offset + self.width() / 2 * A) + k
            waterPath2.lineTo(i, y)

        waterPath1.lineTo(self.width(), self.height())
        waterPath1.lineTo(0, self.height())
        waterPath2.lineTo(self.width(), self.height())
        waterPath2.lineTo(0, self.height())

        bgPath = QPainterPath()
        if self.style_type and self.border_radius:
            bgPath.addRoundedRect(QRectF(self.rect()), 
                                  self.border_radius,
                                  self.border_radius)
        elif self.style_type:
            bgPath.addRect(QRectF(self.rect()))
        else:
            radius = min(self.width(), self.height())
            bgPath.addRoundedRect(QRectF(self.rect()), radius, radius)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        painter.setPen(Qt.PenStyle.NoPen)

        if (not self.style_type
            or (self.style_type and self.border_radius)):
            painter.setClipPath(bgPath)

        painter.save()
        painter.setBrush(self.bg_color)
        painter.drawPath(bgPath)
        painter.restore()

        painter.save()
        painter.setBrush(self.bg_water_color)
        painter.drawPath(waterPath1)
        painter.restore()

        painter.save()
        painter.setBrush(self.fg_water_color)
        painter.drawPath(waterPath2)
        painter.restore()

        if self.isTextVisible():
            pixelRatio = self.devicePixelRatioF()
            sz = QSizeF(self.width() * pixelRatio, self.height() * pixelRatio).toSize()
            rect = QRectF(0, 0, self.width() * pixelRatio, self.height() * pixelRatio)

            font = painter.font()
            rectValue = QRect()
            progressText = self.text().strip('%')

            if progressText == '100':
                font.setPixelSize(sz.height() * 35 / 100)
                painter.setFont(font)

                rectValue.setWidth(sz.width() * 60 / 100)
                rectValue.setHeight(sz.height() * 35 / 100)
                rectValue.moveCenter(rect.center().toPoint())

                painter.setPen(self.text_color)
                painter.drawText(rectValue, Qt.AlignmentFlag.AlignCenter, progressText)
            else:
                font.setPixelSize(sz.height() * 40 / 100)
                painter.setFont(font)

                rectValue.setWidth(sz.width() * 45 / 100)
                rectValue.setHeight(sz.height() * 40 / 100)
                rectValue.moveCenter(rect.center().toPoint())
                rectValue.moveLeft(rect.left() + rect.width() * 0.45 * 0.5)

                painter.setPen(self.text_color)
                painter.drawText(rectValue, Qt.AlignmentFlag.AlignCenter, progressText)

                font.setPixelSize(font.pixelSize() / 2)
                painter.setFont(font)
                rectPerent = QRect(QPoint(rectValue.right(), rectValue.bottom() - rect.height() * 20 / 100),
                                   QPoint(rectValue.right() + rect.width() * 20 / 100, rectValue.bottom()))

                painter.drawText(rectPerent, Qt.AlignmentFlag.AlignCenter, '%')


from ..core.base import WidgetBase
from ..enums.events import EventTypeVar
from ..enums.signals import SignalTypeVar


class WaterRippleProgressBar(WidgetBase, _WaterRippleProgressBar):
    '''
    :param:style_type: 0 = rounded, 1 = rectangle
    '''
    def __init__(self,
                 water_height: int = 1,
                 water_density: int = 1,
                 style_type: int = 1,
                 border_radius: int = 8,
                 text_color: Qt.GlobalColor = Qt.GlobalColor.white,
                 bg_color: Qt.GlobalColor = Qt.GlobalColor.gray,
                 fg_water_color: QColor = QColor(33, 178, 148),
                 bg_water_color: QColor = QColor(33, 178, 148, 100),
                 uid: str = None, 
                 signals: SignalTypeVar = None, 
                 events: EventTypeVar = None, 
                 qss: str | dict = None, 
                 attrs: list[Qt.WidgetAttribute] | dict[Qt.WidgetAttribute, bool] = None, 
                 flags: list[Qt.WindowType] | dict[Qt.WindowType, bool] = None, 
                 **kwargs):
        _WaterRippleProgressBar.__init__(self)
        super().__init__(uid, signals, events, qss, attrs, flags, **kwargs)

        self.water_height = water_height
        self.water_density = water_density
        self.style_type = style_type
        self.border_radius = border_radius
        self.text_color = text_color
        self.bg_color = bg_color
        self.fg_water_color = fg_water_color
        self.bg_water_color = bg_water_color