#!/usr/bin/python3

from typing import Any, Union
from PySide6.QtCore import QUrl, Qt
from PySide6.QtQuickWidgets import QQuickWidget
from ..core import AbstractWidget


class QuickWidget(AbstractWidget, QQuickWidget):
    def __init__(self, 
                 qml: Union[QUrl, str],
                 *,
                 context: list[tuple[str, Any]] = None,
                 **kwargs):
        QQuickWidget.__init__(self, qml)

        self._context = context

        self.setUpdatesEnabled(True)
        self.setTabletTracking(True)
        self.setMouseTracking(True)

        self.setResizeMode(QQuickWidget.ResizeMode.SizeRootObjectToView)
        self.setAttribute(Qt.WidgetAttribute.WA_X11NetWmWindowTypeDesktop, True)

        super().__init__(**kwargs)

        self.statusChanged.connect(self.__on_statusChanged)

    @property
    def root_object(self):
        return self.rootObject()

    @property
    def root_context(self):
        return self.rootContext()

    def __on_statusChanged(self, status):
        if self._context is not None:
            for name, value in self._context:
                self.rootContext().setContextProperty(name, value)