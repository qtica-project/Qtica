from PySide6.QtCore import QPoint, Qt
from PySide6.QtGui import QMouseEvent, QResizeEvent, QScreen
from PySide6.QtWidgets import (
    QApplication, 
    QLayout, 
    QSizeGrip, 
    QVBoxLayout, 
    QWidget, 
    QSizePolicy
)

from ...enums.events import EventTypeVar
from ...enums.signals import SignalTypeVar
from ...core.base import WidgetBase

'''
TODO:
 - [] let user to choose grip edge
 - [] let user to set CustomGrip widget
'''

class FramelessWindow(WidgetBase, QWidget):
    def __init__(self, 
                 uid: str = None, 
                 signals: SignalTypeVar = None, 
                 events: EventTypeVar = None, 
                 qss: str | dict = None,
                 resizable: bool = True,
                 grip_size: int = 12,
                 title_bar: QWidget = None,
                 home: QWidget = None,
                 **kwargs):
        QWidget.__init__(self)
        super().__init__(uid, signals, events, qss, **kwargs)

        self._vlayout = QVBoxLayout(self)

        self._old_pos = self.pos()
        self._is_pressed = False
        self._grip_size = grip_size
        self._resizable = resizable
        self._title_bar = title_bar

        if self._title_bar is not None:
            self._set_title_bar(self._title_bar)
        else:
            self.mouseMoveEvent = self._mouseMoveEvent
            self.mousePressEvent = self._mousePressEvent
            self.mouseReleaseEvent = self._mouseReleaseEvent

        if self._resizable:
            self._grip = QSizeGrip(self)
            self._grip.setCursor(Qt.CursorShape.SizeHorCursor)
            self._grip.resize(self._grip_size, self._grip_size)

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

    def _set_home(self, home: QWidget):
        if isinstance(home, QLayout):
            widget = QWidget(self)
            widget.setLayout(home)
            self._vlayout.addWidget(widget)
        else:
            self._vlayout.addWidget(home)

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

    def setResizeEnabled(self, enabled: bool):
        """ set whether resizing is enabled """
        self._resizable = enabled

    def resizeEvent(self, event: QResizeEvent):

        if self._resizable:
            # self.windowHandle().startSystemResize()

            # top right
            # x, y = self.rect().topRight().toTuple()
            # self._grip.move(x - (self._grip_size - 5), y - 1)

            # bottom right
            rect = self.rect()
            self._grip.move(rect.right() - self._grip_size - 1,
                            rect.bottom() - self._grip_size - 1)

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