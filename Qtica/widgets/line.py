from ..core import AbstractWidget
from qtpy.QtWidgets import QFrame


class Line(AbstractWidget, QFrame):
    def __init__(self, **kwargs):
        QFrame.__init__(self)
        self.setFrameShadow(QFrame.Shadow.Sunken)
        self.setFrameShape(QFrame.Shape.NoFrame)
        super().__init__(**kwargs)


class HLine(Line):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.setFrameShape(QFrame.Shape.HLine)


class VLine(Line):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.setFrameShape(QFrame.Shape.VLine)