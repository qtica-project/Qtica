from typing import Union
from PySide6.QtCore import QFileInfo, QSize, Qt
from PySide6.QtGui import QIcon, QIconEngine, QImage, QPixmap, QPainter, QColor
from PySide6.QtWidgets import QFileIconProvider
from ..core.base import BehaviorDeclarative
from ..enums._abs_icons import AbstractIcons


class Icon(BehaviorDeclarative):
    def __init__(self, 
                 icon: Union[str,
                             QIcon,
                             QIconEngine,
                             QPixmap,
                             QImage,
                             AbstractIcons],
                 color: QColor = None,
                 size: QSize = None,
                 **kwargs) -> QIcon:

        if isinstance(icon, AbstractIcons):
            icon = icon.value

        if (isinstance(icon, str)
            and icon.endswith(".svg")
            and color is not None):
            return self._colored_icon(icon, color, size)

        if color is not None:
            return self._colored_icon(icon, color, size)

        return QIcon(icon)

    @classmethod
    def _colored_icon(cls,
                      icon,
                      color,
                      size: QSize = None) -> QIcon:
        icon = QIcon(icon)
        _size = (icon.availableSizes()[0] 
                 if len(icon.availableSizes()) > 0 
                 else icon.actualSize(QSize(32, 32)))
        pixmap = icon.pixmap(size if size is not None else _size)

        pixmap_painter = QPainter(pixmap)
        pixmap_painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceIn)
        pixmap_painter.fillRect(pixmap.rect(),
                                color 
                                if color is not None 
                                else -1)
        pixmap_painter.end()
        return QIcon(pixmap)

    @classmethod
    def make_svg(cls, 
                 svg: str,
                 color: QColor = None) -> QIcon:

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

    @classmethod
    def file_provider(cls, icon: str | QFileInfo) -> QIcon:
        '''
        param: icon = [file.ext, /path/to/file.ext]
        '''
        return QFileIconProvider().icon(QFileInfo(icon) 
                                        if isinstance(icon, str) 
                                        else icon)