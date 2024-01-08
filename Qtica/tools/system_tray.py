from typing import Union
from PySide6.QtWidgets import QSystemTrayIcon
from PySide6.QtGui import QIcon, QPixmap
from ..core import AbstractQObject


class SystemTray(AbstractQObject, QSystemTrayIcon):
    def __init__(self, **kwargs):
        QSystemTrayIcon.__init__(self)
        super().__init__(**kwargs)

    def alert(self, 
              title: str,
              msg: str = "", 
              icon: Union[QIcon, QPixmap, QSystemTrayIcon.MessageIcon] \
                  = QSystemTrayIcon.MessageIcon.Warning,
              timeout: int = 2000) -> None:
        self.showMessage(title, msg, icon, timeout)

    def notify(self, 
               title: str,
               msg: str = "", 
               icon: Union[QIcon, QPixmap, QSystemTrayIcon.MessageIcon] \
                   = QSystemTrayIcon.MessageIcon.Information,
               timeout: int = 2000) -> None:
        self.alert(title, msg, icon, timeout)