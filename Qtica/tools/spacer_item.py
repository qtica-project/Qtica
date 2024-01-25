#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QSpacerItem, QSizePolicy
from ..core import AbstractTool


class SpacerItem(AbstractTool, QSpacerItem):
    def __init__(self, 
                 width: int, 
                 height: int, 
                 wPolicy: QSizePolicy.Policy = QSizePolicy.Policy.Minimum, 
                 hPolicy: QSizePolicy.Policy = QSizePolicy.Policy.Minimum, 
                 **kwargs):
        QSpacerItem.__init__(self, width, height, wPolicy, hPolicy)
        super().__init__(**kwargs)