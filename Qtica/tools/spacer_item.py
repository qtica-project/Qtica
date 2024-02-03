#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QSpacerItem
from ..core import AbstractTool


class SpacerItem(AbstractTool, QSpacerItem):
    def __init__(self, *args, **kwargs):
        QSpacerItem.__init__(self, *args)
        super().__init__(**kwargs)
