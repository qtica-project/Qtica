from enum import Enum, auto
from typing import Callable, Optional

from PySide6.QtCore import QRect, QSize, QTimer, Qt
from PySide6.QtGui import QColor, QIcon, QMouseEvent, QPainter, QPaintEvent
from PySide6.QtWidgets import QGridLayout, QLabel, QToolButton, QWidget

from ..teaching_tip.tool_tip import _TeachingTip
from ...enums.teaching_tip_tails import TeachingTipTailPositions
from ...core.base import WidgetBase


class NavBarButton(WidgetBase, QToolButton):
    class Alignment(Enum):
        left = auto()
        right = auto()
        center = auto()

    def __init__(
        self, 
        icon: QIcon,
        tool_tip: Optional[str] = None,
        radius: int = 8,
        bg_color: QColor = QColor("#191E23"),
        on_color: QColor = QColor("#282D32"),
        edge_color: QColor = None,
        icon_off: QIcon = None,
        icon_on: QIcon = None,
        clicked: Callable = None,
        **kwargs
    ) -> None:
        QToolButton.__init__(self)
        super().__init__(**kwargs)

        if clicked is not None:
            self.clicked.connect(clicked)

        # Set attributes from arguments
        self._icon = icon
        self._radius = radius
        self._tool_tip: Optional[_TeachingTip] = None

        self._icon_off = icon_off if icon_off is not None else icon
        self._icon_on = icon_on if icon_on is not None else icon

        if tool_tip:
            _tool_tip_widget = QWidget()
            _tool_tip_grid = QGridLayout(_tool_tip_widget)
            _label = QLabel(tool_tip)
            _label.setWordWrap(True)

            _tool_tip_grid.addWidget(_label)
            _tool_tip_widget.setLayout(_tool_tip_grid)

            self._tool_tip = _TeachingTip(
                _tool_tip_widget,
                self,
                TeachingTipTailPositions.bottom
            )

        self._bg_color = bg_color
        self._h1_color = edge_color
        self._on_color = on_color

        # Set QToolButton properties
        self.setCheckable(True)
        self.setMouseTracking(True)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        self._timer = QTimer(self)
        self._timer.timeout.connect(self._start_tooltip)

    def _start_tooltip(self):
        if self._tool_tip.isHidden():
            self._tool_tip.show()

    def enterEvent(self, arg__1) -> None:
        if self._tool_tip and self.underMouse():
            self._timer.start(1000)

        return super().enterEvent(arg__1)

    def leaveEvent(self, arg__1) -> None:
        if self._tool_tip:
            self._timer.stop()
            self._tool_tip.hide()

        return super().leaveEvent(arg__1)

    def setBackgroundColor(self, color: QColor = QColor("#191E23")):
        self._bg_color = color
        self.update()

    def setEdgeColor(self, color: QColor = QColor("#0066FF")):
        self._h1_color = color
        self.update()

    def setOnColor(self, color: QColor = QColor("#282D32")):
        self._on_color = color
        self.update()

    def minimumSizeHint(self) -> QSize:
        return QSize(32, 32)

    def mousePressEvent(self, arg__1: QMouseEvent) -> None:
        if self._tool_tip:
            self._timer.stop()
            self._tool_tip.hide()
        return super().mousePressEvent(arg__1)

    def paintEvent(self, event: QPaintEvent) -> None:
        super().paintEvent(event)

        # Define areas for painting
        radius = self._radius
        width = self.width()
        height = self.height()

        self.rect_background = QRect(0, 0, width, height)
        self.rect_icon = QRect(width // 4, 
                               height // 4, 
                               width // 2, 
                               height // 2)

        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setPen(Qt.PenStyle.NoPen)

        # Draw background
        painter.setBrush(self._bg_color)
        painter.drawRect(self.rect_background)

        if self.isChecked():
            # Draw bottom highlight area
            if self._h1_color is not None:
                painter.setBrush(self._h1_color)
                painter.drawRoundedRect(
                    QRect(
                        radius,
                        height - 2, 
                        height - 2 * radius,
                        2 * radius), 

                    self._radius, 
                    self._radius
                )

            # Draw middle and right active area
            painter.setBrush(self._on_color)
            painter.drawRoundedRect(
                QRect(
                    radius, 
                    radius, 
                    width - 2 * radius, 
                    height - 2 * radius
                ), 
                self._radius, 
                self._radius
            )
            self._icon_on.paint(painter, self.rect_icon)

        elif self.underMouse():
            painter.setBrush(self._on_color)
            painter.drawRoundedRect(
                QRect(
                    radius, 
                    radius, 
                    width - 2 * radius, 
                    height - 2 * radius
                ), 
                self._radius, 
                self._radius
            )
            self._icon_on.paint(painter, self.rect_icon)
        else:
            self._icon_off.paint(painter, self.rect_icon)

        painter.end()