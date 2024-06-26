from typing import Union
from ..core import AbstractQObject, AbstractTool

from qtpy.QtCore import QByteArray, QXmlStreamReader
from qtpy.QtSvg import QSvgRenderer, QSvgGenerator


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