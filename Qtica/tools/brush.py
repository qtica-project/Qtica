#!/usr/bin/python3

from PySide6.QtGui import QBrush
from ..core import AbstractTool


class Brush(AbstractTool, QBrush):
    def __init__(self, **kwargs):
        QBrush.__init__(self)
        super().__init__(**kwargs)