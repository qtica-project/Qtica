from PySide6.QtWidgets import QWidget, QLayout
from typing import Union


class FormLayoutItemWrapper:
    def __init__(
        self,
        label: Union[QWidget, str],
        field: Union[QWidget, QLayout]
    ) -> None:

        if not label:
            raise AttributeError("label should be QWidget | str")

        if not field:
            raise AttributeError("field should be QWidget | QLayout")

        self.label = label
        self.field = field

    # def __init__(self, row: Union[QWidget, QLayout]):
    #     if not row:
    #         raise AttributeError("row should be QWidget | QLayout")
    #     self.row = row

    def _yield_attr(self):
        # if hasattr(self, "row"):
        #     yield self.row
        # else:
            for attr in (
                self.label,
                self.field
            ):
                if attr is not None:
                    yield attr