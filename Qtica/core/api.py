from typing import Any, Union
from PySide6.QtCore import Qt, QObject
from PySide6.QtWidgets import QApplication, QWidget
from ..enums.widgets import Widgets, WidgetTypeVar
from .base import (
    BehaviorDeclarative,
    TrackingDeclarative
)


class Api:
    '''

    ```
    api = Api(parent)
    obj = api.get('uid')
    >> obj = object
    ```

    ### Direct Access
    ```
    Api.fetch('uid')
    >> object
    ```
    '''
    def __init__(self, 
                 parent: QObject = None,
                 w_type: WidgetTypeVar | object = Widgets.any):

        self.parent = parent
        self.w_type = w_type

    @classmethod
    def _find_child(cls, 
                    target: QObject,
                    uid: str,
                    w_type: WidgetTypeVar) -> QObject | None:

        return target.findChild(cls._get_wtype(w_type 
                                                if w_type is not None
                                                else cls.w_type),
                                uid.strip(), 
                                Qt.FindChildOption.FindChildrenRecursively)

    def _get_wtype(self, w_type: WidgetTypeVar = Widgets.any):
        return (w_type.value 
                if isinstance(w_type, Widgets) 
                else w_type)

    def get(self, 
            uid: str, 
            _type: WidgetTypeVar | object = Widgets.any) -> QObject | None:

        if Api.isinstance(_type, BehaviorDeclarative):
            return TrackingDeclarative.get(uid)

        if self.parent is not None:
            return self._find_child(self.parent, uid, _type)

        for parent in QApplication.topLevelWidgets():
            widget = self._find_child(parent, uid, _type)
            if widget is not None:
                return widget

    @staticmethod
    def isinstance(obj, _type) -> bool:
        if obj == _type:
            return True

        if type(obj) == _type:
            return True

        if isinstance(obj, _type):
            return True

        return False

    @classmethod
    def fetch(cls,
              uid: str,
              _type: WidgetTypeVar | object = Widgets.any
        ) -> Union[QWidget, QObject, Any, None]:

        if cls.isinstance(_type, BehaviorDeclarative):
            return TrackingDeclarative.get(uid)

        if uid in TrackingDeclarative._instances_dict:
            return TrackingDeclarative.get(uid)

        for parent in QApplication.topLevelWidgets():
            if parent.objectName().strip() == uid.strip():
                return parent

            if (widget := Api._find_child(parent, uid, _type)) is not None:
                return widget

    @staticmethod
    def declarative_fetch(uid: str) -> Any:
        return TrackingDeclarative.get(uid)

    @staticmethod
    def dec_fetch(uid: str) -> Any:
        return Api.declarative_fetch(uid)

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self.get(*args, **kwds)