import os

from typing import Union
from ..core import QObjectDec

from qtpy.QtCore import QIODevice
from qtpy.QtUiTools import QUiLoader
from qtpy.QtWidgets import QWidget


class UiLoader(QObjectDec, QUiLoader):
    '''
    UiLoader(
        ui="/path/to/file.ui",
        ...
    ) # -> QWidget
    '''

    def __init__(self, ui: Union[str, bytes, os.PathLike, QIODevice], **kwargs) -> QWidget:
        QUiLoader.__init__(self)
        super().__init__(**kwargs)

        return self.load(ui)