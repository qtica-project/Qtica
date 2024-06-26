from PySide6.QtCore import QParallelAnimationGroup, QSequentialAnimationGroup
from ..core import AbstractQObject


class SequentialAnimationGroup(AbstractQObject, QSequentialAnimationGroup):
    def __init__(self, *, running: bool = True, **kwargs):
        QSequentialAnimationGroup.__init__(self)
        super().__init__(**kwargs)

        self._running = running


class ParallelAnimationGroup(AbstractQObject, QParallelAnimationGroup):
    def __init__(self, *, running: bool = True, **kwargs):
        QParallelAnimationGroup.__init__(self)
        super().__init__(**kwargs)

        self._running = running