from typing import TypeAlias, Union
from .._base import AbstractBase
from .._declarative import AbstractDec
from ...utils.key_events import MouseButtons, Modifiers
from ..objects import PosEvents, PosEventsRange, PosEventsArg, QStyleSheet

from PySide6.QtWidgets import QGraphicsEffect
from PySide6.QtCore import QAbstractAnimation, QAnimationGroup,QTimer, QVariantAnimation, Qt, Signal


QssType: TypeAlias = Union[str, dict, QStyleSheet]
WidgetAttrsType: TypeAlias = Union[list[Qt.WidgetAttribute], dict[Qt.WidgetAttribute, bool]]
WidgetFlagsType: TypeAlias = Union[list[Qt.WindowType], dict[Qt.WindowType, bool]]


class AbstractWidget(AbstractBase):
    long_pressed: Signal = Signal()

    def __init__(self,
                 long_press_delay: int = 1000,
                 effect: QGraphicsEffect = None,
                 qss: QssType = None,
                 attrs: WidgetAttrsType = None,
                 flags: WidgetFlagsType = None,
                 at_pos: PosEvents = None,
                 animations: list[QAbstractAnimation] = None,
                 **kwargs):

        self._at_pos: PosEvents = at_pos
        self.__long_press_delay: int = long_press_delay

        self.__long_press_timer = QTimer(self)
        self.__long_press_timer.timeout.connect(self.__long_press_timeout)

        self.setMouseTracking(True)
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

        if animations is not None:
            self._set_animations(animations)

    def setGraphicsEffect(self, effect: QGraphicsEffect):
        effect.setParent(self)
        super().setGraphicsEffect(effect)

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
        if ((pos_event._check_var_type(PosEventsRange) and pos_event._pos_in_range(x, y)) 
            or (pos_event._check_var_type(int) and pos_event._equal_pos(x, y))):
            pos_event.func()

    def _on_at_pos(self, at_pos, event):
        for _pos_event in at_pos:
            if isinstance(_pos_event, PosEventsArg):
                if _pos_event.modifiers is not None and not Modifiers.matches(event, _pos_event.modifiers):
                    continue
                if _pos_event.button is not None and not MouseButtons.matches(event, _pos_event.button):
                    continue
                pass

            elif len(_pos_event) == 3:
                _pos_event = PosEventsArg(*_pos_event)

            elif len(_pos_event) == 2:
                _pos_event = PosEventsArg(*map(int, _pos_event[0].toTuple()), _pos_event[-1])

            if _pos_event is not None:
                self._on_pos_events_arg(_pos_event, *event.position().toPoint().toTuple())

    def _set_animations(self, animations):
        for ani in animations:
            if isinstance(ani, QAnimationGroup):
                ani.setParent(self)
                for sub_ani in ani.children():
                    sub_ani.setParent(ani)
                    sub_ani.setTargetObject(self)
                    ani.addAnimation(sub_ani)

            elif isinstance(ani, QVariantAnimation):
                ani.setParent(self)
                ani.setTargetObject(self)

            if ani._running:
                ani.start()

    def mousePressEvent(self, event):
        self.__long_press_timer.start(self.__long_press_delay)
        if self._at_pos is not None and self._at_pos.clicked is not None:
            self._on_at_pos(self._at_pos.clicked, event)
        super().mousePressEvent(event)

    def mouseDoubleClickEvent(self, event):
        if self._at_pos is not None and self._at_pos.double_clicked is not None:
            self._on_at_pos(self._at_pos.double_clicked, event)
        super().mouseDoubleClickEvent(event)

    # def mouseMoveEvent(self, event):
    #     if self._at_pos is not None and self._at_pos.hover is not None:
    #         self._on_at_pos(self._at_pos.hover, event)
    #     return super().mouseMoveEvent(event)

    # def leaveEvent(self, event) -> None:
    #     if self._at_pos is not None and self._at_pos.leave is not None:
    #         self._on_at_pos(self._at_pos.leave, event)
    #     return super().leaveEvent(event)

    def mouseReleaseEvent(self, event):
        self.__long_press_timer.stop()
        super().mouseReleaseEvent(event)


class WidgetDec(AbstractWidget, AbstractDec):
    pass
