#!/usr/bin/python3

from typing import Union
from PySide6.QtWidgets import QGraphicsEffect
from PySide6.QtCore import QTimer, Qt, Signal
from .qstyle_sheet import QStyleSheet
from ._declarative import AbstractDec
from ._base import AbstractBase


class AbstractWidget(AbstractBase):
    long_pressed: Signal = Signal()

    def __init__(self,
                 *,
                 long_press_delay: int = 1000,
                 effect: QGraphicsEffect = None,
                 qss: Union[str, dict, QStyleSheet] = None,
                 attrs: Union[list[Qt.WidgetAttribute], dict[Qt.WidgetAttribute, bool]] = None,
                 flags: Union[list[Qt.WindowType], dict[Qt.WindowType, bool]] = None,
                 **kwargs):

        self.__long_press_delay: int = long_press_delay

        self.__long_press_timer = QTimer(self)
        self.__long_press_timer.timeout.connect(self.__long_press_timeout)

        self.setMouseTracking(True)
        self.setUpdatesEnabled(True)

        self.setAttribute(Qt.WidgetAttribute.WA_AcceptTouchEvents)

        AbstractBase.__init__(self, **kwargs)

        self._set_qss(
            qss if qss is not None
            else QStyleSheet(qss)
        )

        if effect is not None:
            self._set_effect(effect)

        if attrs is not None:
            self._set_attrs(attrs)

        if flags is not None:
            self._set_flags(flags)

    def _set_effect(self, effect: QGraphicsEffect):
        effect.setParent(self)
        self.setGraphicsEffect(effect)

    def _set_flags(self, flags):
        if isinstance(flags, dict):
            for flag, on in flags.items():
                self.setWindowFlag(flag, on)
        else:
            for flag in flags:
                self.setWindowFlag(flag)

    def _set_attrs(self, attrs: dict):
        if isinstance(attrs, dict):
            for attr, on in attrs.items():
                self.setAttribute(attr, on)
        else:
            for attr in attrs:
                self.setAttribute(attr)

    def _set_qss(self, qss: Union[str, dict, QStyleSheet]):
        self.qss = (QStyleSheet(qss)
                    if isinstance(qss, (str, dict))
                    else qss)
        self.qss._set_parent(self)
        self.qss._set_qss(self.qss._qss)

    def __long_press_timeout(self):
        self.__long_press_timer.stop()
        self.long_pressed.emit()

    def mousePressEvent(self, event):
        self.__long_press_timer.start(self.__long_press_delay)
        return super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.__long_press_timer.stop()
        return super().mouseReleaseEvent(event)


class WidgetDec(AbstractWidget, AbstractDec):
    pass
