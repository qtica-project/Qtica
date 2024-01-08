#!/usr/bin/python3

from dataclasses import dataclass
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QToolBar


@dataclass
class ToolBarWrapper:
    area: Qt.ToolBarArea
    toolbar: QToolBar

@dataclass
class ToolBarBreakWrapper:
    area: Qt.ToolBarArea = None
