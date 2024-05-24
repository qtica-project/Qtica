from typing import Union
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QLayout, QScrollArea, QWidget
from ..core import AbstractWidget


class ScrollArea(AbstractWidget, QScrollArea):
    def __init__(self, 
                 *,
                 child: Union[QWidget, QLayout] = None,
                 **kwargs):
        QScrollArea.__init__(self)

        self.setWidgetResizable(True)
        self.setUpdatesEnabled(True)

        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setSizeAdjustPolicy(QScrollArea.SizeAdjustPolicy.AdjustToContents)

        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setFrameShadow(QFrame.Shadow.Raised)

        super().__init__(**kwargs)

        if child is not None:
            if isinstance(child, QLayout):
                _widget = QWidget()
                child.setProperty("parent", _widget)
                _widget.setLayout(child)
                child = _widget
            self.setWidget(child)