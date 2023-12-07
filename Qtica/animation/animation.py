from typing import Any, Sequence, Tuple
from PySide6.QtCore import (
    QAbstractAnimation, 
    QByteArray, 
    QEasingCurve,
    QPoint,
    QPointF, 
    QRectF
)
from PySide6.QtGui import QPainterPath
from PySide6.QtWidgets import QWidget
from ..enums.animation import AnimationPath
from .property_animation import PropertyAnimation


class Animation(PropertyAnimation):
    def __init__(self, 
                 *,
                 child: QWidget,
                 property_name: QByteArray | bytes,
                 duration: int = None,
                 start_value: Any = None,
                 end_value: Any = None,
                 easing_curve: QEasingCurve | QEasingCurve.Type = None,
                 loop_count: int = None,
                 key_value: Tuple[float, Any] | Sequence[Tuple[float, Any]] = None,
                 path_type: AnimationPath = AnimationPath.linear,
                 direction: QAbstractAnimation.Direction = None,
                 running: bool = False,
                 **kwargs) -> QWidget:

        if path_type is not None:
            self._pathType = path_type
            self.setPath(path_type)

        return super().__init__(child, property_name, duration, 
                                start_value, end_value, easing_curve, 
                                loop_count, key_value, direction, 
                                running, **kwargs)

    def setPath(self, pathType):
        self._pathType = pathType
        self._path = QPainterPath()

    def updateCurrentTime(self, currentTime):
        if self._pathType == AnimationPath.circle:
            if self._path.isEmpty():                
                end = self.endValue()
                start = self.startValue()

                assert (isinstance(end, (QPoint, QPointF, QPainterPath.ElementType))
                        or isinstance(start, (QPoint, QPointF, QPainterPath.ElementType))), \
                            "startValue, endValue should be " +\
                                "QPoint | QRectF | QPainterPath.ElementType" 

                self._path.moveTo(start)
                self._path.addEllipse(QRectF(start, end))

            dura = self.duration()
            if dura == 0:
                progress = 1.0
            else:
                progress = (((currentTime - 1) % dura) + 1) / float(dura)

            eased_progress = self.easingCurve().valueForProgress(progress)
            if eased_progress > 1.0:
                eased_progress -= 1.0
            elif eased_progress < 0:
                eased_progress += 1.0

            pt = self._path.pointAtPercent(eased_progress)

            self.updateCurrentValue(pt)
            self.valueChanged.emit(pt)
        else:
            super(Animation, self).updateCurrentTime(currentTime)