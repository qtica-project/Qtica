from typing import Union
from PySide6.QtWidgets import QVBoxLayout, QWidget, QLayout
from ..tools.wrappers.layout import LayoutWrapper
from ..utils.alignment import Alignment
from .vh_layout import VHLayout



class VLayout(VHLayout, QVBoxLayout):
    def __init__(self,
                 *,
                 children: list[Union[QWidget, 
                                      QLayout, 
                                      LayoutWrapper,
                                      Alignment]] = None,
                 **kwargs):
        QVBoxLayout.__init__(self)
        super().__init__(children=children, **kwargs)


class RowLayout(VLayout):
    ...