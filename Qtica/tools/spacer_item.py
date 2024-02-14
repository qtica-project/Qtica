#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QSpacerItem, QSizePolicy
from ..core import AbstractTool


class SpacerItem(AbstractTool, QSpacerItem):
    Policy = QSizePolicy.Policy
    def __init__(self, *args, **kwargs):
        QSpacerItem.__init__(self, *args)
        super().__init__(**kwargs)