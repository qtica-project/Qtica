from typing import Any, Callable, Union
from PySide6.QtCore import Qt, QObject

from ..enums.widgets import Widgets, WidgetTypeVar
from ..enums.signals import Signals, SignalTypeVar
from ..enums.events import Events, EventTypeVar
from .qstyle_sheet import QStyleSheet

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
                else:
                    self.setProperty(name, value)


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
                 **kwargs):
        super().__init__(uid, signals, events, **kwargs)

        self.setUpdatesEnabled(True)
        self.setMouseTracking(True)

        if qss is not None:
            self._set_qss(qss)

        if attrs is not None:
            self._set_attrs(attrs)

        if flags is not None:
            self._set_flags(flags)

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

    # def update_qss(self, 
    #                qss: Union[str, dict],
    #                *,
    #                save: bool = False) -> None:

    #     if (isinstance(qss, dict) 
    #         and isinstance(self.__qss, dict)):
    #         _qss = self.__qss.copy()
    #         _qss.update(qss)
    #         self.__qss = qss if save else self.__qss
    #         return self._set_qss(_qss)
    #     else:
    #         self._set_qss(qss)

    # def _set_qss(self, qss: Union[str, dict]) -> None:
    #     if isinstance(qss, str):
    #         if not os.path.exists(qss):
    #             return self.setStyleSheet(qss)

    #         with open(qss, "r") as fr:
    #             self.setStyleSheet(fr.read())
    #     else:
    #         style_sheet = ""
    #         _obj_style = ""

    #         for k, v in qss.items():
    #             if isinstance(v, dict):
    #                 style_sheet += "%s {\n" % k
    #                 for sk, sv in v.items():
    #                     style_sheet += f"{sk}: {sv};\n"
    #                 style_sheet += "}\n"
    #             else:
    #                 _obj_style += f"{k}: {v};\n"

    #         if (obj_name := self.objectName()):
    #             style_sheet += "#%s {\n" % obj_name
    #             style_sheet += _obj_style
    #             style_sheet += "}"

    #         elif not style_sheet:
    #             style_sheet = _obj_style

    #         self.setStyleSheet(style_sheet)


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
    """
    NoneCheck(icon, self.setIcon)
    NoneCheck(text, self.setText)
    NoneCheck(font, self.setFont)
    ...
    """
    def __new__(cls, *args, **kwargs) -> Any:
        instance = super().__new__(cls)
        _return = instance.__init__(*args, **kwargs)
        return _return

    def __init__(self, value: Any, _callable: Callable) -> Any:
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
        if uid is not None:
            if uid in self._instances_dict:
                raise DuplicateKeyError(uid)

            self._instances_dict[uid] = obj

    def _deregister(self, uid: str) -> Any:
        """ deregister widget from manager """
        if uid is not None:
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
    the __init__ method can know return value
    any class abstract from this class is return the widget
    you can't type this class as widget, if you want to do this
    you need to use one of those classes ObjectDeclarative or WidgetDeclarative
    """

    def __new__(cls, *args, **kwargs) -> Any:
        instance = super().__new__(cls)
        if (uid := kwargs.pop("uid", None)) is not None:
            TrackingDeclarative._register(uid, instance)
        return instance.__init__(*args, **kwargs)

    # def build(self):
    #     raise NotImplementedError

class ObjectDeclarative(ObjectBase, BehaviorDeclarative):
    pass


class WidgetDeclarative(WidgetBase, BehaviorDeclarative):
    pass