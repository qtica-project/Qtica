from PySide6.QtCore import QPoint, QObject, QPointF
from PySide6.QtGui import QPainterPath, QCursor, QPolygonF
from PySide6.QtWidgets import QWidget, QApplication

from ...enums import TeachingTipTailPositions


class TeachingTipManager(QObject):
    def __init__(self, radius: int = 6):
        super().__init__()
        self.radius = radius

    def doLayout(self, tip: QWidget):
        tip._layout.setContentsMargins(0, 0, 0, 0)

    def position(self, tip: QWidget) -> QPoint:
        pos = self._pos(tip)
        x, y = pos.x(), pos.y()

        rect = QApplication.screenAt(QCursor.pos()).availableGeometry()
        x = min(max(-2, x) if QCursor().pos().x() >=
                0 else x, rect.width() - tip.width() - 4)
        y = min(max(-2, y), rect.height() - tip.height() - 4)

        return QPoint(x, y)

    def _pos(self, tip: QWidget):
        return tip.pos()

    @staticmethod
    def make(position: TeachingTipTailPositions):
        managers = {
            TeachingTipTailPositions.top: TopTailTeachingTipManager,
            TeachingTipTailPositions.bottom: BottomTailTeachingTipManager,
            TeachingTipTailPositions.left: LeftTailTeachingTipManager,
            TeachingTipTailPositions.right: RightTailTeachingTipManager,
            TeachingTipTailPositions.top_right: TopRightTailTeachingTipManager,
            TeachingTipTailPositions.bottom_right: BottomRightTailTeachingTipManager,
            TeachingTipTailPositions.top_left: TopLeftTailTeachingTipManager,
            TeachingTipTailPositions.bottom_left: BottomLeftTailTeachingTipManager,
            TeachingTipTailPositions.left_top: LeftTopTailTeachingTipManager,
            TeachingTipTailPositions.left_bottom: LeftBottomTailTeachingTipManager,
            TeachingTipTailPositions.right_top: RightTopTailTeachingTipManager,
            TeachingTipTailPositions.right_bottom: RightBottomTailTeachingTipManager,
            TeachingTipTailPositions.none: TeachingTipManager,
        }

        if position not in managers:
            raise ValueError(
                f'`{position}` is an invalid teaching tip position.')

        return managers[position]()



class TopTailTeachingTipManager(TeachingTipManager):
    """ Top tail teaching tip manager """

    def doLayout(self, tip):
        tip._layout.setContentsMargins(0, 8, 0, 0)

    def draw(self, tip, painter):
        w, h = tip.width(), tip.height()
        pt = tip._layout.contentsMargins().top()

        path = QPainterPath()
        path.addRoundedRect(1, pt, w - 2, h - pt - 1, self.radius, self.radius)
        path.addPolygon(
            QPolygonF([QPointF(w/2 - 7, pt), 
                       QPointF(w/2, 1), 
                       QPointF(w/2 + 7, pt)]))

        painter.drawPath(path.simplified())

    def _pos(self, tip: QWidget):
        target = tip.target
        pos = target.mapToGlobal(QPoint(0, target.height()))
        x = pos.x() + target.width()//2 - tip.sizeHint().width()//2
        y = pos.y() - tip.layout().contentsMargins().top()
        return QPoint(x, y)


class BottomTailTeachingTipManager(TeachingTipManager):
    """ Bottom tail teaching tip manager """

    def doLayout(self, tip):
        tip._layout.setContentsMargins(0, 0, 0, 8)

    def draw(self, tip, painter):
        w, h = tip.width(), tip.height()
        pb = tip._layout.contentsMargins().bottom()

        path = QPainterPath()
        path.addRoundedRect(1, 1, w - 2, h - pb - 1, self.radius, self.radius)
        path.addPolygon(
            QPolygonF([QPointF(w/2 - 7, h - pb), 
                       QPointF(w/2, h - 1), 
                       QPointF(w/2 + 7, h - pb)]))

        painter.drawPath(path.simplified())

    def _pos(self, tip: QWidget):
        target = tip.target
        pos = target.mapToGlobal(QPoint())
        x = pos.x() + target.width()//2 - tip.sizeHint().width()//2
        y = pos.y() - tip.sizeHint().height() + tip.layout().contentsMargins().bottom()
        return QPoint(x, y)


class LeftTailTeachingTipManager(TeachingTipManager):
    """ Left tail teaching tip manager """

    def doLayout(self, tip):
        tip._layout.setContentsMargins(8, 0, 0, 0)

    def draw(self, tip, painter):
        w, h = tip.width(), tip.height()
        pl = 8

        path = QPainterPath()
        path.addRoundedRect(pl, 1, w - pl - 2, h - 2, self.radius, self.radius)
        path.addPolygon(
            QPolygonF([QPointF(pl, h/2 - 7), 
                       QPointF(1, h/2), 
                       QPointF(pl, h/2 + 7)]))

        painter.drawPath(path.simplified())

    def _pos(self, tip: QWidget):
        target = tip.target
        m = tip.layout().contentsMargins()
        pos = target.mapToGlobal(QPoint(target.width(), 0))
        x = pos.x() - m.left()
        y = pos.y() - tip.view.sizeHint().height()//2 + target.height()//2 - m.top()
        return QPoint(x, y)


class RightTailTeachingTipManager(TeachingTipManager):
    """ Left tail teaching tip manager """

    def doLayout(self, tip):
        tip._layout.setContentsMargins(0, 0, 8, 0)

    def draw(self, tip, painter):
        w, h = tip.width(), tip.height()
        pr = 8

        path = QPainterPath()
        path.addRoundedRect(1, 1, w - pr - 1, h - 2, self.radius, self.radius)
        path.addPolygon(
            QPolygonF([QPointF(w - pr, h/2 - 7), 
                       QPointF(w - 1, h/2), 
                       QPointF(w - pr, h/2 + 7)]))

        painter.drawPath(path.simplified())

    def _pos(self, tip: QWidget):
        target = tip.target
        m = tip.layout().contentsMargins()
        pos = target.mapToGlobal(QPoint(0, 0))
        x = pos.x() - tip.sizeHint().width() + m.right()
        y = pos.y() - tip.view.sizeHint().height()//2 + target.height()//2 - m.top()
        return QPoint(x, y)


class TopLeftTailTeachingTipManager(TopTailTeachingTipManager):
    """ Top left tail teaching tip manager """

    def draw(self, tip, painter):
        w, h = tip.width(), tip.height()
        pt = tip._layout.contentsMargins().top()

        path = QPainterPath()
        path.addRoundedRect(1, pt, w - 2, h - pt - 1, self.radius, self.radius)
        path.addPolygon(
            QPolygonF([QPointF(20, pt), QPointF(27, 1), QPointF(34, pt)]))

        painter.drawPath(path.simplified())

    def _pos(self, tip: QWidget):
        target = tip.target
        pos = target.mapToGlobal(QPoint(0, target.height()))
        x = pos.x() - tip.layout().contentsMargins().left()
        y = pos.y() - tip.layout().contentsMargins().top()
        return QPoint(x, y)


class TopRightTailTeachingTipManager(TopTailTeachingTipManager):
    """ Top right tail teaching tip manager """

    def draw(self, tip, painter):
        w, h = tip.width(), tip.height()
        pt = tip._layout.contentsMargins().top()

        path = QPainterPath()
        path.addRoundedRect(1, pt, w - 2, h - pt - 1, self.radius, self.radius)
        path.addPolygon(
            QPolygonF([QPointF(w - 20, pt), QPointF(w - 27, 1), QPointF(w - 34, pt)]))

        painter.drawPath(path.simplified())

    def _pos(self, tip: QWidget):
        target = tip.target
        pos = target.mapToGlobal(QPoint(target.width(), target.height()))
        x = pos.x() - tip.sizeHint().width() + tip.layout().contentsMargins().left()
        y = pos.y() - tip.layout().contentsMargins().top()
        return QPoint(x, y)


class BottomLeftTailTeachingTipManager(BottomTailTeachingTipManager):
    """ Bottom left tail teaching tip manager """

    def draw(self, tip, painter):
        w, h = tip.width(), tip.height()
        pb = tip._layout.contentsMargins().bottom()

        path = QPainterPath()
        path.addRoundedRect(1, 1, w - 2, h - pb - 1, self.radius, self.radius)
        path.addPolygon(
            QPolygonF([QPointF(20, h - pb), QPointF(27, h - 1), QPointF(34, h - pb)]))

        painter.drawPath(path.simplified())

    def _pos(self, tip: QWidget):
        target = tip.target
        pos = target.mapToGlobal(QPoint())
        x = pos.x() - tip.layout().contentsMargins().left()
        y = pos.y() - tip.sizeHint().height() + tip.layout().contentsMargins().bottom()
        return QPoint(x, y)


class BottomRightTailTeachingTipManager(BottomTailTeachingTipManager):
    """ Bottom right tail teaching tip manager """

    def draw(self, tip, painter):
        w, h = tip.width(), tip.height()
        pb = tip._layout.contentsMargins().bottom()

        path = QPainterPath()
        path.addRoundedRect(1, 1, w - 2, h - pb - 1, self.radius, self.radius)
        path.addPolygon(
            QPolygonF([QPointF(w - 20, h - pb), 
                       QPointF(w - 27, h - 1), 
                       QPointF(w - 34, h - pb)]))

        painter.drawPath(path.simplified())

    def _pos(self, tip: QWidget):
        target = tip.target
        pos = target.mapToGlobal(QPoint(target.width(), 0))
        x = pos.x() - tip.sizeHint().width() + tip.layout().contentsMargins().left()
        y = pos.y() - tip.sizeHint().height() + tip.layout().contentsMargins().bottom()
        return QPoint(x, y)


class LeftTopTailTeachingTipManager(LeftTailTeachingTipManager):
    """ Left top tail teaching tip manager """

    def draw(self, tip, painter):
        w, h = tip.width(), tip.height()
        pl = 8

        path = QPainterPath()
        path.addRoundedRect(pl, 1, w - pl - 2, h - 2, self.radius, self.radius)
        path.addPolygon(
            QPolygonF([QPointF(pl, 10), QPointF(1, 17), QPointF(pl, 24)]))

        painter.drawPath(path.simplified())

    def _pos(self, tip: QWidget):
        target = tip.target
        m = tip.layout().contentsMargins()
        pos = target.mapToGlobal(QPoint(target.width(), 0))
        x = pos.x() - m.left()
        y = pos.y() - m.top()
        return QPoint(x, y)


class LeftBottomTailTeachingTipManager(LeftTailTeachingTipManager):
    """ Left bottom tail teaching tip manager """

    def draw(self, tip, painter):
        w, h = tip.width(), tip.height()
        pl = 9

        path = QPainterPath()
        path.addRoundedRect(pl, 1, w - pl - 1, h - 2, self.radius, self.radius)
        path.addPolygon(
            QPolygonF([QPointF(pl, h - 10), QPointF(1, h - 17), QPointF(pl, h - 24)]))

        painter.drawPath(path.simplified())

    def _pos(self, tip: QWidget):
        target = tip.target
        m = tip.layout().contentsMargins()
        pos = target.mapToGlobal(QPoint(target.width(), target.height()))
        x = pos.x() - m.left()
        y = pos.y() - tip.sizeHint().height() + m.bottom()
        return QPoint(x, y)


class RightTopTailTeachingTipManager(RightTailTeachingTipManager):
    """ Right top tail teaching tip manager """

    def draw(self, tip, painter):
        w, h = tip.width(), tip.height()
        pr = 8

        path = QPainterPath()
        path.addRoundedRect(1, 1, w - pr - 1, h - 2, self.radius, self.radius)
        path.addPolygon(
            QPolygonF([QPointF(w - pr, 10), 
                       QPointF(w - 1, 17), 
                       QPointF(w - pr, 24)]))

        painter.drawPath(path.simplified())

    def _pos(self, tip: QWidget):
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
        pr = 8

        path = QPainterPath()
        path.addRoundedRect(1, 1, w - pr - 1, h - 2, self.radius, self.radius)
        path.addPolygon(
            QPolygonF([QPointF(w - pr, h-10), 
                       QPointF(w - 1, h-17), 
                       QPointF(w - pr, h-24)]))

        painter.drawPath(path.simplified())

    def _pos(self, tip: QWidget):
        target = tip.target
        m = tip.layout().contentsMargins()
        pos = target.mapToGlobal(QPoint(0, target.height()))
        x = pos.x() - tip.sizeHint().width() + m.right()
        y = pos.y() - tip.sizeHint().height() + m.bottom()
        return QPoint(x, y)