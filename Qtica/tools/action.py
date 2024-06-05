#!/usr/bin/python3

from typing import Union, Callable
from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import QAction, QIcon, QPixmap
from ..core import AbstractQObject, QObjectDec


class LinePasswordAction(QObjectDec, QAction):
    def __init__(self,
                 child: QLineEdit,
                 show_icon: Union[QIcon, QPixmap] = None,
                 hide_icon: Union[QIcon, QPixmap] = None,
                 position: QLineEdit.ActionPosition = QLineEdit.ActionPosition.TrailingPosition,
                 **kwargs) -> QLineEdit:
        super().__init__(**kwargs)

        self._child = child
        self._show_icon = show_icon
        self._hide_icon = hide_icon
        self._position = position

        self.triggered.connect(lambda: self._toggle_password_echo_mode_icon())
        self._child.textChanged.connect(lambda: self._update_password_mode())
        self._child.addAction(self, self._position)

        self._toggle_icon()
        self._update_password_mode()

        return self._child

    def _toggle_password_echo_mode_icon(self):
        self._toggle_echo_mode()
        self._toggle_icon()

    def _toggle_echo_mode(self):
        self._child.setEchoMode(
            QLineEdit.EchoMode.Normal 
            if self._child.echoMode() == QLineEdit.EchoMode.Password
            else QLineEdit.EchoMode.Password
        )

    def _toggle_icon(self):
        self.setIcon(
            self._show_icon 
            if self._child.echoMode() == QLineEdit.EchoMode.Password 
            else self._hide_icon
        )

    def _update_password_mode(self):
        self.setVisible(bool(self._child.text()))

    def set_position(self, position):
        self._position = position

    def toggle_show_icon(self):
        self.setIcon(self._show_icon)

    def toggle_hide_icon(self):
        self.setIcon(self._hide_icon)


class MenuAction(AbstractQObject, QAction):
    def __init__(self,
                 *,
                 text: str = None,
                 icon: Union[QIcon, QPixmap] = None,
                 callback: Callable = None,
                 **kwargs):
        QAction.__init__(self)

        if text is not None:
            self.setText(text)

        if icon is not None:
            self.setIcon(icon)

        if callback is not None:
            self.triggered.connect(callback)

        super().__init__(**kwargs)