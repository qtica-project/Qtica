from dataclasses import dataclass
from typing import Callable, TypeAlias, Union

from qtpy.QtCore import Qt, QPoint, QPointF


@dataclass
class PosEventsRange:
    start: int | Callable
    stop: int | Callable

    def _start(self) -> int:
        if callable(self.start):
            return self.start()
        return self.start

    def _stop(self) -> int:
        if callable(self.stop):
            return self.stop()
        return self.stop


@dataclass
class PosEventsArg:
    x: int | PosEventsRange
    y: int | PosEventsRange
    func: Callable
    button: Qt.MouseButton = None
    modifiers: Qt.KeyboardModifier = None

    def _check_var_type(self, _type: object) -> bool:
        return all(isinstance(var, _type) for var in (self.x, self.y))

    def _x_in_range(self, value: int) -> bool:
        return self.x._stop() >= value >= self.x._start()

    def _y_in_range(self, value: int) -> bool:
        return self.y._stop() >= value >= self.y._start()

    def _pos_in_range(self, x: int, y: int) -> bool:
        return self._x_in_range(x) and self._y_in_range(y)

    def _equal_pos(self, x: int, y: int) -> bool:
        return self.x == x and self.y == y


PosEventsType: TypeAlias = Union[tuple[int, int, Callable], 
                                tuple[Union[QPoint, QPointF], Callable],
                                tuple[PosEventsRange, PosEventsRange, Callable],
                                PosEventsArg]

@dataclass(kw_only=True)
class PosEvents:
    clicked: list[PosEventsType] = None
    double_clicked: list[PosEventsType] = None
    # hover: list[PosEventsType] = None
    # leave: list[PosEventsType] = None