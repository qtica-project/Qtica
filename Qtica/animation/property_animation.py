from PySide6.QtCore import (
    QByteArray, 
    QEasingCurve, 
    QPropertyAnimation, 
    QAbstractAnimation
)

from PySide6.QtWidgets import QWidget
from typing import Any, Sequence, Tuple

from ..enums.events import EventTypeVar
from ..enums.signals import SignalTypeVar
from ..core import ObjectDeclarative


class PropertyAnimation(ObjectDeclarative, QPropertyAnimation):
    def __init__(self, 
                 child: QWidget,
                 property_name: QByteArray | bytes,
                 duration: int = None,
                 start_value: Any = None,
                 end_value: Any = None,
                 easing_curve: QEasingCurve | QEasingCurve.Type = None,
                 loop_count: int = None,
                 key_value: Tuple[float, Any] | Sequence[Tuple[float, Any]] = None,
                 direction: QAbstractAnimation.Direction = None,
                 running: bool = False,
                 uid: str = None, 
                 signals: SignalTypeVar = None, 
                 events: EventTypeVar = None, 
                 **kwargs) -> QWidget:

        QPropertyAnimation.__init__(self)
        super().__init__(uid, signals, events, **kwargs)

        self.setTargetObject(child)

        if direction is not None:
            self.setDirection(direction)

        if property_name is not None:
            self.setPropertyName(property_name)

        if duration is not None:
            self.setDuration(duration)

        if end_value is not None:
            self.setEndValue(end_value)

        if start_value is not None:
            self.setStartValue(start_value)

        if easing_curve is not None:
            self.setEasingCurve(easing_curve)

        if loop_count is not None:
            self.setLoopCount(loop_count)

        if key_value is not None:
            if not isinstance(key_value[0], int | float):
                self.setKeyValues([(k/100 if 1 < k <= 100 else k, v) 
                                   for k, v in key_value])
            else:
                self.setKeyValueAt(key_value[0]/100
                                   if 1 < key_value[0] <= 100 
                                   else key_value[0],
                                   key_value[-1])
        if running:
            self.start()

        child._animation = self
        return child

    def build(self):
        return self