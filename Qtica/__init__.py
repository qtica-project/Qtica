# Qtica
__version__ = "0.2.1"
__version_info__ = (0, 2, 1, "", "")

# Python
__minimum_python_version__ = (3, 7)
__maximum_python_version__ = (3, 11)

# PySide6
__pyside_version__ = "6.5.0"

# base classes
from .core import (
    AbstractBase, 
    QObjectBase,
    WidgetBase, 
    NoneCheck,

    # declarative
    BehaviorDeclarative, 
    WidgetDeclarative, 
    QObjectDeclarative,
    DuplicateKeyError,
    TrackingDeclarative,

    # platforms
    AndroidInit,
    IOSInit,
    LinuxInit,
    MacOSInit,
    WindowsInit,

    Api,
    QStyleSheet,
    AbstractTool,
    ToolBase,
    AbstractIcon,
    IconBase,
    AbstractPainter,
    PainterBase
)