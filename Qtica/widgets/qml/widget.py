from PySide6.QtQuickWidgets import QQuickWidget
from PySide6.QtCore import QUrl, Qt
from typing import Tuple, Any

from ...enums.events import EventTypeVar
from ...enums.signals import SignalTypeVar
from ...core.base import WidgetBase


class QuickWidget(WidgetBase, QQuickWidget):
    def __init__(self, 
                 file: QUrl | str,
                 context: list[Tuple[str, Any]] = None,
                 uid: str = None, 
                 signals: SignalTypeVar = None, 
                 events: EventTypeVar = None, 
                 **kwargs):
        QQuickWidget.__init__(self, file)
        super().__init__(uid, signals, events, **kwargs)

        self._context = context

        self.setUpdatesEnabled(True)
        self.setTabletTracking(True)
        self.setMouseTracking(True)

        self.setResizeMode(QQuickWidget.ResizeMode.SizeRootObjectToView)
        self.setAttribute(Qt.WidgetAttribute.WA_X11NetWmWindowTypeDesktop, True)
        self.statusChanged.connect(self.__on_statusChanged)

    @property
    def root_object(self):
        return self.rootObject()

    @property
    def root_context(self):
        return self.rootContext()

    def __on_statusChanged(self, status):
        if self._context is not None:
            for (name, value) in self._context:
                self.rootContext().setContextProperty(name, value)

        if status == self.Status.Error:
            for error in self.errors():
                print("qml-widget-error: ", error.toString())