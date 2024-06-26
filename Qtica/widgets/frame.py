from ..core import AbstractContainer, ContainerChildType
from qtpy.QtWidgets import QFrame


class FrameContainer(AbstractContainer, QFrame):
    def __init__(self, *, child: ContainerChildType = None, **kwargs):
        QFrame.__init__(self)
        super().__init__(child, **kwargs)


class Container(FrameContainer):
    pass