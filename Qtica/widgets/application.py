#!/usr/bin/python3

import sys

from typing import Sequence
from PySide6.QtCore import QResource, Qt, Signal
from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import QApplication, QStyleFactory
# from .._rc.resource import qInitResources


class Application(QApplication):
    on_inactive = Signal()
    on_active = Signal()
    on_hidden = Signal()
    on_suspend = Signal()

    def __init__(self, arg: Sequence[str] = None) -> None:
        super().__init__(arg or [])

        # qInitResources()

        ## it's default enabled by the developer 
        self.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps, True)
        self.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)
        self.setAttribute(Qt.ApplicationAttribute.AA_DontCreateNativeWidgetSiblings, True)

        self.applicationStateChanged.connect(self._applicationStateChanged)

    def _applicationStateChanged(self, event):
        if event == Qt.ApplicationState.ApplicationInactive:
            self.on_inactive.emit()
        elif event == Qt.ApplicationState.ApplicationActive:
            self.on_active.emit()
        elif event == Qt.ApplicationState.ApplicationHidden:
            self.on_hidden.emit()
        elif event == Qt.ApplicationState.ApplicationSuspended:
            self.on_suspend.emit()

    def run(self) -> int:
        return sys.exit(self.exec())

    def list_styles(self) -> list[str]:
        return QStyleFactory.keys()

    def current_style(self) -> str:
        return self.style().name()

    def set_style(self, name: str):
        if name.lower().strip() not in [n.lower() for n in QStyleFactory.keys()]:
            raise ValueError(f"style '{name}' not found please call list_styles to \
                see all available styles in your system.")

        self.setStyle(QStyleFactory.create(name))

    def set_resource(self,
                     rcc_file: str,
                     rcc_root: str = None) -> bool:

        if rcc_root is not None:
            return QResource.registerResource(rcc_file, rcc_root)

        return QResource.registerResource(rcc_file)

    def add_font(self, fontpath: str):
        QFontDatabase.addApplicationFont(fontpath)


class App(Application):
    pass