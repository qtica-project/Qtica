#!/usr/bin/python3

from PySide6.QtWidgets import QGridLayout, QApplication, QLabel, QDialog, QWidget
from PySide6.QtGui import QFont, QMouseEvent
from PySide6.QtCore import QTimer, Qt


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
                     font: QFont = None, 
                     timeout: int = 2000) -> None:
        self.text.setText(text)
        if font is not None:
            self.text.setFont(font)
        else:
            font = self.font()
            font.setBold(True)
            font.setPixelSize(50)
            self.text.setFont(font)

        QTimer.singleShot(0, self.start_show)
        QTimer.singleShot(timeout, self.start_closeing)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if self._close_on_mouse_press:
            self.start_closeing()
        return super().mousePressEvent()


class LargTextDialog:
    @classmethod
    def display(cls,
                *,
                text: str,
                font: QFont = None,
                timeout: int = 2000,
                auto_close: bool = False,
                parent: QWidget = None,
                **kwargs):

        if not parent:
            parent = QApplication.activeWindow()

        larg_text_dialog = _DisplayLargText(parent, auto_close, **kwargs)
        larg_text_dialog.display_text(text, font, timeout)
