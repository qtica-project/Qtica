#!/usr/bin/python3
# coding:utf-8

from typing import Union
from PySide6.QtWidgets import QGraphicsOpacityEffect, QGridLayout, QWidget
from PySide6.QtCore import QEasingCurve, QPropertyAnimation, QSize, Qt
from PySide6.QtGui import QColor, QShowEvent
from darkdetect import isDark
from ...core import AbstractDialog


class MaskDialog(AbstractDialog):
    def __init__(self,
                 *,
                 child: QWidget,
                 mask: QWidget = None,
                 margin: Union[QSize, tuple, int] = 90,
                 enable_animation: bool = True,
                 **kwargs):
        super().__init__(**kwargs)

        self._child = child
        self._child.closeEvent = self._child_close_event

        self._grid_layout = QGridLayout(self)
        self._enable_animation = enable_animation

        self._margin = self._set_margin(margin)

        if mask is not None:
            self._mask = mask
            self._mask.setParent(self)
        else:
            self._mask = QWidget(self)
            color = QColor(0, 0, 0, 76)
            self._mask.setStyleSheet(f"""
                background: rgba({color.red()}, \
                    {color.blue()}, \
                        {color.green()}, \
                            {color.alpha()})
                            """)
            c = 0 if isDark() else 255
            self._mask.setStyleSheet(f'background: rgba({c}, {c}, {c}, 0.6)')

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self._grid_layout.addWidget(self._child)
        self._grid_layout.setAlignment(self._child, Qt.AlignmentFlag.AlignCenter)

        self.setGeometry(0, 0, self._parent.width(), self._parent.height())
        self.resize(self._parent.size()) 
        self._mask.resize(self.size())

    def _set_margin(self, margin) -> QSize:
        if not isinstance(margin, QSize):
            return QSize(*((margin,) * 2 
                           if isinstance(margin, int) 
                           else margin))
        return margin

    def _child_close_event(self, e):
        self.close()

    def showEvent(self, e: QShowEvent) -> None:
        if self._enable_animation:
            def _finished():
                opacityEffect.deleteLater()
                self.setGraphicsEffect(None)

            opacityEffect = QGraphicsOpacityEffect(self)
            self.setGraphicsEffect(opacityEffect)

            opacityAni = QPropertyAnimation(opacityEffect, b'opacity', self)
            opacityAni.setStartValue(0)
            opacityAni.setEndValue(1)
            opacityAni.setDuration(200)
            opacityAni.setEasingCurve(QEasingCurve.Type.InSine)
            opacityAni.finished.connect(_finished)
            opacityAni.start()

        return super().showEvent(e)

    def _resize_child(self):
        w, h =  max(40, self._margin.width()), max(40, self._margin.height())
        self._child.setFixedSize(self.width() - w, self.height() - h)

    def resizeEvent(self, e):
        self._mask.resize(self.size())
        self._resize_child()