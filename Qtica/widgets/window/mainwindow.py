#!/usr/bin/python3

from ...core import AbstractWidget
from .base import BaseWindow


class MainWindow(AbstractWidget, BaseWindow):
    def __init__(self, **kwargs):
        BaseWindow.__init__(self, **kwargs)
        super().__init__(**kwargs)