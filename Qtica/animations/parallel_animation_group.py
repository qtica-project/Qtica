#!/usr/bin/python3

from PySide6.QtCore import QParallelAnimationGroup, QAbstractAnimation
from PySide6.QtWidgets import QWidget
from ..core import QObjectDec


class ParallelAnimationGroup(QObjectDec, QParallelAnimationGroup):
    def __init__(self,
                 *,
                 target: QWidget,
                 children: list[QAbstractAnimation] = None,
                 running: bool = False,
                 **kwargs) -> QWidget:
        QParallelAnimationGroup.__init__(self)
        super().__init__(**kwargs)

        for child in children:
            child.setTargetObject(target)
            self.addAnimation(child)

        if running:
            self.start()

        return target