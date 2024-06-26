from typing import Union
from ..core import AbstractWindow
from .size_grip import WindowSizeGrip

from qtpy.QtCore import QPoint, Qt
from qtpy.QtGui import QMouseEvent, QResizeEvent
from qtpy.QtWidgets import (
    QVBoxLayout,
    QSizePolicy,
    QMainWindow,
    QLayout, 
    QWidget
)


class FramelessWindow(AbstractWindow, QMainWindow):
    def __init__(self, 
                 *,
                 child: Union[QWidget, QLayout] = None,
                 title_bar: QWidget = None,
                 size_grip: WindowSizeGrip = None,
                 **kwargs):
        QMainWindow.__init__(self)

        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_AcceptTouchEvents, True)
        self.setAttribute(Qt.WidgetAttribute.WA_Hover, True)

        self.setAutoFillBackground(True)
        self.setDocumentMode(True)

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

        super().__init__(child, **kwargs)

    def _set_child(self, child) -> None:
        if self._title_bar is not None:
            self._vlayout = QVBoxLayout()
            self._vlayout.setContentsMargins(0, 0, 0, 0)

            if isinstance(self._title_bar, QLayout):
                self.titlebar_layout_widget = QWidget()
                self._title_bar.setProperty("parent", self.titlebar_layout_widget)
                self.titlebar_layout_widget.setLayout(self._title_bar)
                self._title_bar = self.titlebar_layout_widget
                self._set_titlebar(self._title_bar)
            elif isinstance(self._title_bar, QWidget):
                self._set_titlebar(self._title_bar)

            if child is not None:
                if isinstance(child, QLayout):
                    self._vlayout.addLayout(child)
                elif isinstance(child, QWidget):
                    self._vlayout.addWidget(child)

            super()._set_child(self._vlayout)

        super()._set_child(child)

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
        if not self._is_pressed:
            return

        if self._is_system_move:
            return super().mouseMoveEvent(event)

        delta = QPoint(event.globalPos() - self._old_pos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self._old_pos = event.globalPos()

    def _mouseReleaseEvent(self, event: QMouseEvent) -> None:
        self._is_pressed = False
        return super().mouseReleaseEvent(event)