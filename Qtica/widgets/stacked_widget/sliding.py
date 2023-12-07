#!/usr/bin/python3

from typing import Union
from PySide6.QtWidgets import QStackedWidget, QWidget
from PySide6.QtCore import (
    Qt,
    QEasingCurve,
    QPoint,
    Slot,
    QParallelAnimationGroup,
    QPropertyAnimation,
    QAbstractAnimation,
)
from ...core import WidgetBase
from ...utils._routes import Routes



class _SlidingStackedWidget(QStackedWidget):
    def __init__(
        self,
        parent: object = None,
        direction: Qt.Orientation = Qt.Orientation.Horizontal,
        animation_type: QEasingCurve = QEasingCurve.Type.OutCubic,
        speed: int = 1000,
        current: int = 0,
        next: int = 0,
        wrap: bool = False,
        pnow=None,
        active: bool = False
    ):
        QStackedWidget.__init__(self, parent)

        self.m_direction = direction  # QtCore.Qt.Vertical
        self.m_speed = speed
        self.m_animationtype = animation_type
        self.m_now = current
        self.m_next = next
        self.m_wrap = wrap
        self.m_pnow = pnow
        self.m_active = active

    def setDirection(self, direction: Qt.Orientation):
        self.m_direction = direction

    def setSpeed(self, speed: int):
        self.m_speed = speed

    def setAnimation(self, animationtype: QEasingCurve):
        self.m_animationtype = animationtype

    def setWrap(self, wrap: bool):
        self.m_wrap = wrap

    def setCurrentIndex(self, index: int) -> None:
        self.slideInIdx(index)
        return super().setCurrentIndex(index)
    
    def setCurrentWidget(self, w: QWidget) -> None:
        self.slideInWgt(w)
        return super().setCurrentWidget(w)

    @Slot()
    def slideInPrev(self):
        now = self.currentIndex()
        if self.m_wrap or now > 0:
            self.slideInIdx(now - 1)

    @Slot()
    def slideInNext(self):
        now = self.currentIndex()
        if self.m_wrap or now < (self.count() - 1):
            self.slideInIdx(now + 1)

    def slideInIdx(self, idx: int):
        if idx > (self.count() - 1):
            idx = idx % self.count()
        elif idx < 0:
            idx = (idx + self.count()) % self.count()
        self.slideInWgt(self.widget(idx))

    def slideInIndex(self, index: int):
        self.slideInIdx(index)

    def slideInWgt(self, widget):
        if self.m_active:
            return

        self.m_active = True

        _now = self.currentIndex()
        _next = self.indexOf(widget)

        if _now == _next:
            self.m_active = False
            return

        offsetx, offsety = (
            self.frameRect().width() + 500,
            self.frameRect().height() + 500,
        )

        self.widget(_next).setGeometry(self.frameRect())

        if not self.m_direction == Qt.Orientation.Horizontal:
            if _now < _next:
                offsetx, offsety = 0, -offsety
            else:
                offsetx = 0
        else:
            if _now < _next:
                offsetx, offsety = -offsetx, 0
            else:
                offsety = 0

        pnext = self.widget(_next).pos()
        pnow = self.widget(_now).pos()

        self.m_pnow = pnow if self.m_pnow is None else self.m_pnow

        offset = QPoint(offsetx, offsety)

        self.widget(_next).move(pnext - offset)
        self.widget(_next).show()
        self.widget(_next).raise_()

        anim_group = QParallelAnimationGroup(self, finished=self.animationDoneSlot)

        for (index, start, end) in zip(
            (_now, _next), (pnow, pnext - offset), (pnow + offset, pnext)
        ):
            animation = QPropertyAnimation(
                self.widget(index),
                b"pos",
                duration=self.m_speed,
                easingCurve=self.m_animationtype,
                startValue=start,
                endValue=end,
            )

            anim_group.addAnimation(animation)

        self.m_next = _next
        self.m_now = _now
        self.m_active = True

        anim_group.start(QAbstractAnimation.DeletionPolicy.DeleteWhenStopped)

    @Slot()
    def animationDoneSlot(self):
        self.setCurrentIndex(self.m_next)
        self.widget(self.m_now).hide()
        self.widget(self.m_now).move(self.m_pnow)
        self.m_active = False

    def setIndex(self, index: int):
        self.slideInIdx(index)

    def setWidget(self, widget: object):
        self.slideInWgt(widget)

    def setNext(self):
        self.slideInNext()

    def setPrev(self):
        self.slideInPrev()


class SlidingStackedWidget(WidgetBase, _SlidingStackedWidget):
    def __init__(self, 
                 *,
                 children: Union[list[QWidget], dict[str, QWidget]] = None,
                 direction: Qt.Orientation = Qt.Orientation.Horizontal,
                 easing_curve: QEasingCurve = QEasingCurve.Type.OutCubic,
                 speed: int = 500,
                 current: int = 0,
                 next: int = 0,
                 wrap: bool = False,
                 pnow = None,
                 active: bool = False,
                 **kwargs):
        _SlidingStackedWidget.__init__(self,
                                       None,
                                       direction,
                                       easing_curve,
                                       speed,
                                       current,
                                       next,
                                       wrap,
                                       pnow,
                                       active)
        super().__init__(**kwargs)

        if isinstance(children, dict):
            self._routes = Routes(self, "/")
            self.__setattr__("route", self._routes)
            self.__setattr__("push", lambda route: self._routes.push(route))

        if children is not None:
            self._set_children(children)

    def _set_children(self, children) -> None:
        if not isinstance(children, dict):
            for child in children:
                self.addWidget(child)
        else:
            for route, child in children.items():
                if child is not None:
                    self._routes.add(route, child)


if __name__ == "__main__":
    import sys
    import random
    from PySide6 import QtWidgets, QtGui, QtCore
    
    class MainWindow(QtWidgets.QMainWindow):
        def __init__(self, parent=None):
            super(MainWindow, self).__init__(parent)

            slidingStacked = _SlidingStackedWidget()
            for i in range(10):
                label = QtWidgets.QLabel(
                    "Qt is cool " + i * "!", alignment=QtCore.Qt.AlignCenter
                )
                color = QtGui.QColor(*random.sample(range(255), 3))
                label.setStyleSheet(
                    "QLabel{ background-color: %s; color : white; font: 40pt}"
                    % (color.name(),)
                )
                slidingStacked.addWidget(label)

            button_prev = QtWidgets.QPushButton(
                "Previous", pressed=slidingStacked.slideInPrev
            )
            button_next = QtWidgets.QPushButton(
                "Next", pressed=slidingStacked.slideInNext
            )

            hlay = QtWidgets.QHBoxLayout()
            hlay.addWidget(button_prev)
            hlay.addWidget(button_next)

            central_widget = QtWidgets.QWidget()
            self.setCentralWidget(central_widget)
            lay = QtWidgets.QVBoxLayout(central_widget)
            lay.addLayout(hlay)
            lay.addWidget(slidingStacked)

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())