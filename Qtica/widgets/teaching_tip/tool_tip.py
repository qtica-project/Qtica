from PySide6.QtCore import Qt, QEvent
from PySide6.QtGui import QPainter, QColor
from PySide6.QtWidgets import QGridLayout, QWidget

from darkdetect import isDark as isDarkTheme

from ...enums.events import EventTypeVar
from ...enums.signals import SignalTypeVar
from ...enums import TeachingTipTailPositions
from .tails import TeachingTipManager


class _TeachingTip(QWidget):
    def __init__(self, 
                 view: QWidget,
                 target: QWidget,
                 tail_position: TeachingTipTailPositions = TeachingTipTailPositions.bottom,
                 delete_on_close: bool = False,
                 radius: int = 6,
                 parent: QWidget = None
                ) -> None:
        super().__init__(parent=parent)

        self.view = view
        self.target = target
        self.delete_on_close = delete_on_close
        self.manager = TeachingTipManager.make(tail_position)
        self.manager.radius = radius

        self._layout = QGridLayout(self)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        self.manager.doLayout(self)

        self._layout.addWidget(view)

        # set style
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
        self.setWindowFlags(Qt.WindowType.Tool | Qt.WindowType.FramelessWindowHint)

        if parent and parent.window():
            parent.window().installEventFilter(self)

        if self.target is not None:
            self.target.resizeEvent = lambda e: self.update_pos()
            self.target.moveEvent = lambda e: self.update_pos()
            self.target.window().moveEvent = lambda e: self.update_pos()

    def tooltip_pos(self):
        return self.manager.position(self)

    def set_target(self, target: QWidget):
        self.target = target
        self.target.resizeEvent = lambda e: self.update_pos()
        self.target.moveEvent = lambda e: self.update_pos()
        self.target.window().moveEvent = lambda e: self.update_pos()

    def update_pos(self):
        self.move(self.manager.position(self))

    def showEvent(self, e):
        self.update_pos()
        super().showEvent(e)

    def closeEvent(self, e):
        if self.delete_on_close:
            self.deleteLater()
        super().closeEvent(e)

    def eventFilter(self, obj, e: QEvent):
        if self.parent() and obj is self.parent().window():
            if e.type() in [QEvent.Type.Resize, 
                            QEvent.Type.WindowStateChange, 
                            QEvent.Type.Move]:
                self.move(self.manager.position(self))
        return super().eventFilter(obj, e)

    def paintEvent(self, e, scale: float = None):
        super().paintEvent(e)

        painter = QPainter(self)
        painter.setRenderHints(QPainter.RenderHint.Antialiasing)

        painter.setBrush(
            QColor(40, 40, 40) 
            if isDarkTheme() 
            else QColor(248, 248, 248))
        
        painter.setPen(
            QColor(23, 23, 23) 
            if isDarkTheme() 
            else QColor(195, 195, 195))

        self.manager.draw(self, painter)


from ...core.base import WidgetBase

class TeachingTip(WidgetBase, _TeachingTip):
    def __init__(self, 
                 child: QWidget,
                 target: QWidget,
                 tail_position: TeachingTipTailPositions = TeachingTipTailPositions.bottom,
                 delete_on_close: bool = False,
                 radius: int = 6,
                 uid: str = None, 
                 signals: SignalTypeVar = None, 
                 events: EventTypeVar = None, 
                 qss: str | dict = None, 
                 attrs: list[Qt.WidgetAttribute] | dict[Qt.WidgetAttribute, bool] = None, 
                 flags: list[Qt.WindowType] | dict[Qt.WindowType, bool] = None,
                 **kwargs):
        _TeachingTip.__init__(self, child, target, tail_position, delete_on_close, radius)
        super().__init__(uid, signals, events, qss, attrs, flags, **kwargs)