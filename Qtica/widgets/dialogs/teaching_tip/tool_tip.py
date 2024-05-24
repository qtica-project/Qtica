from PySide6.QtGui import QPainter
from PySide6.QtCore import Qt, QEvent
from PySide6.QtWidgets import QGridLayout, QWidget
from .tails import TeachingTipManager, _TailPos, _TailDirection
from ....core import AbstractDialog


class TeachingTipDialog(AbstractDialog):
    TailPos = _TailPos
    TailDirection = _TailDirection

    def __init__(self,
                 child: QWidget,
                 target: QWidget = None,
                 tail_pos: TailPos = TailPos.bottom,
                 tail_direction: TailDirection = TailDirection.center,
                 tail_len: int = 8,
                 auto_close: bool = True,
                 **kwargs) -> None:
        super().__init__(auto_close=auto_close, **kwargs)

        self._auto_close = auto_close

        self.child = child
        self.target = target

        self.manager = TeachingTipManager.make(tail_pos)
        self.manager.direction = tail_direction
        self.manager.lenght = tail_len

        self._layout = QGridLayout(self)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)

        self.manager.doLayout(self)

        self._layout.addWidget(child)

        # set style
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
        self.setWindowFlags(
            Qt.WindowType.Tool
            | Qt.WindowType.FramelessWindowHint)

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

        bg_color = self.child.palette().brush(self.child.backgroundRole())

        painter.setBrush(bg_color)
        painter.setPen(bg_color.color())

        self.manager.draw(self, painter)