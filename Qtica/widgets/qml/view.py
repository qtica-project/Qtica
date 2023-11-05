from PySide6.QtCore import QUrl
from PySide6.QtQuick import QQuickView

from ...enums.events import EventTypeVar
from ...enums.signals import SignalTypeVar
from ...core.base import ObjectBase


class QuickView(ObjectBase, QQuickView):
    def __init__(self,
                 file: QUrl | str,
                 uid: str = None, 
                 signals: SignalTypeVar = None, 
                 events: EventTypeVar = None, 
                 **kwargs):
        QQuickView.__init__(self, file)
        super().__init__(uid, signals, events, **kwargs)

        self.setResizeMode(QQuickView.ResizeMode.SizeRootObjectToView)