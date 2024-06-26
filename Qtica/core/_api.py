from typing import Any, Union
from PySide6.QtCore import Qt, QObject
from PySide6.QtWidgets import QApplication, QWidget
from ._declarative import AbstractDec, TrackingDec
from ._base import WidgetsType
from .. import enums


class Api:
    '''

    ```
    api = Api(parent)
    obj = api.get('uid')
    >> QObject
    ```

    ### Direct Access
    ```
    Api.fetch('uid')
    >> QObject
    ```
    '''
    def __init__(self, 
                 parent: QObject = None,
                 qtype: WidgetsType | object = enums.Widgets.any):

        self.parent = parent
        self.qtype = qtype

    def _find_child(self, 
                    target: QObject,
                    uid: str,
                    qtype: WidgetsType | object) -> QObject | None:

        return target.findChild(self._get_wtype(qtype 
                                                if qtype is not None
                                                else self.qtype),
                                uid.strip(), 
                                Qt.FindChildOption.FindChildrenRecursively)

    def _get_wtype(self, qtype: WidgetsType | object = enums.Widgets.any):
        return (qtype.value 
                if isinstance(qtype, enums.Widgets)
                else qtype)

    def get(self,
            uid: str, 
            qtype: WidgetsType | object = enums.Widgets.any) -> QObject | None:

        uid = uid.strip()

        if Api.isinstance(qtype, AbstractDec):
            return TrackingDec.get(uid)

        if self.parent is not None:
            return self._find_child(self.parent, uid, qtype)

        for parent in QApplication.topLevelWidgets():
            widget = self._find_child(parent, uid, qtype)
            if widget is not None:
                return widget

    @staticmethod
    def isinstance(obj, _class) -> bool:
        if obj == _class:
            return True

        if type(obj) == _class:
            return True

        if isinstance(obj, _class):
            return True

        return False

    @classmethod
    def fetch(cls,
              uid: str,
              qtype: WidgetsType | object = enums.Widgets.any
        ) -> Union[QWidget, QObject, object, None]:

        uid = uid.strip()

        if uid == QApplication.instance().objectName().strip():
            return QApplication.instance()

        if cls.isinstance(qtype, AbstractDec):
            return TrackingDec.get(uid)

        if uid in TrackingDec._instances_dict:
            return TrackingDec.get(uid)

        qobjs_copy = set(QApplication.allWidgets().copy())
        qobjs_copy.update(QApplication.allWindows())
        qobjs_copy.update(QApplication.topLevelWidgets())
        qobjs_copy.update(QApplication.topLevelWindows())
        qobjs_copy.update(QApplication.screens())
        for parent in qobjs_copy:
            if uid == parent.objectName().strip():
                return parent
            if (widget := cls._find_child(cls, parent, uid, qtype)) is not None:
                return widget
        del qobjs_copy

        return cls._find_child(cls, QApplication.instance(), uid, qtype)

    @staticmethod
    def dec_fetch(uid: str) -> Any:
        return TrackingDec.get(uid)

    @staticmethod
    def declarative_fetch(uid: str) -> Any:
        return Api.dec_fetch(uid)

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self.get(*args, **kwds)