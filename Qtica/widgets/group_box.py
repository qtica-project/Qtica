from PySide6.QtWidgets import QGroupBox
from ..core import AbstractContainer, ContainerChildType


class GroupBox(AbstractContainer, QGroupBox):
    def __init__(self, *, child: ContainerChildType = None, **kwargs):
        QGroupBox.__init__()
        super().__init__(child, **kwargs)
