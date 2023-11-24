#!/usr/bin/python3

import os
import sys

from typing import Sequence, Union, Iterable
# from PySide6 import QtCore
from PySide6.QtGui import QFontDatabase
from PySide6.QtCore import QResource, Qt, Signal, qRegisterResourceData
from PySide6.QtWidgets import QApplication, QStyleFactory

from ..enums.events import EventTypeVar
from ..enums.signals import SignalTypeVar
from ..core.base import ObjectBase
from ..utils._import import Imports
from .._rc.resource import qInitResources


class Application(ObjectBase, QApplication):
    on_inactive = Signal()
    on_active = Signal()
    on_hidden = Signal()
    on_suspend = Signal()

    def __init__(self,
                 arg: Sequence[str] = None,
                 resources: list[Union[str, tuple]] = None,
                 fonts: list[str] = None,
                 uid: str = None, 
                 signals: SignalTypeVar = None,
                 events: EventTypeVar = None, 
                 **kwargs):
        QApplication.__init__(self, arg or [])
        super().__init__(uid, signals, events, **kwargs)

        # init Qtica default resource
        qInitResources()

        if resources is not None:
            self._set_resources(resources)

        if fonts is not None:
            self._set_fonts(fonts)

        ## it's default enabled by the developer
        self.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps, True)
        self.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)

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

    def add_rcc_file(self,
                     rcc_file: str,
                     rcc_root: str = None) -> bool:

        if rcc_root is not None:
            return QResource.registerResource(rcc_file, 
                                              rcc_root)
        return QResource.registerResource(rcc_file)

    def add_font(self, fontpath: str) -> int:
        return QFontDatabase.addApplicationFont(fontpath)

    def _set_fonts(self, fonts: list[str]):
        for font in fonts:
            if not os.path.exists(font):
                raise FileNotFoundError(f"'{font}' font file not found!")

            self.add_font(fonts)

    def _set_resources(self, resources: list[Union[str, tuple]]):
        '''
        * resource.py file must contain the qInitResources method
        * Please comment qInitResources calling in the tail of resource.py the file.
        :param: resource
            str = "/path/to/file.py
            tuple = (qt_resource_struct, qt_resource_name, qt_resource_data)
        '''
        for res in resources:
            if isinstance(res, Iterable):
                qRegisterResourceData(0x03, *res)

            elif res.endswith((".py", ".pyc")):
                if not os.path.exists(res):
                    raise FileNotFoundError(f"'{res}' resource file not found!")
                try:
                    Imports.method(res, "qInitResources")()
                except Exception as err:
                    raise ValueError(f"Resource error: '{res}', {err}")


class App(Application):
    pass