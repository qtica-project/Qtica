from typing import Union
from PySide6.QtWidgets import QFormLayout, QWidget, QLayoutItem
from ..tools.wrappers.form_layout import FormLayoutWrapper
from ..utils.alignment import Alignment
from ..core import AbstractQObject


class FormLayout(AbstractQObject, QFormLayout):
    def __init__(self,
                 *,
                 children: list[Union[QWidget, 
                                      QLayoutItem, 
                                      FormLayoutWrapper,
                                      Alignment]],
                 **kwargs):
        QFormLayout.__init__(self)
        super().__init__(**kwargs)

        if not children:
            return

        for child in children:
            if isinstance(child, Alignment):
                _widget = child.child

                if isinstance(_widget, QWidget):
                    self.addWidget(_widget)
                elif isinstance(_widget, QLayoutItem):
                    self.addItem(_widget)

                self.setAlignment(_widget, child.alignment)

            elif isinstance(child, FormLayoutWrapper):
                self.addRow(*([child.row] if child.row is not None else [child.label, child.field]))

            elif isinstance(child, QLayoutItem):
                self.addItem(child)

            elif isinstance(child, QWidget):
                self.addWidget(child)