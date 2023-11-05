from typing import Union
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGridLayout, QWidget, QLayout, QLayoutItem
from .item_wrapper import GridLayoutItemWrapper, GridAlignment
from ...core.base import ObjectBase


class GridLayout(ObjectBase, QGridLayout):
    def __init__(self,
                 children: list[Union[QWidget, QLayoutItem, GridLayoutItemWrapper]] = None,
                 **kwargs):
        QGridLayout.__init__(self)
        super().__init__(**kwargs)

        self._set_children(children)

    def _set_children(self, children: list[Union[QWidget, 
                                                 GridLayoutItemWrapper]]) -> None:
        if not children:
            return

        for child in children:
            if isinstance(child, QWidget):
                self.addWidget(child)

            elif isinstance(child, QLayoutItem):
                self.addItem(child)

            elif isinstance(child, GridAlignment):
                self.addWidget(child._child)
                self.setAlignment(child._child, 
                                  child._alignment)

            elif isinstance(child, GridLayoutItemWrapper):
                child.attrs.update({
                    "row":     child.attrs.get("row", self.rowCount()),
                    "column":  child.attrs.get("column", self.columnCount()),
                    "alignment": child.attrs.get("alignment", Qt.AlignmentFlag.AlignCenter)
                })

                values = child.attrs.values()

                if isinstance(child.child, QWidget):
                    self.addWidget(*values)

                elif isinstance(child.child, QLayoutItem):
                    self.addItem(*values)

                elif isinstance(child.child, QLayout):
                    self.addLayout(*values)

    @staticmethod
    def wrapper(
            child: Union[QWidget, QLayout, QLayoutItem],
            row: int = None,
            column: int = None,
            row_span: int = None,
            column_span: int = None,
            alignment: Qt.AlignmentFlag = None
        ) -> GridLayoutItemWrapper:
        return GridLayoutItemWrapper(
            child,
            row,
            column,
            row_span,
            column_span,
            alignment
        )