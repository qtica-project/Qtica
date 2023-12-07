from PySide6.QtQuick import QQuickView
from PySide6.QtCore import QUrl
from ...core import QObjectBase


class QuickView(QObjectBase, QQuickView):
    def __init__(self,
                 *,
                 qml: QUrl | str,
                 **kwargs):
        QQuickView.__init__(self, qml)
        super().__init__(**kwargs)

        self.setResizeMode(QQuickView.ResizeMode.SizeRootObjectToView)