#!/usr/bin/python3

from typing import Any, Union, Sequence
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGraphicsEffect
from .base import BehaviorDeclarative, AbstractBase
from .qstyle_sheet import QStyleSheet
from ..enums.signals import SignalTypeVar
from ..enums.events import EventTypeVar


class WidgetBase(AbstractBase):
    def __init__(self,
                 *,
                 uid: str = None, 
                 signals: SignalTypeVar = None, 
                 events: EventTypeVar = None,
                 methods: Sequence[tuple[str, Any]] = None,
                 qss: Union[str, dict, QStyleSheet] = None,
                 attrs: Union[list[Qt.WidgetAttribute], 
                              dict[Qt.WidgetAttribute, bool]] = None,
                 flags: Union[list[Qt.WindowType], 
                              dict[Qt.WindowType, bool]] = None,
                 effect: QGraphicsEffect = None,
                 **kwargs):
        super().__init__(
            uid=uid, 
            signals=signals, 
            events=events, 
            methods=methods, 
            **kwargs)

        self.setUpdatesEnabled(True)
        self.setMouseTracking(True)

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


class WidgetDeclarative(WidgetBase, BehaviorDeclarative):
    pass
