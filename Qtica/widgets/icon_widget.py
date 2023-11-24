#!/usr/bin/python3

from typing import Union
from PySide6.QtWidgets import QFrame, QGraphicsEffect
from PySide6.QtGui import QIcon, QIconEngine, QImage, QPaintEvent, QPainter, QPixmap
from PySide6.QtCore import Qt
from ..enums._abs_icons import AbstractIcons

from ..core.qstyle_sheet import QStyleSheet
from ..enums.events import EventTypeVar
from ..enums.signals import SignalTypeVar
from ..core.base import WidgetBase
from ..tools.icon import Icon


class IconWidget(WidgetBase, QFrame):
    def __init__(self,
        icon: Union[str,
                    QIcon,
                    QIconEngine,
                    QPixmap,
                    QImage,
                    AbstractIcons],
        alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignCenter,
        mode: QIcon.Mode = QIcon.Mode.Active,
        state: QIcon.State = QIcon.State.On,
        uid: str = None, 
        signals: SignalTypeVar = None, 
        events: EventTypeVar = None, 
        qss: str | dict | QStyleSheet = None, 
        attrs: list[Qt.WidgetAttribute] | dict[Qt.WidgetAttribute, bool] = None, 
        flags: list[Qt.WindowType] | dict[Qt.WindowType, bool] = None, 
        effect: QGraphicsEffect = None, 
        **kwargs):
        QFrame.__init__(self)
        super().__init__(uid, signals, events, qss, attrs, flags, effect, **kwargs)

        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setFrameShadow(QFrame.Shadow.Raised)

        self._icon = Icon(icon)
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