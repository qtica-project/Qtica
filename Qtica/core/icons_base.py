#!/usr/bin/python3

from enum import Enum
from PySide6.QtGui import QIcon, QIconEngine, QImage, QPixmap


class AbstractIcon(Enum):
    '''
    class Icons(AbstractIcon):
        icon_name: Union[str, QIcon, QIconEngine, QPixmap, QImage]
    '''

    def __new__(cls, value):
        obj = object.__new__(cls)
        if not cls._check_type(value):
            raise ValueError("invalid enum value, " \
                "supported value str | QIcon | QIconEngine | QPixmap | QImage")
        obj._value_ = value
        return obj

    @classmethod
    def _check_type(cls, value):
        for _type in (
            str,
            QIcon,
            QIconEngine,
            QPixmap,
            QImage
        ):
            if (_check := ((type(value) == _type) 
                           or isinstance(value, _type))):
                return _check
        return _check

    @property
    def icon(self) -> QIcon:
        return QIcon(self.value)

    @property
    def pixmap(self) -> QPixmap:
        if not isinstance(self.value, (QPixmap, QImage, str)):
            raise ValueError("invalid value, " \
                "supported value QPixmap | QImage | str")
        return QPixmap(self.value)

    @property
    def image(self) -> QImage:
        if not isinstance(self.value, (QImage, str)):
            raise ValueError("invalid value, \
                supported value QImage | str")
        return QPixmap(self.value)


class IconBase(AbstractIcon):
    pass