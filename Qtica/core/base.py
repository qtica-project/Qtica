from ..enums.widgets import Widgets, WidgetTypeVar
from ..enums.signals import Signals, SignalTypeVar
from ..enums.events import Events, EventTypeVar
from .qstyle_sheet import QStyleSheet
from typing import Any, Callable, Union
from PySide6.QtCore import Qt, QObject
from PySide6.QtWidgets import QGraphicsEffect
import caseconverter


class AbstractBase:
    """
    this class is abstract for any widget.
    """
    def __init__(self, 
                 uid: str = None,
                 signals: SignalTypeVar = None,
                 events: EventTypeVar = None,
                 **kwargs):

        self._set_uid(uid)
        self._set_events(events)
        self._set_signals(signals)
        self._set_property_from_kwargs(**kwargs)

    def _getattr(self, name: str, default: object = None) -> object:
        return getattr(self, name, default)

    def _set_uid(self, uid: str):
        if uid is not None:
            self.setObjectName(uid.strip())

    def _set_events(self, events: EventTypeVar):
        if not events:
            return

        for (event, slot) in events:
            try:
                ename = (caseconverter.camelcase(event.name)
                         if isinstance(event, Events)
                         else event.strip())

                ## self.{event} = newEventMethod
                self.__setattr__(ename, slot)
            except Exception as err:
                print("Error-Event: ", err)

    def _set_signals(self, 
                     signals: SignalTypeVar, 
                     disconnect: bool = False):
        if not signals:
            return

        for (signal, slot) in signals:
            try:
                sname = (caseconverter.camelcase(signal.name)
                         if isinstance(signal, Signals)
                         else signal.strip())

                if (attr := self._getattr(sname)) is not None:
                    if disconnect:
                        attr.disconnect(slot)
                    else:
                        attr.connect(slot)
                else:
                    ## print Warrning slot dose't found.
                    ...
            except Exception as err:
                print("Err-Signal: ", err)

    def _get_wtype(self, w_type: WidgetTypeVar = Widgets.any):
        return (w_type.value
                if isinstance(w_type, Widgets) 
                else w_type)

    def get(self, 
            uid: str, 
            w_type: WidgetTypeVar = Widgets.any) -> QObject:
        return self.findChild(self._get_wtype(w_type), 
                              uid.strip(), 
                              Qt.FindChildOption.FindChildrenRecursively)

    def _set_property_from_kwargs(self, **kwargs):
        for (name, value) in kwargs.items():
            if hasattr(self, name) or self.property(name) is not None:
                snake_case = caseconverter.snakecase(name)
                if snake_case in Signals._member_names_:
                    self._getattr(name).connect(value)
                elif snake_case in Events._member_names_:
                    self.__setattr__(name, value)
                elif self.property(name) is not None:
                    self.setProperty(name, value)
                # elif name.lower().startswith("set"):                  
                elif (func := self._getattr(name)) is not None:
                    if func.__class__.__name__ in (
                        "builtin_function_or_method",
                        "method_descriptor",
                        "function"):
                        try:
                            func(value)
                        except Exception:
                            ...


class ObjectBase(AbstractBase):
    pass

class WidgetBase(AbstractBase):
    def __init__(self, 
                 uid: str = None, 
                 signals: SignalTypeVar = None, 
                 events: EventTypeVar = None,
                 qss: Union[str, dict, QStyleSheet] = None,
                 attrs: Union[list[Qt.WidgetAttribute], 
                              dict[Qt.WidgetAttribute, bool]] = None,
                 flags: Union[list[Qt.WindowType], 
                              dict[Qt.WindowType, bool]] = None,
                 effect: QGraphicsEffect = None,
                 **kwargs):
        super().__init__(uid, signals, events, **kwargs)

        self.setUpdatesEnabled(True)
        self.setMouseTracking(True)

        if effect is not None:
            self._set_effect(effect)

        if qss is not None:
            self._set_qss(qss)

        if attrs is not None:
            self._set_attrs(attrs)

        if flags is not None:
            self._set_flags(flags)

    def _set_effect(self, effect: QGraphicsEffect):
        effect.setProperty("parent", self)
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


class Return:
    def __init__(self, 
                 root: Any, 
                 child: Any):

        self._root = root
        self._child = child

    @property
    def root(self):
        return self._root

    @property
    def child(self):
        return self._child


class NoneCheck:
    '''
    e.g
    NoneCheck(icon, self.setIcon)
    
    # the same!
    if icon is not None:
        self.setIcon()
    '''

    def __new__(cls, *args, **kwargs) -> Any:
        instance = super().__new__(cls)
        return instance.__init__(*args, **kwargs)

    def __init__(self, 
                 _callable: Callable,
                 value: Any) -> Any:

        if value is not None:
            return _callable(value)



## Declarative

class DuplicateKeyError(Exception):
    def __init__(self, uid: str):
        super().__init__(uid)
        print(f"'{uid}' was registered in this dictionary!")


class _TrackingDeclarative:
    def __init__(self):
        self._instances_dict = dict()

    def _register(self, uid: str, obj: Any) -> None:
        if not isinstance(uid, str):
            raise ValueError("invalid uid, must be str type.")

        if uid in self._instances_dict:
            raise DuplicateKeyError(uid)
        self._instances_dict[uid] = obj

    def _deregister(self, uid: str) -> Any:
        """ deregister widget from manager """
        if not isinstance(uid, str):
            raise ValueError("invalid uid, must be str type.")

        if uid not in self._instances_dict:
            return

        return self._instances_dict.pop(uid)

    def pop(self, uid: str) -> Any:
       self._deregister(uid)

    def get(self, uid: str) -> Any:
        return self._instances_dict.get(uid)

    def items(self) -> Any:
        return self._instances_dict.items()

TrackingDeclarative = _TrackingDeclarative()


class BehaviorDeclarative:
    """
    `__init__` method can now return a value

    ### usage example
    ```python
    class Object(BehaviorDeclarative):
        def __init__(self, *args, **kwargs):
            return ...
    ```
    
    #### NOTE: use `uid` parameter to store this class in `TrackingDeclarative`, \
        and call it with Api.fetch
    """

    def __new__(cls, *args, **kwargs) -> Any:
        instance = super().__new__(cls)
        _uid = (kwargs.pop
                if 'uid' not in
                instance.__init__.__code__.co_varnames
                else kwargs.get)("uid", None)

        if _uid is not None:
            TrackingDeclarative._register(_uid, instance)

        return instance.__init__(*args, **kwargs)


class ObjectDeclarative(ObjectBase, BehaviorDeclarative):
    pass


class WidgetDeclarative(WidgetBase, BehaviorDeclarative):
    pass
