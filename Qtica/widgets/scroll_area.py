from PySide6.QtWidgets import QFrame, QScrollArea, QWidget
from PySide6.QtCore import Qt
from ..core import WidgetBase


class ScrollArea(WidgetBase, QScrollArea):
    def __init__(self, 
                 *,
                 child: QWidget = None,
                 **kwargs):
        QScrollArea.__init__(self)
        super().__init__(**kwargs)

        self.setWidgetResizable(True)
        self.setUpdatesEnabled(True)

        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setSizeAdjustPolicy(QScrollArea.SizeAdjustPolicy.AdjustToContents)

        self.setFrameShadow(QFrame.Shadow.Plain)
        self.setFrameShape(QFrame.Shape.NoFrame)

        if child is not None:
            self.setWidget(child)