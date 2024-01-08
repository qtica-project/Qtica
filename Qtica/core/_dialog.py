#!/usr/bin/python3

from PySide6.QtWidgets import QApplication, QDialog, QWidget
from PySide6.QtCore import QEvent, QObject, QTimer
from PySide6.QtGui import QResizeEvent, QShowEvent
from ._widget import AbstractWidget


class AbstractDialog(AbstractWidget, QDialog):
    def __init__(self,
                 *,
                 timeout: float = None,
                 auto_close: bool = False,
                 **kwargs):
        QDialog.__init__(self, QApplication.activeWindow())
        super().__init__(**kwargs)

        self.window().installEventFilter(self)
        if self._parent is not None:
            self._parent.installEventFilter(self)

        self._timeout = timeout
        self._auto_close = auto_close

    @property
    def _parent(self) -> QWidget:
        return self.parent()

    def showEvent(self, e: QShowEvent) -> None:
        if self._timeout is not None:
            QTimer.singleShot(self._timeout, self.close)
        super().showEvent(e)
        return self.activateWindow()

    def eventFilter(self, arg__1: QObject, arg__2: QEvent) -> bool:
        if arg__1 is self.window():
            if arg__2.type() == QEvent.Type.Resize:
                re = QResizeEvent(arg__2)
                self.resize(re.size())

            if self._auto_close and arg__2.type() == QEvent.Type.WindowDeactivate:
                self.close()

        return super().eventFilter(arg__1, arg__2)