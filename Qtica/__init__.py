# Qtica
__version__ = "0.1.4"
__version_info__ = (0, 1, 4, "", "")

# Python
__minimum_python_version__ = (3, 7)
__maximum_python_version__ = (3, 11)

# PySide6
__pyside_version__ = "6.5.0"

# base classes
from .core import (
    AbstractBase, 
    ObjectBase, 
    WidgetBase, 
    Return,
    NoneCheck,

    # declarative
    BehaviorDeclarative, 
    WidgetDeclarative, 
    ObjectDeclarative,
    DuplicateKeyError,
    TrackingDeclarative,

    # platforms
    AndroidInit,
    IOSInit,
    LinuxInit,
    MacOSInit,
    WindowsInit,

    Api,
    QStyleSheet
)