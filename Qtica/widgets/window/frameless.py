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
from .mainwindow import MainWindow


class FramelessWindow(MainWindow):
    def __init__(self, 
                 *,
                 home: Union[QWidget, QLayout] = None,
                 title_bar: QWidget = None,
                 size_grip: WindowSizeGrip = None,
                 **kwargs):

        self.setWindowFlags(
            self.windowFlags()
            | Qt.WindowType.FramelessWindowHint
        )

        self.setAttribute(Qt.WidgetAttribute.WA_AcceptTouchEvents, True)
        self.setAttribute(Qt.WidgetAttribute.WA_Hover, True)

        self.setAutoFillBackground(True)
        self.setUpdatesEnabled(True)
        self.setDocumentMode(True)
        self.setAnimated(True)

        MainWindow.__init__(self, **kwargs)

        self._old_pos = self.pos()

        self._is_system_move = False
        self._size_grip = size_grip
        self._title_bar = title_bar

        if self._title_bar is not None:
            self._set_title_bar(self._title_bar)
        else:
            self.mouseMoveEvent = self._mouseMoveEvent
            self.mousePressEvent = self._mousePressEvent

        if size_grip is not None:
            self._size_grip.setParent(self)

        if home is not None:
            self._set_home(home)

    def _set_home(self, home) -> None:
        if self._title_bar is not None:
            self._frame = QWidget(self)
            self._vlayout = QVBoxLayout(self._frame)

            title_bar = self._title_bar
            if isinstance(self._title_bar, QLayout):
                title_bar = QWidget(self._frame)
                self._title_bar.setProperty("parent", title_bar)
            self._set_titlebar(title_bar)

            if isinstance(home, QLayout):
                home.setProperty("parent", self._frame)
                self._vlayout.addLayout(home)
            else:
                home.setParent(self._frame)
                self._vlayout.addWidget(home)
        else:
            super()._set_home(home)

    def _set_titlebar(self, titlebar: QWidget):
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(titlebar.sizePolicy().hasHeightForWidth())
        titlebar.setSizePolicy(sizePolicy)

        titlebar.mouseMoveEvent = self._mouseMoveEvent
        titlebar.mousePressEvent = self._mousePressEvent

        self._vlayout.addWidget(titlebar)

    def resizeEvent(self, event: QResizeEvent):
        self._size_grip.updateGeometry()
        if self._title_bar is not None:
            self._title_bar.resize(self.width(), self._title_bar.height())
        return QWidget.resizeEvent(self, event)

    def _mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == event.buttons().LeftButton:
            self._old_pos = event.globalPos()
            self._is_system_move = self.windowHandle().startSystemMove()
        return super().mousePressEvent(event)

    def _mouseMoveEvent(self, event: QMouseEvent) -> None:
        if not self._is_system_move:
            delta = QPoint(event.globalPos() - self._old_pos)
            self.move(self.x() + delta.x(),
                      self.y() + delta.y())
            self._old_pos = event.globalPos()
        else:
            return super().mouseMoveEvent(event)
