from typing import Union
from ..core import AbstractTool

from qtpy.QtWidgets import QSizePolicy, QWidget


class SizePolicy(AbstractTool, QSizePolicy):
    def __init__(self,
                 hsizetype: QSizePolicy.Policy = None,
                 vsizetype: QSizePolicy.Policy = None,
                 control_type: QSizePolicy.ControlType = None,
                 stretch: Union[tuple[int, int], int] = None,
                 **kwargs) -> QWidget:
        QSizePolicy.__init__(self)

        if control_type is not None:
            self.setControlType(control_type)

        if hsizetype is not None:
            self.setHorizontalPolicy(hsizetype)

        if vsizetype is not None:
            self.setVerticalPolicy(vsizetype)

        if stretch is not None:
            h, v = (stretch,) * 2 if isinstance(stretch, int) else stretch
            self.setHorizontalStretch(h)
            self.setVerticalStretch(v)

        super().__init__(**kwargs)