from typing import Union
from ..enums import Colors
from ..core import AbstractTool, AbstractIcons

from qtpy.QtGui import QIcon, QIconEngine, QImage, QPixmap, QPainter, QColor
from qtpy.QtWidgets import QFileIconProvider
from qtpy.QtCore import QFileInfo, QSize, Qt


class Icon(AbstractTool, QIcon):
    def __init__(self,
                 icon: Union[str,
                             QIcon,
                             QIconEngine,
                             QPixmap,
                             QImage,
                             AbstractIcons],
                 color: Union[QColor, Colors] = None,
                 size: Union[QSize, tuple, int] = None,
                 **kwargs):

        if isinstance(icon, AbstractIcons):
            icon = icon.value

        if color is not None or size is not None:
            icon = self.icon_color(icon, color, size)

        QIcon.__init__(self, icon)
        super().__init__(**kwargs)

    @classmethod
    def icon_color(cls,
                   icon,
                   color: Union[QColor, Colors],
                   size: Union[QSize, tuple, int] = None) -> QIcon:

        if isinstance(size, int):
            size = QSize(size, size)

        if isinstance(size, (tuple, list, set)):
            size = QSize(*size[:2])

        if not isinstance(icon, QIcon):
            icon = QIcon(icon)

        default_size = (icon.availableSizes()[0]
                        if icon.availableSizes().__len__()
                        else icon.actualSize(QSize(512, 512)))

        pixmap = icon.pixmap(size if size is not None else default_size)

        pixmap_painter = QPainter(pixmap)
        pixmap_painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceIn)
        pixmap_painter.setRenderHint(QPainter.RenderHint.Antialiasing 
                                     | QPainter.RenderHint.TextAntialiasing 
                                     | QPainter.RenderHint.SmoothPixmapTransform)

        if color is not None:
            color = color.value if isinstance(color, Colors) else color
            pixmap_painter.fillRect(pixmap.rect(), color)

        pixmap_painter.end()
        return QIcon(pixmap)

    @classmethod
    def icon_svg(cls,
                 svg: str,
                 color: Union[QColor, Colors] = None) -> QIcon:

        image = QImage()
        image.fill(Qt.GlobalColor.transparent)
        image.loadFromData(bytes(svg, "utf-8"))
        pixmap = QPixmap.fromImage(image, Qt.ImageConversionFlag.NoFormatConversion)

        if color is not None:
            color = color.value if isinstance(color, Colors) else color
            pixmap_painter = QPainter(pixmap)
            pixmap_painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceIn)
            pixmap_painter.fillRect(pixmap.rect(), color)
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