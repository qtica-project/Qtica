
from typing import Callable, Union
from PySide6.QtGui import QAction, QIcon, QPixmap
from Qtica import BehaviorDeclarative


class MenuSeparator:
    ...


class MenuSection(BehaviorDeclarative):
    def __init__(self,
                 text: str,
                 icon: Union[QIcon, QPixmap] = None):
        return (text, icon) if icon is not None else (text,)


class MenuSimpleAction(BehaviorDeclarative):
    def __init__(self, 
                 text: str = None,
                 icon: Union[QIcon, QPixmap] = None, 
                 callable: Callable = None):

        action = QAction()

        if icon is not None:
            action.setIcon(icon)

        if callable is not None:
            action.triggered.connect(callable)

        action.setText(text)
        return action