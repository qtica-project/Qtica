#!/usr/bin/python3

from ._base import AbstractBase
from ._declarative import AbstractDec


class AbstractQObject(AbstractBase):
    pass


class QObjectDec(AbstractQObject, AbstractDec):
    pass