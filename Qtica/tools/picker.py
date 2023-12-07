from typing import Callable
from pynput import mouse
from PIL import ImageGrab
from PySide6.QtCore import Signal, QObject
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QApplication
from .icon import Icon



class ColorPicker(QObject):
    color_changed = Signal(QColor)

    def __init__(self,
                 *,
                 mouse_icon: Icon = None,
                 color_changed: Callable = None):
        super().__init__()

        self._mouse_icon = mouse_icon
        self._is_running = False
        self._on_color_changed = color_changed
        self._mouse_listener = mouse.Listener(on_click = self._on_click)
        self._mouse_listener.start()

        if color_changed is not None:
            self.color_changed.connect(color_changed)

    def start(self):
        self._is_running = True
        if self._mouse_icon is not None:
            QApplication.setOverrideCursor(
                self._mouse_icon.pixmap(32, 32)
            )

    def close(self) -> None:
        self._is_running = False
        if self._mouse_icon is not None:
            QApplication.restoreOverrideCursor()
        self._mouse_listener.stop()

    def _get_color(self, x: int, y: int):
        im = ImageGrab.grab(bbox=(x, y, x + 1, y + 1))
        rgbim = im.convert('RGB')
        r,g,b,*_ = rgbim.getpixel((0,0))
        return r, g, b

    def _on_click(self, x, y, button, pressed):
        if not self._is_running:
            return

        if pressed and button == mouse.Button.left:
            self.color_changed.emit(QColor(*self._get_color(x, y)))
            self._is_running = False
            QApplication.restoreOverrideCursor()