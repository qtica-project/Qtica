from typing import Union
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QMenu, QSystemTrayIcon
from ..enums.events import EventTypeVar
from ..enums.signals import SignalTypeVar
from ..core.base import ObjectBase


class SystemTray(ObjectBase, QSystemTrayIcon):
    def __init__(self, 
                 uid: str = None, 
                 signals: SignalTypeVar = None, 
                 events: EventTypeVar = None,
                 parent: object = None,
                 tip: str = None,
                 menu: QMenu = None,
                 **kwargs):
        QSystemTrayIcon.__init__(self, parent)
        super().__init__(uid, signals, events, **kwargs)

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