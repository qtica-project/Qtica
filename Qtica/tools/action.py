#!/usr/bin/python3

from PySide6.QtGui import QAction
from ..core import QObjectBase


class Action(QObjectBase, QAction):
    def __init__(self, **kwargs):
        QAction.__init__(self)
        super().__init__(**kwargs)