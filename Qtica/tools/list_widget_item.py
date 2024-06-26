from PySide6.QtWidgets import QListWidgetItem
from ..core import AbstractTool


class ListWidgetItem(AbstractTool, QListWidgetItem):
    def __init__(self, *args, **kwargs):
        QListWidgetItem.__init__(self, *args)
        super().__init__(**kwargs)
