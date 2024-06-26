from ..core import AbstractTool
from qtpy.QtWidgets import QSpacerItem, QSizePolicy


class SpacerItem(AbstractTool, QSpacerItem):
    Policy = QSizePolicy.Policy
    def __init__(self, *args, **kwargs):
        QSpacerItem.__init__(self, *args)
        super().__init__(**kwargs)