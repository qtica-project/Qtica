from typing import Union
from PySide6.QtCore import QPoint, Qt
from PySide6.QtGui import QMouseEvent, QResizeEvent
from PySide6.QtWidgets import (
    QLayout, 
    QVBoxLayout,
    QWidget, 
    QSizePolicy
)
from ..size_grip import WindowSizeGrip
from ...core import AbstractWidget
from .base import BaseWindow


class FramelessWindow(AbstractWidget, BaseWindow):
    def __init__(self, *,
                 home: Union[QWidget, QLayout] = None,
                 title_bar: QWidget = None,
                 size_grip: WindowSizeGrip = None,
                 **kwargs):
        BaseWindow.__init__(self, **kwargs)

        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_AcceptTouchEvents, True)
        self.setAttribute(Qt.WidgetAttribute.WA_Hover, True)

        self.setAutoFillBackground(True)
        self.setDocumentMode(True)

        super().__init__(**kwargs)

        self._old_pos = self.pos()

        self._is_system_move = False
        self._is_pressed = False
        self._size_grip = size_grip
        self._title_bar = title_bar

        if not title_bar:
            self.mouseMoveEvent = self._mouseMoveEvent
            self.mousePressEvent = self._mousePressEvent
            self.mouseReleaseEvent = self._mouseReleaseEvent

        if size_grip is not None:
            self._size_grip.setParent(self)

        self._set_home(home)

    def _set_home(self, home) -> None:
        if self._title_bar is not None:
            self._vlayout = QVBoxLayout()
            self._vlayout.setContentsMargins(0, 0, 0, 0)

            if isinstance(self._title_bar, QLayout):
                _widget = QWidget()
                self._title_bar.setProperty("parent", _widget)
                _widget.setLayout(self._title_bar)
                self._title_bar = _widget

            self._set_titlebar(self._title_bar)

            if home is not None:
                _func = self._vlayout.addWidget
                if isinstance(home, QLayout):
                    _func = self._vlayout.addLayout
                _func(home)

            return super()._set_home(self._vlayout)

        return super()._set_home(home)

    def _set_titlebar(self, titlebar: QWidget):
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(titlebar.sizePolicy().hasHeightForWidth())
        titlebar.setSizePolicy(sizePolicy)

        titlebar.mouseMoveEvent = self._mouseMoveEvent
        titlebar.mousePressEvent = self._mousePressEvent
        titlebar.mouseReleaseEvent = self._mouseReleaseEvent

        self._vlayout.addWidget(titlebar)

    def resizeEvent(self, event: QResizeEvent):
        if self._size_grip is not None:
            self._size_grip.updateGeometry()

        if self._title_bar is not None:
            self._title_bar.resize(self.width(), self._title_bar.height())

        return QWidget.resizeEvent(self, event)

    def _mousePressEvent(self, event: QMouseEvent) -> None:
        self._is_pressed = True
        if event.button() == event.buttons().LeftButton:
            self._old_pos = event.globalPos()
            self._is_system_move = self.windowHandle().startSystemMove()
        return super().mousePressEvent(event)

    def _mouseMoveEvent(self, event: QMouseEvent) -> None:
        if self._is_pressed:

            if self._is_system_move:
                return super().mouseMoveEvent(event)

            delta = QPoint(event.globalPos() - self._old_pos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self._old_pos = event.globalPos()

    def _mouseReleaseEvent(self, event: QMouseEvent) -> None:
        self._is_pressed = False
        return super().mouseReleaseEvent(event)