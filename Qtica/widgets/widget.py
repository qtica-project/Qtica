from ..core import AbstractContainer, ContainerChildType
from qtpy.QtWidgets import QWidget


class WidgetContainer(AbstractContainer, QWidget):
    def __init__(self, *, child: ContainerChildType = None, **kwargs):
        QWidget.__init__(self)
        super().__init__(child, **kwargs)
