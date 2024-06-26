import os.path

from typing import Any, Union
from ..core import AbstractWidget
from ..tools.qt_file_open import TempFile

from qtpy.QtCore import QUrl
from qtpy.QtQuickWidgets import QQuickWidget


class QuickWidget(AbstractWidget, QQuickWidget):
    def __init__(self, 
                 qml: Union[QUrl, str],
                 *,
                 context: Union[list[tuple[str, Any]], dict[str, Any]] = None,
                 **kwargs):

        if not os.path.exists(qml):
            with TempFile(mode=TempFile.OpenModeFlag.ReadWrite) as tf:
                tf.write(bytes(qml, encoding="utf-8"))
                tf.readAll()
                QQuickWidget.__init__(self, tf.fileName())
            del tf
        else:
            QQuickWidget.__init__(self, qml)

        self._context = context

        self.setTabletTracking(True)
        self.setMouseTracking(True)
        self.setResizeMode(QQuickWidget.ResizeMode.SizeRootObjectToView)

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
            for name, value in (self._context.items() 
                                if isinstance(self._context, dict) 
                                else self._context):
                self.rootContext().setContextProperty(name, value)