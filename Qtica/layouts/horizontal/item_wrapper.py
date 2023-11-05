from PySide6.QtWidgets import QWidget, QLayout
from PySide6.QtCore import Qt


class HLayoutItemWrapper:
    def __init__(self, 
                 child: QWidget | QLayout, 
                 stretch: int = None,
                 alignment: Qt.AlignmentFlag = None) -> None:

        if not child:
            raise AttributeError("child should be QWidget | QLayout")

        self.child = child
        self.stretch = stretch
        self.alignment = alignment

    def _yield_attr(self):
        for attr in (
            self.child,
            self.stretch,
            self.alignment
        ):
            if attr is not None:
                yield attr
