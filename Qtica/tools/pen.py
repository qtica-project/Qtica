#!/usr/bin/python3

from PySide6.QtGui import QPen
from ..core import AbstractTool


class Pen(AbstractTool, QPen):
    def __init__(self, **kwargs):
        QPen.__init__(self)
        super().__init__(**kwargs)