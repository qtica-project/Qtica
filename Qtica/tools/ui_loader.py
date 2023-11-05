from PySide6.QtCore import QObject
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QWidget
from .qt_file_open import File
from ..core.base import BehaviorDeclarative
import os


class UILoader(BehaviorDeclarative):
    def __init__(self, 
                 file: str, 
                 parent: QObject = None) -> QWidget:

        loader = QUiLoader(parent)

        if not os.path.exists(file):
            return loader.load(file, parent)

        with File(file, File.OpenModeFlag.ReadOnly) as fr:
            return loader.load(fr, parent)