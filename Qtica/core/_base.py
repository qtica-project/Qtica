from typing import Any, Callable, TypeAlias, Union
from PySide6.QtCore import Qt, QObject
from PySide6.QtWidgets import QApplication
from ..utils.caseconverter import camelcase, snakecase
from .objects import Args, MArgs, Func
from .. import enums


EventsType: TypeAlias = Union[list[tuple[Union[enums.Events, str], Callable[..., Any]]], 
                            dict[Union[enums.Events, str], Callable[..., Any]]]
SignalsType: TypeAlias = Union[list[tuple[Union[enums.Signals, str], Callable[..., Any]]], 
                            dict[Union[enums.Signals, str], Callable[..., Any]]]
MethodsType: TypeAlias = Union[list[Union[tuple[str, Union[Any, Args]], Func]], dict[str, Union[Any, Args]]]

WidgetsType: TypeAlias = Union[QObject, enums.Widgets]


class AbstractBase:
    def __init__(self,
                 uid: str = None,
                 signals: SignalsType = None,
                 events:  EventsType = None,
                 methods: MethodsType = None,
                 enable_event_stack: bool = True,
                 **kwargs):

        self._enable_event_stack = enable_event_stack

        self._set_uid(uid)
        self._set_property_from_kwargs(**kwargs)
        self._set_signals(signals)
        self._set_events(events)
        self._set_methods(methods)

    def setEventStackEnable(self, on: bool):
        self._enable_event_stack = on

    def _getattr(self, name: str, default: object = None) -> object:
        return getattr(self, name, default)

    def _set_uid(self, uid: str):
        if uid is not None:
            self.setObjectName(uid.strip())

    def _set_methods(self, methods: MethodsType):
        if not methods:
            return

        if isinstance(methods, dict):
            for name, value in methods.items():
                if (func := getattr(self, name)) is not None and callable(func):
                    if isinstance(value, Args):
                        func(*value.args(), **value.kwargs())
                    else:
                        func(value)
        else:
            for method in methods:
                if isinstance(method, Func):
                    if (func := getattr(self, method.func())) is not None and callable(func):
                        func(*method.args(), **method.kwargs())
                elif (func := getattr(self, method[0])) is not None and callable(func):
                    arg = method[1]
                    if isinstance(arg, Args):
                        func(*arg.args(), **arg.kwargs())
                    else:
                        func(arg)

    def _set_events(self, events: EventsType):
        if not events:
            return

        for event, slot in (events.items() if isinstance(events, dict) else events):
            if isinstance(event, enums.Events):
                _ename = camelcase(event.name) + "Event"
            else:
                _ename = event.strip()

            _ecomp = _ename + "Event"
            if hasattr(self, _ecomp):
                _ename = _ecomp

            self.__setattr__(_ename, slot)

    def _set_signals(self, signals: SignalsType, disconnect: bool = False):
        if not signals:
            return

        for signal, slot in (signals.items() if isinstance(signals, dict) else signals):
            if isinstance(signal, enums.Signals):
                _sname = camelcase(signal.name)
            else:
                _sname = signal.strip()

            if (attr := self._getattr(_sname)) is not None:
                if disconnect:
                    attr.disconnect(slot)
                else:
                    attr.connect(slot)

    def _get_wtype(self, qtype: WidgetsType = enums.Widgets.any):
        return qtype.value if isinstance(qtype, enums.Widgets) else qtype

    def fetch(self, uid: str, qtype: WidgetsType = enums.Widgets.any) -> QObject:
        return self.findChild(
            self._get_wtype(qtype), 
            uid.strip(), 
            Qt.FindChildOption.FindChildrenRecursively)

    def _set_property_from_kwargs(self, **kwargs):
        for name, value in kwargs.items():
            if hasattr(self, name) or self.property(name) is not None:
                snake_case = snakecase(name)

                # handle signals
                if snake_case in enums.Signals._member_names_:
                    self._getattr(name).connect(value)

                # handle events
                elif snake_case in enums.Events._member_names_:
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
                elif (widget := parent.findChild(QObject, value.strip(), Qt.FindChildOption.FindChildrenRecursively)) is not None:
                    self.setParent(widget)
        elif callable(value):
            self.setParent(value())
        else:
            self.setParent(value)

    def _handle_set_methods(self, name: str, value: Any) -> None:
        if (func := self._getattr(name)) is not None and callable(func):
            if isinstance(value, MArgs):
                for v in value.args():
                    func(*v.args(), **v.kwargs())
            elif isinstance(value, Args):
                func(*value.args(), **value.kwargs())
            else:
                func(value)

    def _handle_add_methods(self, name: str, value: Any) -> None:
        if (func := self._getattr(name)) is not None and callable(func):
            if isinstance(value, (MArgs, set, list, tuple)):
                for v in (value.args() if isinstance(value, MArgs) else value):
                    if isinstance(v, Args):
                        func(*v.args(), **v.kwargs())
                    else:
                        func(v)
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