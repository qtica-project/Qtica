from PySide6.QtWidgets import QFrame, QScrollArea, QWidget
from PySide6.QtCore import Qt
from ..enums.events import EventTypeVar
from ..enums.signals import SignalTypeVar
from ..core.base import WidgetBase


class ScrollArea(WidgetBase, QScrollArea):
    def __init__(self, 
                 child: QWidget = None,
                 uid: str = None,
                 signals: SignalTypeVar = None, 
                 events: EventTypeVar = None, 
                 qss: str | dict = None, 
                 attrs: list[Qt.WidgetAttribute] | dict[Qt.WidgetAttribute, bool] = None, 
                 flags: list[Qt.WindowType] | dict[Qt.WindowType, bool] = None, 
                 **kwargs):
        QScrollArea.__init__(self)
        super().__init__(uid, signals, events, qss, attrs, flags, **kwargs)

        self.setWidgetResizable(True)
        self.setUpdatesEnabled(True)

        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setSizeAdjustPolicy(QScrollArea.SizeAdjustPolicy.AdjustToContents)

        self.setFrameShadow(QFrame.Shadow.Plain)
        self.setFrameShape(QFrame.Shape.NoFrame)

        if child is not None:
            self.setWidget(child)