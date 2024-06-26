from typing import Union
from ...core import AbstractDec

from qtpy.QtGui import QIcon, QPixmap


class MenuSeparatorWrapper:
    ...


class MenuSectionWrapper(AbstractDec):
    def __init__(self,
                 text: str,
                 icon: Union[QIcon, QPixmap] = None):

        return (text, icon) if icon is not None else (text,)
