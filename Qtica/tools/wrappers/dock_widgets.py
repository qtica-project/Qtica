#!/usr/bin/python3

from typing import Any
from dataclasses import dataclass
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDockWidget


@dataclass
class DockWidgetWrapper:
    area: Qt.DockWidgetArea
    dockwidget: QDockWidget
    orient: Qt.Orientation = None

    def _args(self) -> list[Any]:
        return [self.area, self.dockwidget, self.orient]
