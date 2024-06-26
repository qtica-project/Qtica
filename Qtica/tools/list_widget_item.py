from ..core import AbstractTool
from qtpy.QtWidgets import QListWidgetItem


class ListWidgetItem(AbstractTool, QListWidgetItem):
    def __init__(self, *args, **kwargs):
        QListWidgetItem.__init__(self, *args)
        super().__init__(**kwargs)
