from typing import Union
from PySide6.QtCore import QByteArray, QXmlStreamReader
from PySide6.QtSvg import QSvgRenderer, QSvgGenerator
from ..core import AbstractQObject, AbstractTool


class SvgRenderer(AbstractQObject, QSvgRenderer):
    def __init__(self, file: Union[QXmlStreamReader, QByteArray, bytes, str], **kwargs):
        QSvgRenderer.__init__(self, file)
        super().__init__(**kwargs)


class SvgGenerator(QSvgGenerator, AbstractTool):
    def __init__(self, version: QSvgGenerator.SvgVersion = None, **kwargs):
        if version is not None:
            QSvgGenerator.__init__(self, version)
        else:
            QSvgGenerator.__init__(self)

        super().__init__(**kwargs)