from PySide6.QtWidgets import QLineEdit
from ..core import AbstractWidget


class LineEdit(AbstractWidget, QLineEdit):
    def __init__(self, **kwargs):
        QLineEdit.__init__(self)
        super().__init__(**kwargs)