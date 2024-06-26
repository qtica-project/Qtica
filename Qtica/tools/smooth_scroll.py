from collections import deque
from math import cos, pi
from enum import IntEnum
from PySide6.QtGui import QWheelEvent
from PySide6.QtCore import QDateTime, Qt, QTimer, QPoint
from PySide6.QtWidgets import QApplication, QScrollArea, QAbstractScrollArea
from ..core import AbstractDec


class SmoothScroll(AbstractDec):
    """ Scroll smoothly """

    class Mode(IntEnum):
        """ Scroll smoothly mode """

        normal = 0
        constant = 1
        linear = 2
        quadrati = 3
        cosine = 4

    def __init__(self,
                 *,
                 child: QScrollArea,
                 orient: Qt.Orientation = Qt.Orientation.Vertical,
                 mode: Mode = Mode.linear,
                 fps: int = 60,
                 duration: int = 400,
                 step_ratio: int = 1.5,
                 acceleration: int = 1,
                 steps_total: int = 0
                 ):
        """
        Parameters
        ----------
        child: QScrollArea
            scroll area to scroll smoothly

        orient: Orientation
            scroll orientation
        """
        self.child = child
        self.orient = orient

        self.fps = fps
        self.duration = duration
        self.stepsTotal = steps_total
        self.stepRatio = step_ratio
        self.acceleration = acceleration
        self.lastWheelEvent = None
        self.scrollStamps = deque()
        self.stepsLeftQueue = deque()
        self.smoothMoveTimer = QTimer(child)
        self.smoothMode = mode
        self.smoothMoveTimer.timeout.connect(self.__smoothMove)

        return self.child

    def setSmoothMode(self, smoothMode):
        """ set smooth mode """
        self.smoothMode = smoothMode

    def wheelEvent(self, e):
        # only process the wheel events triggered by mouse, fixes issue #75
        delta = e.angleDelta().y() if e.angleDelta().y() != 0 else e.angleDelta().x()
        if self.smoothMode == SmoothScroll.Mode.normal or abs(delta) % 120 != 0:
            QAbstractScrollArea.wheelEvent(self.child, e)
            return

        # push current time to queque
        now = QDateTime.currentDateTime().toMSecsSinceEpoch()
        self.scrollStamps.append(now)
        while now - self.scrollStamps[0] > 500:
            self.scrollStamps.popleft()

        # adjust the acceration ratio based on unprocessed events
        accerationRatio = min(len(self.scrollStamps) / 15, 1)
        self.lastWheelPos = e.position()
        self.lastWheelGlobalPos = e.globalPosition()

        # get the number of steps
        self.stepsTotal = self.fps * self.duration / 1000

        # get the moving distance corresponding to each event
        delta = delta* self.stepRatio
        if self.acceleration > 0:
            delta += delta * self.acceleration * accerationRatio

        # form a list of moving distances and steps, and insert it into the queue for processing.
        self.stepsLeftQueue.append([delta, self.stepsTotal])

        # overflow time of timer: 1000ms/frames
        self.smoothMoveTimer.start(int(1000 / self.fps))

    def __smoothMove(self):
        """ scroll smoothly when timer time out """
        totalDelta = 0

        # Calculate the scrolling distance of all unprocessed events,
        # the timer will reduce the number of steps by 1 each time it overflows.
        for i in self.stepsLeftQueue:
            totalDelta += self.__subDelta(i[0], i[1])
            i[1] -= 1

        # If the event has been processed, move it out of the queue
        while self.stepsLeftQueue and self.stepsLeftQueue[0][1] == 0:
            self.stepsLeftQueue.popleft()

        # construct wheel event
        if self.orient == Qt.Orientation.Vertical:
            pixelDelta = QPoint(round(totalDelta), 0)
            bar = self.child.verticalScrollBar()
        else:
            pixelDelta = QPoint(0, round(totalDelta))
            bar = self.child.horizontalScrollBar()

        e = QWheelEvent(
            self.lastWheelPos,
            self.lastWheelGlobalPos,
            pixelDelta,
            QPoint(round(totalDelta), 0),
            Qt.MouseButton.LeftButton,
            Qt.KeyboardModifier.NoModifier,
            Qt.ScrollPhase.ScrollBegin,
            False,
        )

        # send wheel event to app
        QApplication.sendEvent(bar, e)

        # stop scrolling if the queque is empty
        if not self.stepsLeftQueue:
            self.smoothMoveTimer.stop()

    def __subDelta(self, delta, stepsLeft):
        """ get the interpolation for each step """
        m = self.stepsTotal / 2
        x = abs(self.stepsTotal - stepsLeft - m)

        res = 0
        if self.smoothMode == SmoothScroll.Mode.normal:
            res = 0
        elif self.smoothMode == SmoothScroll.Mode.constant:
            res = delta / self.stepsTotal
        elif self.smoothMode == SmoothScroll.Mode.linear:
            res = 2 * delta / self.stepsTotal * (m - x) / m
        elif self.smoothMode == SmoothScroll.Mode.quadrati:
            res = 3 / 4 / m * (1 - x * x / m / m) * delta
        elif self.smoothMode == SmoothScroll.Mode.cosine:
            res = (cos(x * pi / m) + 1) / (2 * m) * delta

        return res
