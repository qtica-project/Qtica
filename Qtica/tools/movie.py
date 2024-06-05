#!/usr/bin/python3

from typing import Union
from enum import IntEnum
from PySide6.QtGui import QMovie
from PySide6.QtCore import QByteArray
from ..core import AbstractQObject


class Movie(AbstractQObject, QMovie):
    class Loop(IntEnum):
        infinite: int = -1

    def __init__(self,
                 filename: str = None,
                 *,
                 format: QByteArray | bytes = None,
                 running: bool = True,
                 loop: Union[Loop, int] = Loop.infinite,
                 **kwargs):
        QMovie.__init__(self)

        self.set_loop_count(loop)
        self._current_loop_count = self._get_loop_count(loop)

        self.frameChanged.connect(self._check_loop_count)

        if filename is not None:
            self.setFileName(filename)

        if format is not None:
            self.setFormat(format)

        if running:
            self.start()

        super().__init__(**kwargs)

    @property
    def current_value(self) -> int:
        return self.currentFrameNumber()

    @property
    def current_loop_count(self) -> int:
        return self._loop_count - self._current_loop_count

    @property
    def is_paused(self) -> bool:
        return self.state() == QMovie.MovieState.Paused

    @property
    def is_running(self) -> bool:
        return self.state() == QMovie.MovieState.Running

    def loopCount(self) -> int:
        return self._loop_count

    def _get_loop_count(self, count) -> int:
        return count.value if isinstance(count, Movie.Loop) else count

    def set_loop_count(self, count: Union[Loop, int]) -> int:
        self._loop_count = self._get_loop_count(count)

    def jump_next(self) -> bool:
        return self.jumpToNextFrame()

    def jump_prev(self) -> bool:
        self.jumpToFrame(self.current_value - 1)

    def pause(self) -> None:
        return self.setPaused(self.state() == QMovie.MovieState.Running)

    def resum(self) -> None:
        return self.setPaused(not (self.state() == QMovie.MovieState.Paused))

    def start(self) -> None:
        return super().start()

    def _check_loop_count(self):
        if self._current_loop_count == -1:
            return

        if self.current_value == 0:
            self._current_loop_count -= 1
            if self._current_loop_count < 0:
                self._current_loop_count = self._loop_count
                self.stop()