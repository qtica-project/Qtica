from PySide6.QtWidgets import QFrame
from ..core import WidgetBase


class _Line(WidgetBase, QFrame):
    def __init__(self,
                 shadow: QFrame.Shadow = QFrame.Shadow.Sunken,
                 **kwargs):
        QFrame.__init__(self)
        super().__init__(**kwargs)

        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setFrameShadow(shadow)


class HLine(_Line):
    def __init__(self,
                 *,
                 shadow: QFrame.Shadow = QFrame.Shadow.Sunken,
                 **kwargs):
        super().__init__(shadow=shadow, **kwargs)

        self.setFrameShape(QFrame.Shape.HLine)


class VLine(_Line):
    def __init__(self, 
                 *,
                 shadow: QFrame.Shadow = QFrame.Shadow.Sunken,
                 **kwargs):
        super().__init__(shadow=shadow,**kwargs)

        self.setFrameShape(QFrame.Shape.VLine)