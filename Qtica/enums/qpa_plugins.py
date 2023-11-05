from enum import Enum


class QPA_Platforms(Enum):
    android: str = "android"
    cocoa: str = "cocoa"
    directfb: str = "directfb"
    eglfs: str = "eglfs"
    ios: str = "ios"
    kms: str = "kms"
    linuxfb: str = "linuxfb"
    minimal: str = "minimal"
    minimalegl: str = "minimalegl"
    offscreen: str = "offscreen"
    openwfd: str = "openwfd"
    qnx: str = "qnx"
    windows: str = "windows"
    wayland: str = "wayland"
    xcb: str = "xcb"