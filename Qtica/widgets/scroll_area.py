from typing import Union
from PySide6.QtWidgets import QLayout, QScrollArea, QWidget
from ..core import AbstractWidget


class ScrollArea(AbstractWidget, QScrollArea):
    def __init__(self, 
                 *,
                 child: Union[QWidget, QLayout] = None,
                 **kwargs):
        QScrollArea.__init__(self)

        self.setWidgetResizable(True)

        super().__init__(**kwargs)

        if not child:
            return

        if isinstance(child, QLayout):
            self.scrollAreaWidgetContents = QWidget()
            child.setProperty("parent", self.scrollAreaWidgetContents)
            self.scrollAreaWidgetContents.setLayout(child)
            self.setWidget(self.scrollAreaWidgetContents)
        elif isinstance(child, QWidget):
            self.setWidget(child)