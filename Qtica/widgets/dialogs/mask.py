#!/usr/bin/python3
# coding:utf-8

from typing import Union
from PySide6.QtWidgets import QGraphicsOpacityEffect, QGridLayout, QHBoxLayout, QSpacerItem, QWidget
from PySide6.QtCore import QEasingCurve, QEvent, QPropertyAnimation, QSize, Qt
from PySide6.QtGui import QColor, QIcon, QResizeEvent, QShowEvent
from darkdetect import isDark
from ...core import AbstractDialog
from ...tools import SizePolicy
from ..icon_widget import IconWidget


class MaskDialog(AbstractDialog):
    def __init__(self,
                 *,
                 child: QWidget,
                 mask: QWidget = None,
                 margin: Union[QSize, tuple, int] = 90,
                 enable_animation: bool = True,
                 hide_title_bar: bool = False,
                 **kwargs):
        super().__init__(**kwargs)

        self._child = child
        self._child.closeEvent = lambda e: self.close()

        self._grid_layout = QGridLayout(self)
        self._enable_animation = enable_animation
        self._hide_title_bar = hide_title_bar

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

        if not hide_title_bar and not self._auto_close:
            self.init_title_bar()

        self._grid_layout.addWidget(self._child)
        self._grid_layout.setAlignment(self._child, Qt.AlignmentFlag.AlignCenter)

        self.setGeometry(0, 0, self._parent.width(), self._parent.height())
        self.resize(self._parent.size()) 
        self._mask.resize(self.size())

        if self._auto_close:
            self._mask.mouseReleaseEvent = lambda e: self.close()

    def _set_margin(self, margin) -> QSize:
        if not isinstance(margin, QSize):
            return QSize(*((margin,) * 2 
                           if isinstance(margin, int) 
                           else margin))
        return margin

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

        super().showEvent(e)

    def _resize_child(self):
        w, h =  max(40, self._margin.width()), max(40, self._margin.height())
        self._child.setFixedSize(self.width() - w, self.height() - h)

    def resizeEvent(self, e):
        self._mask.resize(self.size())
        self._resize_child()

    def eventFilter(self, obj, e: QEvent):
        if self.parent() and obj is self.parent().window():
            if e.type() == QEvent.Type.Resize:
                re = QResizeEvent(e)
                self.resize(re.size())
        return super().eventFilter(obj, e)

    def init_title_bar(self):
        def animation_close():
            def _finished():
                opacityEffect.deleteLater()
                self.setGraphicsEffect(None)
                self.close()

            opacityEffect = QGraphicsOpacityEffect(self)
            self.setGraphicsEffect(opacityEffect)

            opacityAni = QPropertyAnimation(opacityEffect, b'opacity', self)
            opacityAni.setStartValue(1)
            opacityAni.setEndValue(0)
            opacityAni.setDuration(100)
            opacityAni.setEasingCurve(QEasingCurve.Type.OutCubic)
            opacityAni.finished.connect(_finished)
            opacityAni.start()

        title_bar = QWidget(self)
        title_bar.setSizePolicy(
            SizePolicy(
                horizontal=SizePolicy.Policy.Expanding,
                vertical=SizePolicy.Policy.Fixed
            )
        )

        close_icon = IconWidget(QIcon.fromTheme("window-close"))
        close_icon.setCursor(Qt.CursorShape.PointingHandCursor)
        close_icon.setFixedSize(22, 22)
        close_icon.mousePressEvent = lambda e: animation_close() if self._enable_animation else self.close()

        h_layout = QHBoxLayout(title_bar)
        h_layout.setContentsMargins(0, 0, 8, 0)
        h_layout.addSpacerItem(QSpacerItem(0, 0, SizePolicy.Policy.Expanding, SizePolicy.Policy.Fixed))
        h_layout.addWidget(close_icon)

        title_bar.setLayout(h_layout)
        self._grid_layout.addWidget(title_bar)