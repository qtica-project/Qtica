#!/usr/bin/python3
from sys import argv

from PySide6.QtGui import QFont, QMouseEvent
from PySide6.QtWidgets import QGridLayout, QApplication, QLabel, QDialog, QWidget
from PySide6.QtCore import QTimer, Qt

from ...enums.events import EventTypeVar
from ...enums.signals import SignalTypeVar
from ...core.base import WidgetBase


class _DisplayLargText(QDialog):
    def __init__(self,
                 parent = None,
                 close_on_mouse_press: bool = True) -> None:
        QDialog.__init__(self, parent)

        self._close_on_mouse_press = close_on_mouse_press

        self.setWindowFlags(
            self.windowFlags() 
            | Qt.WindowType.FramelessWindowHint)

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WidgetAttribute.WA_AlwaysStackOnTop, True)
        self.setWindowOpacity(0.9)

        self.setStyleSheet("""
        QDialog, QWidget{
            padding: 8px;
            border-radius: 8px;
            background-color: #0d0d0d;
            color: #ffffff;
        }
        """)

        self.form = QWidget(self)
        self.grid_layout1 = QGridLayout(self)
        self.grid_layout2 = QGridLayout(self.form)
        self.text = QLabel(self.form)

        self.font = QFont()
        self.font.setBold(True)

        self.text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text.setWordWrap(True)

        self.grid_layout2.addWidget(self.text, 0, 0, 0, 0, Qt.AlignmentFlag.AlignCenter)

        self.grid_layout1.addWidget(self.form)
        self.form.setLayout(self.grid_layout2)

        self.setLayout(self.grid_layout1)

    def start_closeing(self):
        self.close()

    def start_show(self):
        if self.isHidden():
            self.show()
            self.adjustSize()

    def display_text(self, 
                     text: str, 
                     font_size: int = 50, 
                     timeout: int = 2000) -> None:

        self.text.setText(text)
        self.font.setPixelSize(font_size)
        self.text.setFont(self.font)

        QTimer.singleShot(0, self.start_show)
        QTimer.singleShot(timeout, self.start_closeing)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if self._close_on_mouse_press:
            self.start_closeing()
        return


class LargTextDialog(WidgetBase, _DisplayLargText):
    def __init__(self,
                 uid: str = None, 
                 signals: SignalTypeVar = None, 
                 events: EventTypeVar = None,
                 close_on_mouse_press: bool = True,
                 **kwargs):
        _DisplayLargText.__init__(self, 
                                  close_on_mouse_press=close_on_mouse_press)
        super().__init__(uid, signals, events, **kwargs)

    def display(self, 
                text: str,
                font_size: int = 50,
                timeout: int = 2000) -> None:

        self.display_text(text, font_size, timeout)

    def run(self,
            text: str,
            font_size: int = 50,
            timeout: int = 2000) -> None:

        self.display_text(text, font_size, timeout)


def main():
    app = QApplication(argv)
    window = _DisplayLargText()
    window.display_text("Test Display Larg Text is Ok!")
    window.show()
    exit(app.exec())

if __name__ == "__main__":
    main()
