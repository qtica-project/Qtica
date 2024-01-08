#!/usr/bin/python3

from PySide6.QtWidgets import QGraphicsOpacityEffect, QHBoxLayout, QLabel, QWidget
from PySide6.QtCore import QEasingCurve, QPropertyAnimation, Qt
from PySide6.QtGui import QShowEvent
from ...core import AbstractDialog


class SilentDialog(AbstractDialog):
    def __init__(self,
                 *,
                 icon: QWidget,
                 text: QLabel,
                 enable_animation: bool = True,
                 auto_close: bool = True,
                 **kwargs):
        super().__init__(auto_close=auto_close, **kwargs)

        self._enable_animation = enable_animation

        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_AlwaysStackOnTop)
        self.setWindowOpacity(0.9)

        self.setStyleSheet("""
            QDialog, QWidget {
                padding: 6px;
                border-radius: 12px;
                background-color: #0d0d0d;
                color: #ffffff;
            }
        """)

        self._layout = QHBoxLayout(self)

        icon.setFixedSize(40, 40)

        self._layout.addWidget(icon)
        self._layout.addWidget(text)

        self.setLayout(self._layout)

    def showEvent(self, e: QShowEvent) -> None:
        if self._enable_animation:
            def _finished():
                opacityEffect.deleteLater()
                self.setGraphicsEffect(None)

            opacityEffect = QGraphicsOpacityEffect(self)
            self.setGraphicsEffect(opacityEffect)

            opacityAni = QPropertyAnimation(opacityEffect, b'opacity', self)
            opacityAni.setStartValue(0)
            opacityAni.setEndValue(1)
            opacityAni.setDuration(200)
            opacityAni.setEasingCurve(QEasingCurve.Type.InSine)
            opacityAni.finished.connect(_finished)
            opacityAni.start()

        return super().showEvent(e)