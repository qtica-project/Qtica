from PySide6.QtWidgets import QFrame
from ..core import AbstractContainer, ContainerChildType


class FrameContainer(AbstractContainer, QFrame):
    def __init__(self, *, child: ContainerChildType = None, **kwargs):
        QFrame.__init__(self)
        super().__init__(child, **kwargs)


class Container(FrameContainer):
    pass