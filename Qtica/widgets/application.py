import os
import sys
import signal

from ..core import AbstractQObject
from typing import Callable, NoReturn, Optional, Union

from qtpy.QtCore import QResource, Qt, Signal, qRegisterResourceData
from qtpy.QtWidgets import QApplication, QStyleFactory, QWidget
from qtpy.QtGui import QFontDatabase


class Application(AbstractQObject, QApplication):
    on_inactive = Signal()
    on_active = Signal()
    on_hidden = Signal()
    on_suspend = Signal()

    def __init__(self,
                 *args,
                 resources: list[Union[str, tuple[Optional[int], bytes, bytes, bytes]]] = None,
                 fonts: list[str] = None,
                 **kwargs):
        QApplication.__init__(self, *args)

        if resources is not None:
            self._set_resources(resources)

        if fonts is not None:
            self._set_fonts(fonts)

        super().__init__(**kwargs)

        self.applicationStateChanged.connect(self._applicationStateChanged)

    def _applicationStateChanged(self, event) -> None:
        if event == Qt.ApplicationState.ApplicationInactive:
            self.on_inactive.emit()
        elif event == Qt.ApplicationState.ApplicationActive:
            self.on_active.emit()
        elif event == Qt.ApplicationState.ApplicationHidden:
            self.on_hidden.emit()
        elif event == Qt.ApplicationState.ApplicationSuspended:
            self.on_suspend.emit()

    def run(self, term_exit: bool = False) -> NoReturn:
        if term_exit:
            signal.signal(signal.SIGINT, signal.SIG_DFL)
        return sys.exit(self.exec())

    def style_list(self) -> list[str]:
        return QStyleFactory.keys()

    def current_style(self) -> str:
        return self.style().name()

    def add_rcc_file(self,
                     rcc_file: str,
                     rcc_root: str = None) -> bool:
        return QResource.registerResource(rcc_file, rcc_root or "")

    def add_font(self, fontpath: str) -> int:
        return QFontDatabase.addApplicationFont(fontpath)

    def _set_fonts(self, fonts: list[str]):
        for font in fonts:
            if not os.path.exists(font):
                raise FileNotFoundError(f"font file not found, '{font}'")
            self.add_font(font)

    def _set_resources(self, resources: list[Union[Callable, tuple[Optional[int], bytes, bytes, bytes]]]):
        '''
        :param: resource
            callable = qInitResources
            tuple = (0x03 | None, qt_resource_struct, qt_resource_name, qt_resource_data)
        '''
        for res in resources:
            if isinstance(res, (tuple, list, set)):
                if len(res) < 4:
                    res = list(res)
                    res.insert(0, 0x03)
                qRegisterResourceData(res[0] if res[0] is not None else 0x03, *res[1:])
            elif callable(res):
                try:
                    res()
                except Exception:
                    continue

    @staticmethod
    def active_window() -> QWidget:
        return QApplication.activeWindow()

    @staticmethod
    def active_modal() -> QWidget:
        return QApplication.activeModalWidget()

    @staticmethod
    def active_popup() -> QWidget:
        return QApplication.activePopupWidget()


class App(Application):
    pass