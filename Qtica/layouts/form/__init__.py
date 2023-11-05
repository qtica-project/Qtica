from PySide6.QtWidgets import QFormLayout, QWidget, QLayout, QLayoutItem
from typing import Union
from .item_wrapper import FormLayoutItemWrapper
from ...core.base import ObjectBase


class FormLayout(ObjectBase, QFormLayout):
    def __init__(self,
                 children: list[Union[QWidget, 
                                      QLayoutItem, 
                                      FormLayoutItemWrapper]],
                 **kwargs):
        QFormLayout.__init__(self)
        super().__init__(**kwargs)

        self._set_children(children)

    def _set_children(self, children: list[Union[QWidget, 
                                                 QLayoutItem, 
                                                 FormLayoutItemWrapper]]) -> None:
        if not children:
            return

        for child in children:
            if isinstance(child, QWidget):
                self.addWidget(child)

            elif isinstance(child, QLayoutItem):
                self.addItem(child)

            elif isinstance(child, FormLayoutItemWrapper):
                self.addRow(*child._yield_attr())

    @staticmethod
    def wrapper(
            label: Union[QWidget, str],
            field: Union[QWidget, QLayout]
        ) -> FormLayoutItemWrapper:
        return FormLayoutItemWrapper(
            label,
            field
        )

    # @staticmethod
    # def wrapper(
    #         row: Union[QWidget, QLayout]
    #     ) -> FormLayoutItemWrapper:
    #     return FormLayoutItemWrapper(row)