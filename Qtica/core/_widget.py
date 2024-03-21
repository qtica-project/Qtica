#!/usr/bin/python3

from dataclasses import dataclass
from typing import Callable, TypeAlias, Union
from PySide6.QtWidgets import QGraphicsEffect
from PySide6.QtCore import QPoint, QPointF, QTimer, Qt, Signal
from .qstyle_sheet import QStyleSheet
from ._declarative import AbstractDec
from ._base import AbstractBase


@dataclass
class PosEventsRange():
    start: int 
    stop: int

    def _start(self) -> int:
        if callable(self.start):
            return self.start()
        return self.start

    def _stop(self) -> int:
        if callable(self.stop):
            return self.stop()
        return self.stop


@dataclass
class PosEventsArg():
    x: int | PosEventsRange
    y: int | PosEventsRange
    callback: Callable

    def _check_var_type(self, _type: object) -> bool:
        return all(isinstance(var, _type) for var in (self.x, self.y))

    def _x_in_range(self, value: int) -> bool:
        return self.x._stop() >= value >= self.x._start()

    def _y_in_range(self, value: int) -> bool:
        return self.y._stop() >= value >= self.y._start()

    def _pos_in_range(self, x: int, y: int) -> bool:
        return self._x_in_range(x) and self._y_in_range(y)

    def _equal_pos(self, x: int, y: int) -> bool:
        return self.x == x and self.y == y


PosEventsTypeVar: TypeAlias = Union[tuple[int, int, Callable],
                                    tuple[Union[QPoint, QPointF], Callable],
                                    tuple[PosEventsRange, PosEventsRange, Callable],
                                    PosEventsArg]
@dataclass(kw_only=True)
class PosEvents():
    clicked: list[PosEventsTypeVar] = None
    double_clicked: list[PosEventsTypeVar] = None
    hover: list[PosEventsTypeVar] = None


class AbstractWidget(AbstractBase):
    long_pressed: Signal = Signal()

    def __init__(self,
                 long_press_delay: int = 1000,
                 effect: QGraphicsEffect = None,
                 qss: Union[str, dict, QStyleSheet] = None,
                 attrs: Union[list[Qt.WidgetAttribute], dict[Qt.WidgetAttribute, bool]] = None,
                 flags: Union[list[Qt.WindowType], dict[Qt.WindowType, bool]] = None,
                 at_pos: PosEvents = None,
                 **kwargs):

        self._at_pos: PosEvents = at_pos
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

    def _on_pos_events_arg(self, pos_event, x, y):
        if pos_event._check_var_type(PosEventsRange) and pos_event._pos_in_range(x, y):
            pos_event.callback()
        elif pos_event._check_var_type(int) and pos_event._equal_pos(x, y):
            pos_event.callback()

    def _on_at_pos(self, at_pos, event):
        for _pos_event in at_pos:
            if isinstance(_pos_event, PosEventsArg):
                pass
            elif len(_pos_event) == 3:
                _pos_event = PosEventsArg(*_pos_event)
            elif len(_pos_event) == 2:
                _pos_event = PosEventsArg(*map(int, _pos_event[0].toTuple()), _pos_event[-1])

            if _pos_event is not None:
                self._on_pos_events_arg(_pos_event, *event.position().toPoint().toTuple())

    def mousePressEvent(self, event) -> None:
        self.__long_press_timer.start(self.__long_press_delay)

        if self._at_pos is not None and self._at_pos.clicked is not None:
            self._on_at_pos(self._at_pos.clicked, event)

        return super().mousePressEvent(event)

    def mouseDoubleClickEvent(self, event) -> None:
        if self._at_pos is not None and self._at_pos.double_clicked is not None:
            self._on_at_pos(self._at_pos.double_clicked, event)

        return super().mouseDoubleClickEvent(event)

    def mouseMoveEvent(self, event) -> None:
        if self._at_pos is not None and self._at_pos.hover is not None:
            self._on_at_pos(self._at_pos.hover, event)

        return super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.__long_press_timer.stop()
        return super().mouseReleaseEvent(event)


class WidgetDec(AbstractWidget, AbstractDec):
    pass
