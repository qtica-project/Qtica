from ..core import AbstractContainer, ContainerChildType
from qtpy.QtWidgets import QGroupBox


class GroupBox(AbstractContainer, QGroupBox):
    def __init__(self, *, child: ContainerChildType = None, **kwargs):
        QGroupBox.__init__()
        super().__init__(child, **kwargs)
