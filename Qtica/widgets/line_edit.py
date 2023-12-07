from typing import Union
from PySide6.QtGui import QAction, QIcon, QPixmap
from PySide6.QtWidgets import QLineEdit
from ..core import WidgetBase


class LineEdit(WidgetBase, QLineEdit):
    def __init__(self,
                 *,
                 password_mode: bool = False,
                 password_show_icon: Union[QIcon, QPixmap] = None,
                 password_hide_icon: Union[QIcon, QPixmap] = None,
                 **kwargs):
        QLineEdit.__init__(self)
        super().__init__(**kwargs)

        self._password_show_icon = password_show_icon
        self._password_hide_icon = password_hide_icon

        if password_mode:
            self._set_password_mode()

    def _toggle_password_echo_mode_icon(self):
        if self.echoMode() == QLineEdit.EchoMode.Password:
            self.setEchoMode(QLineEdit.EchoMode.Normal)
            # set eye close
            self._password_echo_mode_action.setIcon(self._password_hide_icon)
        else:
            self.setEchoMode(QLineEdit.EchoMode.Password)
            # set eye open
            self._password_echo_mode_action.setIcon(self._password_show_icon)

    def _set_password_mode(self):
        self.setEchoMode(QLineEdit.EchoMode.Password)
        self._password_echo_mode_action = QAction(icon=self._password_show_icon)
        self._password_echo_mode_action.triggered.connect(self._toggle_password_echo_mode_icon)
        self.addAction(self._password_echo_mode_action, 
                       QLineEdit.ActionPosition.TrailingPosition)

    def _set_normal_mode(self):
        self.setEchoMode(QLineEdit.EchoMode.Normal)
        self._password_echo_mode_action.deleteLater()

    def toggle_password_mode(self, enable: bool = False):
        if enable:
            return self._set_password_mode()
        return self._set_normal_mode