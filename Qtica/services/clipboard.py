from typing import Union
from PySide6.QtCore import QMimeData
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QClipboard, QImage, QPixmap
from ..enums.clipboard import ClipboardDataTypes


class Clipboard:
    @staticmethod
    def paste_data(
        data_type: ClipboardDataTypes = ClipboardDataTypes.text,
        mode: QClipboard.Mode = QClipboard.Mode.Clipboard,
    ) -> Union[QMimeData, str, QImage, QPixmap]:

        cb = QApplication.clipboard()
        match data_type:
            case ClipboardDataTypes.image:
                return cb.image(mode)
            case ClipboardDataTypes.pixmap:
                return cb.pixmap(mode)
            case ClipboardDataTypes.mimedata:
                return cb.mimeData(mode)
            case ClipboardDataTypes.text:
                return cb.text(mode)

    @staticmethod
    def copy_data(
        data: Union[QMimeData, str, QImage, QPixmap],
        data_type: ClipboardDataTypes = ClipboardDataTypes.text,
        mode: QClipboard.Mode = QClipboard.Mode.Clipboard,
    ) -> None:

        cb = QApplication.clipboard()
        match data_type:
            case ClipboardDataTypes.image:
                return cb.setImage(data, mode)
            case ClipboardDataTypes.pixmap:
                return cb.setPixmap(data, mode)
            case ClipboardDataTypes.mimedata:
                return cb.setMimeData(data, mode)
            case ClipboardDataTypes.text:
                return cb.setText(data, mode)

    @staticmethod
    def copy(
        data: Union[QMimeData, str, QImage, QPixmap],
        data_type: ClipboardDataTypes = ClipboardDataTypes.text,
        mode: QClipboard.Mode = QClipboard.Mode.Clipboard,
    ) -> None:
        return Clipboard.copy_data(data, data_type, mode)

    @staticmethod
    def paste(
        data_type: ClipboardDataTypes = ClipboardDataTypes.text,
        mode: QClipboard.Mode = QClipboard.Mode.Clipboard,
    ) -> Union[QMimeData, str, QImage, QPixmap]:
        return Clipboard.paste_data(data_type, mode)