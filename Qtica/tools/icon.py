from typing import Union
from PySide6.QtCore import QFileInfo, QSize, Qt
from PySide6.QtGui import QIcon, QIconEngine, QImage, QPixmap, QPainter
from PySide6.QtWidgets import QFileIconProvider
from ..core.base import BehaviorDeclarative
from .color import Color


class Icon(BehaviorDeclarative):
    def __init__(self, 
                 icon: Union[QIcon, 
                             QIconEngine, 
                             str, 
                             QPixmap],
                 color: Color = None,
                 size: QSize = None,
                 **kwargs) -> QIcon:

        if (isinstance(icon, str)
            and icon.endswith(".svg")
            and color is not None):
            return self._colored_icon(icon, color, size)

        if color is not None:
            return self._colored_icon(icon, color, size)

        return QIcon(icon)

    def _colored_icon(self, 
                      icon, 
                      color: Color = None) -> QIcon:

        pixmap = QPixmap(icon)
        pixmap_painter = QPainter(pixmap)
        pixmap_painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceIn)
        pixmap_painter.fillRect(pixmap.rect(), color if color is not None else -1)
        pixmap_painter.end()
        return QIcon(pixmap)

    @staticmethod
    def make_svg(svg: str, color: Color = None) -> QIcon:
        image = QImage()
        image.fill(Qt.GlobalColor.transparent)
        image.loadFromData(bytes(svg, "utf-8"))
        pixmap = QPixmap.fromImage(image, Qt.ImageConversionFlag.NoFormatConversion)

        if color is not None:
            pixmap_painter = QPainter(pixmap)
            pixmap_painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceIn)
            pixmap_painter.fillRect(pixmap.rect(), color if color is not None else -1)
            pixmap_painter.end()

        return QIcon(pixmap)

    @staticmethod
    def file_provider(icon: str | QFileInfo) -> QIcon:
        '''
        param: icon = [file.ext, /path/to/file.ext]
        '''
        return QFileIconProvider().icon(QFileInfo(icon) 
                                        if isinstance(icon, str) 
                                        else icon)