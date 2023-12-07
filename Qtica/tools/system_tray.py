from typing import Union
from PySide6.QtWidgets import QMenu, QSystemTrayIcon
from PySide6.QtGui import QIcon, QPixmap
from ..core import QObjectBase


class SystemTray(QObjectBase, QSystemTrayIcon):
    def __init__(self, 
                 *,
                 tip: str = None,
                 menu: QMenu = None,
                 **kwargs):
        QSystemTrayIcon.__init__(self)
        super().__init__(**kwargs)

        if menu is not None:
            self.setContextMenu(menu)

        if tip is not None:
            self.setToolTip(tip)

    def alert(self, 
              title: str,
              msg: str = "", 
              icon: Union[QIcon, QPixmap, QSystemTrayIcon.MessageIcon] = QSystemTrayIcon.MessageIcon.Information,
              timeout: int = 1500) -> None:
        self.showMessage(title, msg, icon, timeout)

    def notify(self, 
               title: str,
               msg: str = "", 
               icon: Union[QIcon, QPixmap, QSystemTrayIcon.MessageIcon] = QSystemTrayIcon.MessageIcon.Information,
               timeout: int = 1500) -> None:
        self.alert(title, msg, icon, timeout)