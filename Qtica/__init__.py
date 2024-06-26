# Qtica
__version__ = "0.5.1"
__version_info__ = (0, 5, 1, "", "")

# Python
__minimum_python_version__ = (3, 10)
__maximum_python_version__ = (3, 12)

# PySide6
__pyside_version__ = "6.7.2"


from PySide6.QtCore import (
    Qt, 
    Property, 
    Signal, 
    Slot, 
    SignalInstance, 
    ClassInfo, 
    MetaFunction, 
    MetaSignal, 
    PyClassProperty
)
from .core import *