from typing import Optional, Union
from qtpy.QtWidgets import QWidget, QLayout


class FormLayoutWrapper:
    def __init__(
        self,
        row: Optional[Union[QWidget, QLayout]] = None,
        *,
        label: Union[QWidget, str],
        field: Union[QWidget, QLayout]
    ) -> None:

        self.label = label
        self.field = field
        self.row = row