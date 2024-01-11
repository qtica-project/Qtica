from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QPoint, QObject, QPointF
from PySide6.QtGui import QCursor, QPolygonF
from enum import IntEnum


class _TailPos(IntEnum):
    top = 0
    bottom = 1
    left = 2
    right = 3

    top_left = 4
    top_right = 5

    bottom_left = 6
    bottom_right = 7

    left_top = 8
    left_bottom = 9

    right_top = 10
    right_bottom = 11

    # auto = 12
    none = 13

class _TailDirection(IntEnum):
    center: int = 0
    left: int  = 1
    right: int = 2

    top = left
    bottom = right


class TeachingTipManager(QObject):
    def __init__(self, 
                 direction: _TailDirection = _TailDirection.center,
                 lenght: int = 8):
        super().__init__()

        self.direction = direction
        self.lenght = lenght

    def _direction(self):
        if self.direction == _TailDirection.left:
            return -self.lenght // 2
        elif self.direction == _TailDirection.right:
            return self.lenght // 2
        return 0

    def doLayout(self, tip: QWidget):
        tip._layout.setContentsMargins(0, 0, 0, 0)

    def position(self, tip: QWidget) -> QPoint:
        if not tip._auto_close and not tip.target:
            tip.target = QApplication.activeWindow()

        if tip.target is not None:
            return self._target_pos(tip)

        return self._cursor_pos(tip)

    def _cursor_pos(self, tip: QWidget):
        pos = QCursor.pos()
        return QPoint(pos.x() - tip.width() // 2, pos.y() + 24)

    @staticmethod
    def make(position: _TailPos):
        managers = {
            _TailPos.top: TopTailTeachingTipManager,
            _TailPos.bottom: BottomTailTeachingTipManager,
            _TailPos.left: LeftTailTeachingTipManager,
            _TailPos.right: RightTailTeachingTipManager,
            _TailPos.top_right: TopRightTailTeachingTipManager,
            _TailPos.bottom_right: BottomRightTailTeachingTipManager,
            _TailPos.top_left: TopLeftTailTeachingTipManager,
            _TailPos.bottom_left: BottomLeftTailTeachingTipManager,
            _TailPos.left_top: LeftTopTailTeachingTipManager,
            _TailPos.left_bottom: LeftBottomTailTeachingTipManager,
            _TailPos.right_top: RightTopTailTeachingTipManager,
            _TailPos.right_bottom: RightBottomTailTeachingTipManager,
            _TailPos.none: TeachingTipManager,
            # _TailPos.auto: AutoTailTeachingTipManager,
        }

        if position not in managers:
            raise ValueError(
                f'`{position}` is an invalid teaching tip position.')
        return managers[position]()


class AutoTailTeachingTipManager(TeachingTipManager):
    """ Auto tail teaching tip manager """

    def doLayout(self, tip):
        ...

    def draw(self, tip, painter):
        ...

    def _cursor_pos(self, tip: QWidget):
        ...

class TopTailTeachingTipManager(TeachingTipManager):
    """ Top tail teaching tip manager """

    def doLayout(self, tip):
        tip._layout.setContentsMargins(0, self.lenght, 0, 0)

    def draw(self, tip, painter):
        w = tip.width()
        painter.drawPolygon(
             QPolygonF([QPointF(w/2 - 7, self.lenght), 
                       QPointF(w/2 + self._direction(), 1),
                       QPointF(w/2 + 7, self.lenght)]))

    def _cursor_pos(self, tip: QWidget):
        '''
        24 = cursor hight
        '''
        pos = QCursor.pos()
        return QPoint(pos.x() - tip.width() // 2,
                      pos.y() + 24)

    def _target_pos(self, tip: QWidget):
        target = tip.target
        pos = target.mapToGlobal(QPoint(0, target.height()))
        x = pos.x() + target.width()//2 - tip.sizeHint().width()//2
        y = pos.y() - tip.layout().contentsMargins().top()
        return QPoint(x, y)


class BottomTailTeachingTipManager(TeachingTipManager):
    """ Bottom tail teaching tip manager """

    def doLayout(self, tip):
        tip._layout.setContentsMargins(0, 0, 0, self.lenght)

    def draw(self, tip, painter):
        w, h = tip.width(), tip.height()
        painter.drawPolygon(
            QPolygonF([QPointF(w/2 - 7, h - self.lenght),
                       QPointF(w/2 + self._direction(), h - 1), 
                       QPointF(w/2 + 7, h - self.lenght)]))

    def _cursor_pos(self, tip: QWidget):
        pos = QCursor.pos()
        return QPoint(pos.x() - tip.width() // 2,
                      pos.y() - tip.height() - 12)

    def _target_pos(self, tip: QWidget):
        target = tip.target
        pos = target.mapToGlobal(QPoint())
        x = pos.x() + target.width()//2 - tip.sizeHint().width()//2
        y = pos.y() - tip.sizeHint().height() + tip.layout().contentsMargins().bottom()
        return QPoint(x, y)


class LeftTailTeachingTipManager(TeachingTipManager):
    """ Left tail teaching tip manager """

    def doLayout(self, tip):
        tip._layout.setContentsMargins(self.lenght, 0, 0, 0)

    def draw(self, tip, painter):
        h = tip.height()
        painter.drawPolygon(
            QPolygonF([QPointF(self.lenght, h/2 - 7), 
                       QPointF(1, h/2 + self._direction()), 
                       QPointF(self.lenght, h/2 + 7)]))

    def _cursor_pos(self, tip: QWidget):
        pos = QCursor.pos()
        return QPoint(pos.x() + 12,
                      pos.y() - tip.height() // 2)

    def _target_pos(self, tip: QWidget):
        target = tip.target
        m = tip.layout().contentsMargins()
        pos = target.mapToGlobal(QPoint(target.width(), 0))
        x = pos.x() - m.left()
        y = pos.y() - tip.child.sizeHint().height()//2 + target.height()//2 - m.top()
        return QPoint(x, y)


class RightTailTeachingTipManager(TeachingTipManager):
    """ Left tail teaching tip manager """

    def doLayout(self, tip):
        tip._layout.setContentsMargins(0, 0, self.lenght, 0)

    def draw(self, tip, painter):
        w, h = tip.width(), tip.height()
        painter.drawPolygon(
            QPolygonF([QPointF(w - self.lenght, h/2 - 7), 
                       QPointF(w - 1, h/2 + self._direction()), 
                       QPointF(w - self.lenght, h/2 + 7)]))

    def _cursor_pos(self, tip: QWidget):
        pos = QCursor.pos()
        return QPoint(pos.x() - tip.width() - 12,
                      pos.y() - tip.height() // 2)

    def _target_pos(self, tip: QWidget):
        target = tip.target
        m = tip.layout().contentsMargins()
        pos = target.mapToGlobal(QPoint(0, 0))
        x = pos.x() - tip.sizeHint().width() + m.right()
        y = pos.y() - tip.child.sizeHint().height()//2 + target.height()//2 - m.top()
        return QPoint(x, y)


class TopLeftTailTeachingTipManager(TopTailTeachingTipManager):
    """ Top left tail teaching tip manager """

    def draw(self, tip, painter):
        painter.drawPolygon(
            QPolygonF([QPointF(20, self.lenght),
                       QPointF(27 + self._direction(), 1),
                       QPointF(34, self.lenght)]))

    def _cursor_pos(self, tip: QWidget):
        pos = QCursor.pos()
        return QPoint(pos.x() - 27,
                      pos.y() + 24)

    def _target_pos(self, tip: QWidget):
        target = tip.target
        pos = target.mapToGlobal(QPoint(0, target.height()))
        x = pos.x() - tip.layout().contentsMargins().left()
        y = pos.y() - tip.layout().contentsMargins().top()
        return QPoint(x, y)


class TopRightTailTeachingTipManager(TopTailTeachingTipManager):
    """ Top right tail teaching tip manager """

    def draw(self, tip, painter):
        w = tip.width()
        painter.drawPolygon(
            QPolygonF([QPointF(w - 20, self.lenght), 
                       QPointF(w - 27 + self._direction(), 1),
                       QPointF(w - 34, self.lenght)]))

    def _cursor_pos(self, tip: QWidget):
        pos = QCursor.pos()
        return QPoint(pos.x() - tip.width() + 27,
                      pos.y() + 24)

    def _target_pos(self, tip: QWidget):
        target = tip.target
        pos = target.mapToGlobal(QPoint(target.width(), target.height()))
        x = pos.x() - tip.sizeHint().width() + tip.layout().contentsMargins().left()
        y = pos.y() - tip.layout().contentsMargins().top()
        return QPoint(x, y)


class BottomLeftTailTeachingTipManager(BottomTailTeachingTipManager):
    """ Bottom left tail teaching tip manager """

    def draw(self, tip, painter):
        h = tip.height()
        painter.drawPolygon(
            QPolygonF([QPointF(20, h - self.lenght), 
                       QPointF(27 + self._direction(), h - 1), 
                       QPointF(34, h - self.lenght)]))

    def _cursor_pos(self, tip: QWidget):
        pos = QCursor.pos()
        return QPoint(pos.x() - 27,
                      pos.y() - tip.height() - 12)

    def _target_pos(self, tip: QWidget):
        target = tip.target
        pos = target.mapToGlobal(QPoint())
        x = pos.x() - tip.layout().contentsMargins().left()
        y = pos.y() - tip.sizeHint().height() + tip.layout().contentsMargins().bottom()
        return QPoint(x, y)


class BottomRightTailTeachingTipManager(BottomTailTeachingTipManager):
    """ Bottom right tail teaching tip manager """

    def draw(self, tip, painter):
        w, h = tip.width(), tip.height()
        painter.drawPolygon(
            QPolygonF([QPointF(w - 20, h - self.lenght), 
                       QPointF(w - 27 + self._direction(), h - 1), 
                       QPointF(w - 34, h - self.lenght)]))

    def _cursor_pos(self, tip: QWidget):
        pos = QCursor.pos()
        return QPoint(pos.x() - tip.width() + 27,
                      pos.y() - tip.height() - 12)

    def _target_pos(self, tip: QWidget):
        target = tip.target
        pos = target.mapToGlobal(QPoint(target.width(), 0))
        x = pos.x() - tip.sizeHint().width() + tip.layout().contentsMargins().left()
        y = pos.y() - tip.sizeHint().height() + tip.layout().contentsMargins().bottom()
        return QPoint(x, y)


class LeftTopTailTeachingTipManager(LeftTailTeachingTipManager):
    """ Left top tail teaching tip manager """

    def draw(self, tip, painter):
        painter.drawPolygon(
            QPolygonF([QPointF(self.lenght, 10), 
                       QPointF(1, 17 + self._direction()),
                       QPointF(self.lenght, 24)]))

    def _cursor_pos(self, tip: QWidget):
        pos = QCursor.pos()
        return QPoint(pos.x() + 12,
                      pos.y() - 17)

    def _target_pos(self, tip: QWidget):
        target = tip.target
        m = tip.layout().contentsMargins()
        pos = target.mapToGlobal(QPoint(target.width(), 0))
        x = pos.x() - m.left()
        y = pos.y() - m.top()
        return QPoint(x, y)


class LeftBottomTailTeachingTipManager(LeftTailTeachingTipManager):
    """ Left bottom tail teaching tip manager """

    def draw(self, tip, painter):
        h = tip.height()
        painter.drawPolygon(
            QPolygonF([QPointF(self.lenght, h - 10), 
                       QPointF(1, h - 17 + self._direction()), 
                       QPointF(self.lenght, h - 24)]))

    def _cursor_pos(self, tip: QWidget):
        pos = QCursor.pos()
        return QPoint(pos.x() + 12,
                      pos.y() - (tip.width() + tip.width() // 2 - 17))

    def _target_pos(self, tip: QWidget):
        target = tip.target
        m = tip.layout().contentsMargins()
        pos = target.mapToGlobal(QPoint(target.width(), target.height()))
        x = pos.x() - m.left()
        y = pos.y() - tip.sizeHint().height() + m.bottom()
        return QPoint(x, y)


class RightTopTailTeachingTipManager(RightTailTeachingTipManager):
    """ Right top tail teaching tip manager """

    def draw(self, tip, painter):
        w = tip.width()
        painter.drawPolygon(
            QPolygonF([QPointF(w - self.lenght, 10), 
                       QPointF(w - 1, 17 + self._direction()),
                       QPointF(w - self.lenght, 24)]))

    def _cursor_pos(self, tip: QWidget):
        pos = QCursor.pos()
        return QPoint(pos.x() - tip.width() - 12,
                      pos.y() - 17)

    def _target_pos(self, tip: QWidget):
        target = tip.target
        m = tip.layout().contentsMargins()
        pos = target.mapToGlobal(QPoint(0, 0))
        x = pos.x() - tip.sizeHint().width() + m.right()
        y = pos.y() - m.top()
        return QPoint(x, y)

class RightBottomTailTeachingTipManager(RightTailTeachingTipManager):
    """ Right bottom tail teaching tip manager """

    def draw(self, tip, painter):
        w, h = tip.width(), tip.height()
        painter.drawPolygon(
            QPolygonF([QPointF(w - self.lenght, h-10), 
                       QPointF(w - 1, h-17 + self._direction()), 
                       QPointF(w - self.lenght, h-24)]))

    def _cursor_pos(self, tip: QWidget):
        pos = QCursor.pos()
        return QPoint(pos.x() - tip.width() - 12,
                      pos.y() - (tip.width() + tip.width() // 2 - 17))

    def _target_pos(self, tip: QWidget):
        target = tip.target
        m = tip.layout().contentsMargins()
        pos = target.mapToGlobal(QPoint(0, target.height()))
        x = pos.x() - tip.sizeHint().width() + m.right()
        y = pos.y() - tip.sizeHint().height() + m.bottom()
        return QPoint(x, y)