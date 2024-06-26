from ..core import AbstractButton
from qtpy.QtWidgets import QPushButton, QToolButton, QCommandLinkButton, QRadioButton


class PushButton(AbstractButton, QPushButton):
    def __init__(self, *args, **kwargs):
        QPushButton.__init__(self, *args)
        super().__init__(**kwargs)


class ToolButton(AbstractButton, QToolButton):
    def __init__(self, *args, **kwargs):
        QToolButton.__init__(self, *args)
        super().__init__(**kwargs)


class CommandLinkButton(AbstractButton, QCommandLinkButton):
    def __init__(self, *args, **kwargs):
        QCommandLinkButton.__init__(self, *args)
        super().__init__(**kwargs)


class RadioButton(AbstractButton, QRadioButton):
    def __init__(self, *args, **kwargs):
        QRadioButton.__init__(self, *args)
        super().__init__(**kwargs)