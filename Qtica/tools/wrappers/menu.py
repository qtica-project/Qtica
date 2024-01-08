
from typing import Union
from PySide6.QtGui import QIcon, QPixmap
from ...core import AbstractDec


class MenuSeparatorWrapper:
    ...


class MenuSectionWrapper(AbstractDec):
    def __init__(self,
                 text: str,
                 icon: Union[QIcon, QPixmap] = None):

        return (text, icon) if icon is not None else (text,)
