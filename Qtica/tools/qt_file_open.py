from PySide6.QtCore import QFile, QTemporaryFile


class OpenFile(QFile):
    def __init__(self, 
                 file: str,
                 mode: QFile.OpenModeFlag = QFile.OpenModeFlag.ReadOnly):
        super().__init__(file)
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



class TempFile(QTemporaryFile):
    def __init__(self, 
                 mode: QTemporaryFile.OpenModeFlag = QTemporaryFile.OpenModeFlag.WriteOnly,
                 name: str = None,
                 *args, 
                 **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._mode = mode
        if name is not None:
            self.setFileName(name)
    
    def __enter__(self):
        self.open(self._mode)
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback) -> None:
        self.close()
        self.remove()

    def read_with_utf_8(self) -> str:
        return str(self.readAll(), encoding='utf-8')

    def readUtf8(self) -> str:
        return self.read_with_utf_8()