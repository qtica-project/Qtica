from typing import Union
from PySide6.QtWidgets import QHBoxLayout, QWidget, QLayout
from ..tools.wrappers.layout import LayoutWrapper
from ..utils.alignment import Alignment
from .vh_layout import VHLayout



class HLayout(VHLayout, QHBoxLayout):
    def __init__(self,
                 *,
                 children: list[Union[QWidget, 
                                      QLayout, 
                                      LayoutWrapper,
                                      Alignment]] = None,
                 **kwargs):
        QHBoxLayout.__init__(self)
        super().__init__(children=children, **kwargs)


class ColumnLayout(HLayout):
    ...