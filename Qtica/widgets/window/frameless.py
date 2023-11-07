from typing import Union
from PySide6.QtCore import QPoint, QSize, Qt, Signal
from PySide6.QtGui import QCloseEvent, QMouseEvent, QResizeEvent, QScreen, QShowEvent
from PySide6.QtWidgets import (
    QApplication,
    QDockWidget, 
    QLayout, 
    QSizeGrip,
    QStatusBar, 
    QVBoxLayout,
    QWidget, 
    QMainWindow,
    QSizePolicy
)

from ...enums.events import EventTypeVar
from ...enums.signals import SignalTypeVar
from ...core.base import WidgetBase


class FramelessWindowSizeGrip(QSizeGrip):
    def __init__(self,
                 size: Union[tuple[int, int], QSize] = QSize(12, 12)) -> None:
        super().__init__(None)

        self.resize(*size if not isinstance(size, QSize) else size)
        self.setCursor(Qt.CursorShape.SizeHorCursor)


class FramelessWindow(WidgetBase, QMainWindow):
    startup_changed = Signal()

    def __init__(self, 
                 uid: str = None, 
                 signals: SignalTypeVar = None, 
                 events: EventTypeVar = None, 
                 qss: str | dict = None,
                 title_bar: QWidget = None,
                 home: Union[QWidget, QLayout] = None,
                 status_bar: QStatusBar = None,
                 dock_widget: QDockWidget = None,
                 size_grip: QSizeGrip = None,
                 **kwargs):
        QMainWindow.__init__(self)
        super().__init__(uid, signals, events, qss, **kwargs)

        self.__is_startup = False

        self._old_pos = self.pos()
        self._is_pressed = False
        self._size_grip = size_grip
        self._title_bar = title_bar

        self._set_central_widget()

        if self._title_bar is not None:
            self._set_title_bar(self._title_bar)
        else:
            self.mouseMoveEvent = self._mouseMoveEvent
            self.mousePressEvent = self._mousePressEvent
            self.mouseReleaseEvent = self._mouseReleaseEvent

        if size_grip is not None:
            self._size_grip.setParent(self)

        if home is not None:
            self._set_home(home)

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

        if status_bar is not None:
            self._set_status_bar(status_bar)

        if dock_widget is not None:
            self._set_dock_widget(dock_widget)

    def closeEvent(self, event: QCloseEvent) -> None:
        self.__is_startup = False
        return super().closeEvent(event)

    def showEvent(self, event: QShowEvent) -> None:
        if not self.__is_startup:
            self.__is_startup = True
            self.startup_changed.emit()

        return super().showEvent(event)

    def _set_central_widget(self):
        self.__centralwidget = QWidget(self)
        self._vlayout = QVBoxLayout(self.__centralwidget)

        self.__centralwidget.setObjectName("__centralwidget")
        self.setCentralWidget(self.__centralwidget)

    def _set_home(self, home: QWidget):
        if isinstance(home, QLayout):
            home.setProperty("parent", 
                             self.__centralwidget)
            self._vlayout.addLayout(home)

        elif isinstance(home, QWidget):
            home.setParent(self)
            self._vlayout.addWidget(home)

        else:
            raise ValueError("the 'home' argument must be one of \
                the QWidget or QLayout instance.")

    def _set_title_bar(self, title_bar: QWidget):
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, 
                                 QSizePolicy.Policy.Fixed)

        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(title_bar.sizePolicy().hasHeightForWidth())
        title_bar.setSizePolicy(sizePolicy)

        title_bar.mouseMoveEvent = self._mouseMoveEvent
        title_bar.mousePressEvent = self._mousePressEvent
        title_bar.mouseReleaseEvent = self._mouseReleaseEvent

        self._vlayout.addWidget(title_bar)

    def resizeEvent(self, event: QResizeEvent):
        if self._size_grip is not None:
            # top right
            # x, y = self.rect().topRight().toTuple()
            # self._size_grip.move(x - (self._size_grip.width() - 5), y - 1)

            # bottom right
            rect = self.rect()
            self._size_grip.move(rect.right() - self._size_grip.width() - 1, 
                                 rect.bottom() - self._size_grip.height() - 1)

        if self._title_bar is not None:
            self._title_bar.resize(self.width(), 
                                   self._title_bar.height())

        return QWidget.resizeEvent(self, event)

    def center_window(self, screen: QScreen = None):
        dst = screen if screen is not None else QApplication.primaryScreen()
        geo = self.frameGeometry()
        geo.moveCenter(QScreen.availableGeometry(dst).center())
        self.move(geo.center())

    def _mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == event.buttons().LeftButton:
            self._is_pressed = True
            self._old_pos = event.globalPos()
            self.windowHandle().startSystemMove()

        return super().mousePressEvent(event)

    def _mouseReleaseEvent(self, event: QMouseEvent) -> None:
        self._is_pressed = False
        return super().mouseReleaseEvent(event)

    def _mouseMoveEvent(self, event: QMouseEvent) -> None:
        if self._is_pressed:
            delta = QPoint(event.globalPos() - self._old_pos)
            self.move(self.x() + delta.x(),
                      self.y() + delta.y())
            self._old_pos = event.globalPos()

        return super().mouseMoveEvent(event)

    def _set_status_bar(self, status_bar: QStatusBar) -> None:
        self.setStatusBar(status_bar)

    def _set_dock_widget(self, dock_widget: QDockWidget) -> None:
        self.addDockWidget(dock_widget)
