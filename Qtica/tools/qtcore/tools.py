#!/usr/bin/python3

from PySide6 import QtCore
from ...core import AbstractTool


class BitArray(AbstractTool, QtCore.QBitArray):
    def __init__(self, *args, **kwargs):
        QtCore.QBitArray.__init__(self, *args)
        super().__init__(**kwargs)


class ByteArray(AbstractTool, QtCore.QByteArray):
    def __init__(self, *args, **kwargs):
        QtCore.QByteArray.__init__(self, *args)
        super().__init__(**kwargs)


class ByteArrayMatcher(AbstractTool, QtCore.QByteArrayMatcher):
    def __init__(self, *args, **kwargs):
        QtCore.QByteArrayMatcher.__init__(self, *args)
        super().__init__(**kwargs)


class Collator(AbstractTool, QtCore.QCollator):
    def __init__(self, *args, **kwargs):
        QtCore.QCollator.__init__(self, *args)
        super().__init__(**kwargs)


class DataStream(AbstractTool, QtCore.QDataStream):
    def __init__(self, *args, **kwargs):
        QtCore.QDataStream.__init__(self, *args)
        super().__init__(**kwargs)


class Date(AbstractTool, QtCore.QDate):
    def __init__(self, *args, **kwargs):
        QtCore.QDate.__init__(self, *args)
        super().__init__(**kwargs)


class DateTime(AbstractTool, QtCore.QDateTime):
    def __init__(self, *args, **kwargs):
        QtCore.QDateTime.__init__(self, *args)
        super().__init__(**kwargs)


class DeadlineTimer(AbstractTool, QtCore.QDeadlineTimer):
    def __init__(self, *args, **kwargs):
        QtCore.QDeadlineTimer.__init__(self, *args)
        super().__init__(**kwargs)


class Dir(AbstractTool, QtCore.QDir):
    def __init__(self, *args, **kwargs):
        QtCore.QDir.__init__(self, *args)
        super().__init__(**kwargs)


class EasingCurve(AbstractTool, QtCore.QEasingCurve):
    def __init__(self, *args, **kwargs):
        QtCore.QEasingCurve.__init__(self, *args)
        super().__init__(**kwargs)


class FileInfo(AbstractTool, QtCore.QFileInfo):
    def __init__(self, *args, **kwargs):
        QtCore.QFileInfo.__init__(self, *args)
        super().__init__(**kwargs)


class FutureInterfaceBase(AbstractTool, QtCore.QFutureInterfaceBase):
    def __init__(self, *args, **kwargs):
        QtCore.QFutureInterfaceBase.__init__(self, *args)
        super().__init__(**kwargs)


class JsonDocument(AbstractTool, QtCore.QJsonDocument):
    def __init__(self, *args, **kwargs):
        QtCore.QJsonDocument.__init__(self, *args)
        super().__init__(**kwargs)


class Line(AbstractTool, QtCore.QLine):
    def __init__(self, *args, **kwargs):
        QtCore.QLine.__init__(self, *args)
        super().__init__(**kwargs)


class LineF(AbstractTool, QtCore.QLineF):
    def __init__(self, *args, **kwargs):
        QtCore.QLineF.__init__(self, *args)
        super().__init__(**kwargs)


class Locale(AbstractTool, QtCore.QLocale):
    def __init__(self, *args, **kwargs):
        QtCore.QLocale.__init__(self, *args)
        super().__init__(**kwargs)


class LockFile(AbstractTool, QtCore.QLockFile):
    def __init__(self, *args, **kwargs):
        QtCore.QLockFile.__init__(self, *args)
        super().__init__(**kwargs)


class LoggingCategory(AbstractTool, QtCore.QLoggingCategory):
    def __init__(self, *args, **kwargs):
        QtCore.QLoggingCategory.__init__(self, *args)
        super().__init__(**kwargs)


class Margins(AbstractTool, QtCore.QMargins):
    def __init__(self, *args, **kwargs):
        QtCore.QMargins.__init__(self, *args)
        super().__init__(**kwargs)


class MarginsF(AbstractTool, QtCore.QMarginsF):
    def __init__(self, *args, **kwargs):
        QtCore.QMarginsF.__init__(self, *args)
        super().__init__(**kwargs)


class NativeIpcKey(AbstractTool, QtCore.QNativeIpcKey):
    def __init__(self, *args, **kwargs):
        QtCore.QNativeIpcKey.__init__(self, *args)
        super().__init__(**kwargs)


class Point(AbstractTool, QtCore.QPoint):
    def __init__(self, *args, **kwargs):
        QtCore.QPoint.__init__(self, *args)
        super().__init__(**kwargs)


class PointF(AbstractTool, QtCore.QPointF):
    def __init__(self, *args, **kwargs):
        QtCore.QPointF.__init__(self, *args)
        super().__init__(**kwargs)


class Rect(AbstractTool, QtCore.QRect):
    def __init__(self, *args, **kwargs):
        QtCore.QRect.__init__(self, *args)
        super().__init__(**kwargs)


class RectF(AbstractTool, QtCore.QRectF):
    def __init__(self, *args, **kwargs):
        QtCore.QRectF.__init__(self, *args)
        super().__init__(**kwargs)


class RegularExpression(AbstractTool, QtCore.QRegularExpression):
    def __init__(self, *args, **kwargs):
        QtCore.QRegularExpression.__init__(self, *args)
        super().__init__(**kwargs)


class Size(AbstractTool, QtCore.QSize):
    def __init__(self, *args, **kwargs):
        QtCore.QSize.__init__(self, *args)
        super().__init__(**kwargs)


class SizeF(AbstractTool, QtCore.QSizeF):
    def __init__(self, *args, **kwargs):
        QtCore.QSizeF.__init__(self, *args)
        super().__init__(**kwargs)


class SystemSemaphore(AbstractTool, QtCore.QSystemSemaphore):
    def __init__(self, *args, **kwargs):
        QtCore.QSystemSemaphore.__init__(self, *args)
        super().__init__(**kwargs)


class TextStream(AbstractTool, QtCore.QTextStream):
    def __init__(self, *args, **kwargs):
        QtCore.QTextStream.__init__(self, *args)
        super().__init__(**kwargs)


class Time(AbstractTool, QtCore.QTime):
    def __init__(self, *args, **kwargs):
        QtCore.QTime.__init__(self, *args)
        super().__init__(**kwargs)


class Url(AbstractTool, QtCore.QUrl):
    def __init__(self, *args, **kwargs):
        QtCore.QUrl.__init__(self, *args)
        super().__init__(**kwargs)


class UrlQuery(AbstractTool, QtCore.QUrlQuery):
    def __init__(self, *args, **kwargs):
        QtCore.QUrlQuery.__init__(self, *args)
        super().__init__(**kwargs)


class XmlStreamReader(AbstractTool, QtCore.QXmlStreamReader):
    def __init__(self, *args, **kwargs):
        QtCore.QXmlStreamReader.__init__(self, *args)
        super().__init__(**kwargs)


class XmlStreamWriter(AbstractTool, QtCore.QXmlStreamWriter):
    def __init__(self, *args, **kwargs):
        QtCore.QXmlStreamWriter.__init__(self, *args)
        super().__init__(**kwargs)
