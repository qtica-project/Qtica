#!/usr/bin/python3

from typing import Union
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import (
    QColor, 
    QIcon, 
    QIconEngine, 
    QImage, 
    QMovie, 
    QPaintEvent, 
    QPainter, 
    QPixmap
)
from ..core import AbstractIcons, AbstractWidget
from ..tools.icon import Icon


class IconWidget(AbstractWidget, QWidget):
    def __init__(self,
                icon: Union[str,
                            QIcon,
                            QIconEngine,
                            QPixmap,
                            QImage,
                            AbstractIcons,
                            QMovie],
                *,
                alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignHCenter,
                mode: QIcon.Mode = QIcon.Mode.Active,
                state: QIcon.State = QIcon.State.On,
                color: QColor = None,
                size: Union[QSize, tuple, int] = None,
                **kwargs):
        QWidget.__init__(self)
        super().__init__(**kwargs)

        if isinstance(icon, QMovie):
            self._icon = icon
            icon.frameChanged.connect(self.update)
        else:
            self._icon = Icon(icon, color, size)
            self._alignment = alignment
            self._mode = mode
            self._state = state

    @property
    def icon(self) -> QIcon:
        return self._icon

    @icon.setter
    def icon(self, icon) -> None:
        self._icon = Icon(icon)

    def paintEvent(self, event: QPaintEvent) -> None:
        super().paintEvent(event)

        painter = QPainter(self)
        painter.setRenderHints(QPainter.RenderHint.Antialiasing 
                               | QPainter.RenderHint.SmoothPixmapTransform
                               | QPainter.RenderHint.TextAntialiasing)

        if isinstance(self.icon, QMovie):
            painter.drawPixmap(self.rect(), 
                               self.icon.currentPixmap())
        else:
            painter.drawPixmap(self.rect(), 
                               self._icon.pixmap(self.rect().size(), 
                                                 self._mode, 
                                                 self._state))
    
    def setIcon(self, icon) -> None:
        self._icon = Icon(icon)
        self.update()