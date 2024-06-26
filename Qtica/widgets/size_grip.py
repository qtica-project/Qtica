from PySide6.QtWidgets import QSizeGrip
from PySide6.QtGui import QMouseEvent
from PySide6.QtCore import QRect, Qt
from ..services import corner_to_edge
from ..core import AbstractWidget


class WindowSizeGrip(AbstractWidget, QSizeGrip):
    def __init__(self,
                 *,
                 corner: Qt.Corner = Qt.Corner.BottomRightCorner,
                 **kwargs) -> None:
        QSizeGrip.__init__(self)
        super().__init__(**kwargs)

        self._corner = corner
        self.set_cursor_for_position(corner)

    def set_cursor_for_position(self, corner: Qt.Corner):
        self.setCursor({
            Qt.Corner.TopLeftCorner: Qt.CursorShape.SizeFDiagCursor,
            Qt.Corner.TopRightCorner: Qt.CursorShape.SizeBDiagCursor,
            Qt.Corner.BottomLeftCorner: Qt.CursorShape.SizeBDiagCursor,
            Qt.Corner.BottomRightCorner: Qt.CursorShape.SizeFDiagCursor,
        }.get(corner, Qt.CursorShape.ArrowCursor))

    def _move(self) -> None:
        if self.parent() is not None:
            rect: QRect = self.parent().rect()

            if self._corner == Qt.Corner.TopLeftCorner:
                self.move(
                    rect.x(),
                    0
                )

            elif self._corner == Qt.Corner.TopRightCorner:
                x, y = rect.topRight().toTuple()
                self.move(x - (self.width() + 5), y - 5)

            elif self._corner == Qt.Corner.BottomLeftCorner:
                self.move(0, rect.bottom() - self.height())

            elif self._corner == Qt.Corner.BottomRightCorner:
                self.move(rect.right() - self.width() - 1, 
                          rect.bottom() - self.height() - 1)

    def mousePressEvent(self, arg__1: QMouseEvent) -> None:
        self.parent().windowHandle().startSystemResize(corner_to_edge(self._corner))
        return super().mousePressEvent(arg__1)

    def updateGeometry(self) -> None:
        self._move()
        return super().updateGeometry()