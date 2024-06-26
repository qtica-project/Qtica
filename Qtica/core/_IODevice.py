from ._qobject import AbstractQObject

from qtpy.QtCore import QIODevice


class AbstractIODevice(AbstractQObject):
    def __init__(self, mode: QIODevice.OpenModeFlag, **kwargs):
        super().__init__(**kwargs)
        self._mode = mode

    def __enter__(self):
        self.open(self._mode)
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback) -> None:
        self.close()

    def read_with_utf_8(self) -> str:
        return str(self.readAll(), encoding='utf-8')

    def readUtf8(self) -> str:
        return self.read_with_utf_8()