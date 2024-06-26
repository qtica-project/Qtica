from PySide6.QtCore import QFile, QTemporaryFile
from ..core import AbstractIODevice


class OpenFile(AbstractIODevice, QFile):
    def __init__(self, 
                 file: str,
                 mode: QFile.OpenModeFlag = QFile.OpenModeFlag.ReadOnly,
                 **kwargs):
        QFile.__init__(self, file)
        super().__init__(mode, **kwargs)


class TempFile(AbstractIODevice, QTemporaryFile):
    def __init__(self, 
                 name: str = None,
                 mode: QTemporaryFile.OpenModeFlag = QTemporaryFile.OpenModeFlag.WriteOnly,
                 **kwargs) -> None:

        if name is not None:
            QTemporaryFile.__init__(self, name)
        else:
            QTemporaryFile.__init__(self)
        super().__init__(mode, **kwargs)

    def __exit__(self, exception_type, exception_value, exception_traceback) -> None:
        self.close()
        if self.autoRemove():
            self.remove()