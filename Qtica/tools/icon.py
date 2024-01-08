from typing import Union
from PySide6.QtGui import QIcon, QIconEngine, QImage, QPixmap, QPainter, QColor
from PySide6.QtWidgets import QFileIconProvider
from PySide6.QtCore import QFileInfo, QSize, Qt
from ..core import AbstractTool, AbstractIcons


class Icon(AbstractTool, QIcon):
    def __init__(self,
                 icon: Union[str,
                             QIcon,
                             QIconEngine,
                             QPixmap,
                             QImage,
                             AbstractIcons],
                 color: QColor = None,
                 size: Union[QSize, tuple, int] = None,
                 **kwargs):

        if isinstance(icon, AbstractIcons):
            icon = icon.value

        if color is not None or size is not None:
            icon = self.colored_icon(icon, color, size)

        QIcon.__init__(self, icon)
        super().__init__(**kwargs)

    @classmethod
    def colored_icon(cls,
                     icon,
                     color: QColor,
                     size: Union[QSize, tuple, int] = None) -> QIcon:

        if isinstance(size, int):
            size = QSize(size, size)

        if isinstance(size, (tuple, list, set)):
            size = QSize(*size[:2])

        icon = QIcon(icon)
        default_size = (icon.availableSizes()[0] 
                        if len(icon.availableSizes()) > 0 
                        else icon.actualSize(QSize(32, 32)))

        pixmap = icon.pixmap(size 
                             if size is not None 
                             else default_size)

        pixmap_painter = QPainter(pixmap)
        pixmap_painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceIn)

        if color is not None:
            pixmap_painter.fillRect(pixmap.rect(), color if color is not None else 0)

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
    def file_provider(cls, icon: Union[str, QFileInfo]) -> QIcon:
        '''
        param: icon = [file.ext, /path/to/file.ext]
        '''
        return QFileIconProvider().icon(QFileInfo(icon) 
                                        if isinstance(icon, str) 
                                        else icon)