from typing import Union
from enum import Enum, auto
from ..utils.caseconverter import camelcase

from PySide6.QtCore import QMimeData
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QClipboard, QImage, QPixmap


class Clipboard:
    Mode = QClipboard.Mode
    class Types(Enum):
        mime_data = auto()
        pixmap = auto()
        image = auto()
        text = auto()

    @classmethod
    def paste_data(
        cls,
        dtype: Types = Types.text,
        mode: QClipboard.Mode = QClipboard.Mode.Clipboard,
    ) -> Union[QMimeData, str, QImage, QPixmap]:

        return getattr(QApplication.clipboard(), camelcase(dtype.name))(mode)

    @classmethod
    def copy_data(
        cls,
        data: Union[QMimeData, QImage, QPixmap, str],
        dtype: Types = Types.text,
        mode: QClipboard.Mode = QClipboard.Mode.Clipboard,
    ) -> None:

        return getattr(QApplication.clipboard(), camelcase("set_"+dtype.name))(data, mode)

    @classmethod
    def copy(
        cls,
        data: Union[QMimeData, QImage, QPixmap, str],
        dtype: Types = Types.text,
        mode: QClipboard.Mode = QClipboard.Mode.Clipboard
    ) -> None:
        return cls.copy_data(data, dtype, mode)

    @classmethod
    def paste(
        cls,
        dtype: Types = Types.text,
        mode: QClipboard.Mode = QClipboard.Mode.Clipboard
    ) -> Union[QMimeData, str, QImage, QPixmap]:
        return cls.paste_data(dtype, mode)