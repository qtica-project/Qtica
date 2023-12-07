from PySide6.QtWidgets import QSizePolicy, QWidget
from ..core import ToolBase


class SizePolicy(ToolBase, QSizePolicy):
    def __init__(self,
                 *,
                 child: QWidget,
                 horizontal: QSizePolicy.Policy = None,
                 vertical: QSizePolicy.Policy = None,
                 stretch: tuple[int, int] = None,
                 type: QSizePolicy.ControlType = None,
                 **kwargs) -> QWidget:
        QSizePolicy.__init__(self)
        super().__init__(**kwargs)

        if type is not None:
            self.setControlType(type)

        if horizontal is not None:
            self.setHorizontalPolicy(horizontal)

        if vertical is not None:
            self.setVerticalPolicy(vertical)

        self.setHorizontalStretch(stretch[0] if stretch is not None else 0)
        self.setVerticalStretch(stretch[-1] if stretch is not None else 0)

        self.setHeightForWidth(child.sizePolicy().hasHeightForWidth())
        self.setWidthForHeight(child.sizePolicy().hasWidthForHeight())
        # sizePolicy.setRetainSizeWhenHidden(True)

        child.setSizePolicy(self)

        return child