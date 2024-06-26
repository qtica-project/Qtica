from PySide6.QtWidgets import QBoxLayout, QHBoxLayout, QVBoxLayout
from ..core import AbstractBoxLayout, BoxLayoutChildrenType


class BoxLayout(AbstractBoxLayout, QBoxLayout):
    def __init__(self, *, 
                 direction: QBoxLayout.Direction,
                 children: BoxLayoutChildrenType = None, 
                 **kwargs):

        QBoxLayout.__init__(self, direction)
        super().__init__(children, **kwargs)


class VLayout(AbstractBoxLayout, QVBoxLayout):
    def __init__(self, *, children: BoxLayoutChildrenType = None, **kwargs):
        QVBoxLayout.__init__(self)
        super().__init__(children, **kwargs)


class HLayout(AbstractBoxLayout, QHBoxLayout):
    def __init__(self, *, children: BoxLayoutChildrenType = None, **kwargs):
        QHBoxLayout.__init__(self)
        super().__init__(children, **kwargs)


class Row(VLayout):
    ...

class Column(HLayout):
    ...