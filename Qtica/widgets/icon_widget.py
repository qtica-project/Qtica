#!/usr/bin/python3

from typing import Union
from PySide6.QtGui import QColor, QIcon, QIconEngine, QImage, QPaintEvent, QPainter, QPixmap
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QSize, Qt
from ..core import AbstractIcon
from ..core import WidgetBase
from ..tools.icon import Icon


class IconWidget(WidgetBase, QWidget):
    def __init__(self,
                 *,
                icon: Union[str,
                            QIcon,
                            QIconEngine,
                            QPixmap,
                            QImage,
                            AbstractIcon],
                alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignHCenter,
                mode: QIcon.Mode = QIcon.Mode.Active,
                state: QIcon.State = QIcon.State.On,
                color: QColor = None,
                size: Union[QSize, tuple, int] = None,
                **kwargs):
        QWidget.__init__(self)
        super().__init__(**kwargs)

        self._icon = Icon(icon, color, size)
        self._alignment = alignment
        self._mode = mode
        self._state = state

    def paintEvent(self, event: QPaintEvent) -> None:
        super().paintEvent(event)

        painter = QPainter(self)
        painter.setRenderHints(QPainter.RenderHint.Antialiasing 
                               | QPainter.RenderHint.SmoothPixmapTransform
                               | QPainter.RenderHint.TextAntialiasing)

        self._icon.paint(painter, 
                         self.rect(),
                         self._alignment, 
                         self._mode, 
                         self._state)