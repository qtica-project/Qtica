#!/usr/bin/python3

from PySide6.QtWidgets import QApplication, QDialog, QWidget
from PySide6.QtCore import QEvent, QObject, QTimer
from PySide6.QtGui import QShowEvent
from ._widget import AbstractWidget


class AbstractDialog(AbstractWidget, QDialog):
    def __init__(self,
                 timeout: float = None,
                 auto_close: bool = False,
                 **kwargs):

        _parent = QApplication.activeWindow()
        if not auto_close:
            _parent.hideEvent = lambda _: self.hide()
            _parent.showEvent = lambda _: self.show()

        QDialog.__init__(self, _parent)
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
        if self.isHidden() or not self.isActiveWindow():
            if self._timeout is not None:
                QTimer.singleShot(self._timeout, self.close)

            super().showEvent(e)
            self.activateWindow()

    def eventFilter(self, arg__1: QObject, arg__2: QEvent) -> bool:
        if arg__1 is self.window():
            if (self._auto_close
                and arg__2.type() in (QEvent.Type.WindowDeactivate, QEvent.Type.Hide)):
                self.close()

        return super().eventFilter(arg__1, arg__2)