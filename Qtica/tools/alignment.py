from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from ..core.base import BehaviorDeclarative


class Alignment(BehaviorDeclarative):
    def __init__(self,
                 child: QWidget,
                 alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignCenter):

        if not hasattr(child, "setAlignment"):
            raise ValueError("invalid child widget!")
        
        child.setAlignment(alignment)
        return child