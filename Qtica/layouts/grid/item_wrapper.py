from PySide6.QtWidgets import QWidget, QLayout, QLayoutItem
from PySide6.QtCore import Qt
from typing import Union


class GridAlignment:
    def __init__(self, 
                 child: QWidget,
                 alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignCenter) -> None:

        self._child = child
        self._alignment = alignment


class GridLayoutItemWrapper:
    def __init__(
        self,
        *,
        child: Union[QWidget, QLayout, QLayoutItem],
        row: int = None,
        column: int = None,
        row_span: int = None,
        column_span: int = None,
        alignment: Qt.AlignmentFlag = None
    ) -> None:

        if not child:
            raise AttributeError("invalid child widget!")

        self._attrs = {}

        for k, v in zip(("arg__1", "row", "column", "rowSpan", "columnSpan", "alignment"), 
                        (child, row, column, row_span, column_span, alignment)):
            if v is not None:
                self._attrs[k] = v

    @property
    def child(self) -> QWidget:
        return self.attrs.get("arg__1")

    @property
    def attrs(self) -> dict:
        return self._attrs