from PySide6.QtWidgets import QWidget, QLayout
from ..core import WidgetBase


class Widget(WidgetBase, QWidget):
    def __init__(self,
                 *,
                 child: QWidget | QLayout = None,
                 **kwargs):
        QWidget.__init__(self)
        super().__init__(**kwargs)

        self._set_child(child)

    def _set_child(self, child: QWidget | QLayout):
        if child is not None:
            if isinstance(child, QWidget):
                child.setParent(self)

            elif isinstance(child, QLayout):
                child.setProperty("parent", self)
                self.setLayout(child)
            else:
                raise ValueError("the 'child' argument must be one of the QWidget or QLayout instance.")