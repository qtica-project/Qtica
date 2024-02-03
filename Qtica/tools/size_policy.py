#!/usr/bin/python3

from typing import Union
from PySide6.QtWidgets import QSizePolicy, QWidget
from ..core import AbstractTool


class SizePolicy(AbstractTool, QSizePolicy):
    def __init__(self,
                 horizontal: QSizePolicy.Policy = None,
                 vertical: QSizePolicy.Policy = None,
                 control_type: QSizePolicy.ControlType = None,
                 stretch: Union[tuple[int, int], int] = None,
                 **kwargs) -> QWidget:
        QSizePolicy.__init__(self)

        if control_type is not None:
            self.setControlType(control_type)

        if horizontal is not None:
            self.setHorizontalPolicy(horizontal)

        if vertical is not None:
            self.setVerticalPolicy(vertical)

        if stretch is not None:
            h, v = (stretch,) * 2 if isinstance(stretch, int) else stretch
            self.setHorizontalStretch(h)
            self.setVerticalStretch(v)

        super().__init__(**kwargs)