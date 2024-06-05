from PySide6.QtCore import QFile, QTemporaryFile
from PySide6.QtCore import QIODevice
from ..core import AbstractQObject


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


class OpenFile(AbstractIODevice, QFile):
    def __init__(self, 
                 file: str,
                 mode: QFile.OpenModeFlag = QFile.OpenModeFlag.ReadOnly,
                 **kwargs):
        QFile.__init__(self, file)
        super().__init__(mode, **kwargs)


class TempFile(AbstractIODevice, QTemporaryFile):
    def __init__(self, 
                 mode: QTemporaryFile.OpenModeFlag = QTemporaryFile.OpenModeFlag.WriteOnly,
                 name: str = None,
                 **kwargs) -> None:
        QTemporaryFile.__init__(self, name)
        super().__init__(mode, **kwargs)

    def __exit__(self, exception_type, exception_value, exception_traceback) -> None:
        self.close()
        if self.autoRemove():
            self.remove()