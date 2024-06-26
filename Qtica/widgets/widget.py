from PySide6.QtWidgets import QWidget
from ..core import AbstractContainer, ContainerChildType


class WidgetContainer(AbstractContainer, QWidget):
    def __init__(self, *, child: ContainerChildType = None, **kwargs):
        QWidget.__init__(self)
        super().__init__(child, **kwargs)
