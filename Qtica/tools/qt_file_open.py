from PySide6.QtCore import QFile


class File(QFile):
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
        return str(self.readAll(), 
                   encoding='utf-8')