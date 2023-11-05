#!/usr/bin/python3

from sys import argv

from PySide6.QtGui import QFont, QIcon, QPixmap
from PySide6.QtWidgets import QGridLayout, QWidget, QApplication, QLabel, QDialog, QWidget
from PySide6.QtCore import QSize, QTimer, Qt

from ...enums.events import EventTypeVar
from ...enums.signals import SignalTypeVar
from ...core.base import WidgetBase


class _SilentTextDialog(QDialog):
    def __init__(self, parent = None, close_on_mouse_press: bool = True) -> None:
        QDialog.__init__(self, parent)

        self._close_on_mouse_press = close_on_mouse_press

        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WidgetAttribute.WA_AlwaysStackOnTop, True)
        self.setWindowOpacity(0.9)

        self.setStyleSheet("""
        QDialog, QWidget {
            padding: 6px;
            border-radius: 12px;
            background-color: #0d0d0d;
            color: #ffffff;
        }
        """)

        ## Create Qt Widgetes
        self.form = QWidget(self)
        self.form.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)

        self.grid_layout1 = QGridLayout(self)
        self.grid_layout2 = QGridLayout(self.form)

        self.icon = QLabel(self.form)
        self.text = QLabel(self.form)

        font = QFont()
        font.setBold(True)
        font.setPixelSize(16)

        self.text.setFont(font)
        self.text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # self.text.setWordWrap(True)

        self.grid_layout2.addWidget(self.icon, 0, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)
        self.grid_layout2.addWidget(self.text, 0, 1, 1, 1, Qt.AlignmentFlag.AlignCenter)

        self.form.setLayout(self.grid_layout2)
        self.grid_layout1.addWidget(self.form)
        self.setLayout(self.grid_layout1)

    def start_closeing(self):
        self.close()

    def start_show(self):
        if self.isHidden():
            self.show()
            self.adjustSize()

    def display_text(self, 
                     icon: QIcon | QPixmap,
                     text: str, 
                     timeout: int = 1500, 
                     icon_size: QSize = None):

        if isinstance(icon, QIcon):
            self.icon.setPixmap(icon.pixmap(icon_size 
                                            if icon_size is not None 
                                            else QSize(32, 32)))
        else:
            self.icon.setPixmap(icon)

        self.text.setText(str(text))

        QTimer.singleShot(0, self.start_show)
        QTimer.singleShot(timeout, self.start_closeing)

    def mousePressEvent(self, event) -> None:
        if self._close_on_mouse_press:
            self.start_closeing()


class SilentTextDialog(WidgetBase, _SilentTextDialog):
    def __init__(self, 
                 uid: str = None, 
                 signals: SignalTypeVar = None, 
                 events: EventTypeVar = None, 
                 close_on_mouse_press: bool = True,
                 **kwargs):
        _SilentTextDialog.__init__(self, 
                                   close_on_mouse_press=close_on_mouse_press)
        super().__init__(uid, signals, events, **kwargs)

    def display(self, 
                icon: QIcon | QPixmap,
                text: str,
                timeout: int = 1500,
                icon_size: QSize = None):
        self.display_text(icon, text, timeout, icon_size)

    def run(self, 
            icon: QIcon | QPixmap,
            text: str, 
            timeout: int = 1500,
            icon_size: QSize = None):
        self.display_text(icon, text, timeout, icon_size)


def main():
    app = QApplication(argv)
    window = _SilentTextDialog()
    window.display_text(QIcon.fromTheme("firefox"), "Test Display Silent Text is Ok! slkdfjskjfkls jdflksjdflksdjf")
    window.show()
    exit(app.exec())

if __name__ == "__main__":
    main()
