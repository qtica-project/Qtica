#!/usr/bin/python3

from typing import Any, Callable, Sequence, Union
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt, QObject
from ..enums.events import Events, EventTypeVar
from ..enums.widgets import Widgets, WidgetTypeVar
from ..enums.signals import Signals, SignalTypeVar
from ..utils.caseconverter import camelcase, snakecase


class Func:
    def __init__(self, func, *args, **kwargs):
        self._func = func
        self._args = args
        self._kwargs = kwargs

    def func(self) -> Union[Callable, str]:
        return self._func

    def args(self) -> tuple[Any]:
        return self._args

    def kwargs(self) -> dict[str, Any]:
        return self._kwargs


class Args:
    def __init__(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs

    def args(self) -> list[Any]:
        return self._args

    def kwargs(self) -> dict[str, Any]:
        return self._kwargs


class MArgs:
    def __init__(self, *args: Union[Args, Any]):
        self._args = args

    def args(self) -> list[Union[Args, Any]]:
        return self._args



class AbstractBase:
    def __init__(self,
                 uid: str = None,
                 signals: SignalTypeVar = None,
                 events: EventTypeVar = None,
                 methods: Sequence[Union[tuple[str, Any], Func]] = None,
                 enable_event_stack: bool = True,
                 **kwargs):

        self._enable_event_stack = enable_event_stack

        self._set_uid(uid)
        self._set_events(events)
        self._set_signals(signals)
        self._set_methods(methods)
        self._set_property_from_kwargs(**kwargs)

    def setEventStackEnable(self, state: bool):
        self._enable_event_stack = state

    def _getattr(self, name: str, default: object = None) -> object:
        return getattr(self, name, default)

    def _set_uid(self, uid: str):
        if uid is not None:
            self.setObjectName(uid.strip())

    def _set_methods(self, methods):
        if not methods:
            return

        for method in methods:
            if isinstance(method, Func):
                if (func := getattr(self, method.func())) is not None and callable(func):
                    func(*method.args(), **method.kwargs())
            elif (func := getattr(self, method[0])) is not None and callable(func):
                func(method[1])

    def _set_events(self, events: EventTypeVar):
        if not events:
            return

        for event, slot in events:
            if isinstance(event, Events):
                _ename = camelcase(event.name) + "Event"
            else:
                _ename = event.strip()

            _ecomp = _ename + "Event"
            if hasattr(self, _ecomp):
                _ename = _ecomp

            self.__setattr__(_ename, slot)

    def _set_signals(self, signals: SignalTypeVar, disconnect: bool = False):
        if not signals:
            return

        for signal, slot in signals:
            if isinstance(signal, Signals):
                _sname = camelcase(signal.name)
            else:
                _sname = signal.strip()

            if (attr := self._getattr(_sname)) is not None:
                if disconnect:
                    attr.disconnect(slot)
                else:
                    attr.connect(slot)

    def _get_wtype(self, qtype: Union[WidgetTypeVar, QObject] = Widgets.any):
        return (qtype.value
                if isinstance(qtype, Widgets)
                else qtype)

    def fetch(self, 
            uid: str, 
            qtype: Union[WidgetTypeVar, QObject] = Widgets.any) -> QObject:

        return self.findChild(
            self._get_wtype(qtype), 
            uid.strip(), 
            Qt.FindChildOption.FindChildrenRecursively)

    def _set_property_from_kwargs(self, **kwargs):
        for name, value in kwargs.items():
            if hasattr(self, name) or self.property(name) is not None:
                snake_case = snakecase(name)

                # handle signals
                if snake_case in Signals._member_names_:
                    self._getattr(name).connect(value)

                # handle events
                elif snake_case in Events._member_names_:
                    self.__setattr__(name, value)

                # handle parent parametar
                elif name == "parent":
                    self._handle_parent_kwarg(name, value)

                # handle properties
                elif self.property(name) is not None:
                    self.setProperty(name, value)

                # handle set callable methods
                elif name.startswith("set"):
                    self._handle_set_methods(name, value)

                # handle add callable methods
                elif name.startswith("add"):
                    self._handle_add_methods(name, value)

    def _handle_parent_kwarg(self, name: str, value: Any) -> None:
        if isinstance(value, str):
            for parent in QApplication.topLevelWidgets():
                if parent.objectName().strip() == value.strip():
                    self.setParent(parent)

                elif (widget := parent.findChild(QObject, 
                                                    value.strip(), 
                                                    Qt.FindChildOption.FindChildrenRecursively)) is not None:
                    self.setParent(widget)

        elif callable(value):
            self.setParent(value())

        else:
            self.setParent(value)

    def _handle_set_methods(self, name: str, value: Any) -> None:
        if (func := self._getattr(name)) is not None and callable(func):
            if isinstance(value, Args):
                func(*value.args(), **value.kwargs())
            else:
                func(value)

    def _handle_add_methods(self, name: str, value: Any) -> None:
        if (func := self._getattr(name)) is not None and callable(func):
            if isinstance(value, MArgs):
                for v in value.args():
                    if isinstance(v, Args):
                        func(*v.args(), **v.kwargs())
                    else:
                        func(value)
            elif isinstance(value, Args):
                func(*value.args(), **value.kwargs())
            else:
                func(value)

    def __setattr__(self, __name: str, __value: Any) -> None:
        if hasattr(self, "_enable_event_stack") and self._enable_event_stack:
            # Events Stack
            if __name.endswith("Event"):
                __func = self.__getattribute__(__name)
                def __event(e):
                    __func(e)  # load prev events
                    __value(e) # load new event
                    return getattr(self.__class__, __name)

                return super().__setattr__(__name, __event)

        return super().__setattr__(__name, __value)