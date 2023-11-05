from PySide6.QtWidgets import QSizePolicy, QWidget
from ..core.base import BehaviorDeclarative


class SizePolicy(BehaviorDeclarative):
    def __init__(self, 
                 child: QWidget, 
                 horizontal: QSizePolicy.Policy = None,
                 vertical: QSizePolicy.Policy = None,
                 stretch: tuple[int, int] = None,
                 type: QSizePolicy.ControlType = None) -> QWidget:

        self._size_policy = QSizePolicy()

        if type is not None:
            self._size_policy.setControlType(type)

        if horizontal is not None:
            self._size_policy.setHorizontalPolicy(horizontal)

        if vertical is not None:
            self._size_policy.setVerticalPolicy(vertical)

        self._size_policy.setHorizontalStretch(stretch[0] if stretch is not None else 0)
        self._size_policy.setVerticalStretch(stretch[-1] if stretch is not None else 0)

        self._size_policy.setHeightForWidth(child.sizePolicy().hasHeightForWidth())
        self._size_policy.setWidthForHeight(child.sizePolicy().hasWidthForHeight())

        child.setSizePolicy(self._size_policy)

        # sizePolicy.setRetainSizeWhenHidden(True)

        return child

    def build(self):
        self._size_policy