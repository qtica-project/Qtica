from enum import Enum, auto


class ClipboardDataTypes(Enum):
    mimedata = auto()
    pixmap = auto()
    image = auto()
    text = auto()