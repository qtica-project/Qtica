from typing import Union
from PySide6.QtCore import QPoint, QRect, QSize, Qt, Signal
from PySide6.QtGui import QCloseEvent, QMouseEvent, QResizeEvent, QScreen, QShowEvent
from PySide6.QtWidgets import (
    QApplication,
    QDockWidget, 
    QLayout, 
    QSizeGrip,
    QStatusBar,
    QSystemTrayIcon, 
    QVBoxLayout,
    QWidget, 
    QMainWindow,
    QSizePolicy
)

from ...core import WidgetBase
from ...utils.methods import qt_corner_to_edge


class FramelessWindowSizeGrip(QSizeGrip):
    def __init__(self,
                 *,
                 size: Union[tuple[int, int], QSize] = QSize(12, 12),
                 corner: Qt.Corner = Qt.Corner.BottomRightCorner) -> None:
        super().__init__(None)

        self._corner = corner
        self.resize(*size if not isinstance(size, QSize) else size)
        self.get_cursor_for_position()

    def get_cursor_for_position(self):
        self.setCursor({
            Qt.Corner.TopLeftCorner: Qt.CursorShape.SizeFDiagCursor,
            Qt.Corner.TopRightCorner: Qt.CursorShape.SizeBDiagCursor,
            Qt.Corner.BottomLeftCorner: Qt.CursorShape.SizeBDiagCursor,
            Qt.Corner.BottomRightCorner: Qt.CursorShape.SizeFDiagCursor,
        }.get(self._corner, Qt.CursorShape.ArrowCursor))

    def _move(self) -> None:
        if self.parent() is not None:
            rect: QRect = self.parent().rect()

            if self._corner == Qt.Corner.TopRightCorner:
                x, y = rect.topRight().toTuple()
                self.move(x - (self.width() + 5), y - 5)

            elif self._corner == Qt.Corner.TopLeftCorner:
                self.move(
                    rect.x(),
                    0
                )

            elif self._corner == Qt.Corner.BottomRightCorner:
                self.move(rect.right() - self.width() - 1, 
                          rect.bottom() - self.height() - 1)

            elif self._corner == Qt.Corner.BottomLeftCorner:
                self.move(0, rect.bottom() - self.height())

    def mousePressEvent(self, arg__1: QMouseEvent) -> None:
        self.parent().windowHandle().startSystemResize(qt_corner_to_edge(self._corner))
        return super().mousePressEvent(arg__1)

    def updateGeometry(self) -> None:
        self._move()
        return super().updateGeometry()


class FramelessWindow(WidgetBase, QMainWindow):
    startup_changed = Signal()

    def __init__(self, 
                 *,
                 title_bar: QWidget = None,
                 home: Union[QWidget, QLayout] = None,
                 status_bar: QStatusBar = None,
                 dock_widget: QDockWidget = None,
                 size_grip: QSizeGrip = None,
                 sys_tray: QSystemTrayIcon = None,
                 **kwargs):
        QMainWindow.__init__(self)
        super().__init__(**kwargs)

        self.__is_startup = False

        self._old_pos = self.pos()
        self._is_system_move = False
        self._size_grip = size_grip
        self._title_bar = title_bar

        self._set_central_widget()

        if self._title_bar is not None:
            self._set_title_bar(self._title_bar)
        else:
            self.mouseMoveEvent = self._mouseMoveEvent
            self.mousePressEvent = self._mousePressEvent

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

        if sys_tray is not None:
            sys_tray.setParent(self)
            sys_tray.show()

    def closeEvent(self, event: QCloseEvent) -> None:
        super().closeEvent(event)
        self.__is_startup = False

    def showEvent(self, event: QShowEvent) -> None:
        super().showEvent(event)
        if not self.__is_startup:
            self.__is_startup = True
            self.startup_changed.emit()

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

        self._vlayout.addWidget(title_bar)

    def resizeEvent(self, event: QResizeEvent):
        self._size_grip.updateGeometry()
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

    def _set_status_bar(self, status_bar: QStatusBar) -> None:
        self.setStatusBar(status_bar)

    def _set_dock_widget(self, dock_widget: QDockWidget) -> None:
        self.addDockWidget(dock_widget)
