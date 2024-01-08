from typing import Union
from PySide6.QtWidgets import QFormLayout, QWidget, QLayoutItem
from ..tools.wrappers.form_layout import FormLayoutWrapper
from ..tools.alignment import Alignment
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

                if isinstance(child.child, QWidget):
                    _func = self.addWidget
                elif isinstance(child.child, QLayoutItem):
                    _func = self.addItem

                _func(_widget)
                self.setAlignment(_widget, child.alignment)

            elif isinstance(child, FormLayoutWrapper):
                if child.row is not None:
                    self.addRow(child.row)
                else:
                    self.addRow(child.label, child.field)

            elif isinstance(child, QLayoutItem):
                self.addItem(child)

            elif isinstance(child, QWidget):
                self.addWidget(child)