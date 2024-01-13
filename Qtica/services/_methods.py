#!/usr/bin/python3

import re
from random import random
from typing import Union
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QColor, QGuiApplication, QLinearGradient, QPixmap, QScreen
from ..utils.maths import deg_to_coordinates
from ..core import AbstractDialog


CORNERS = {
    Qt.Corner.TopLeftCorner: Qt.Edge.LeftEdge | Qt.Edge.TopEdge,
    Qt.Corner.TopRightCorner: Qt.Edge.RightEdge | Qt.Edge.TopEdge,
    Qt.Corner.BottomLeftCorner: Qt.Edge.LeftEdge | Qt.Edge.BottomEdge,
    Qt.Corner.BottomRightCorner: Qt.Edge.RightEdge | Qt.Edge.BottomEdge
}


def showDialog(child: AbstractDialog, **kwargs) -> int:
    if kwargs.get("show"):
        return child.show()
    return child.exec()


def TakeScreenShot(*args, **kwargs) -> QPixmap:
    return QGuiApplication.primaryScreen().grabWindow(*args)


def corner_to_edge(corner: Qt.Corner,
                   default: Qt.Edge = Qt.Edge(0)) -> Qt.Edge:

    return CORNERS.get(corner, default)


def edge_to_corner(edge: Qt.Edge,
                   default: Qt.Corner = Qt.Corner.TopLeftCorner) -> Qt.Edge:

    return {v: k for k, v in CORNERS.items()}.get(edge, default)


def center_window(window: QWidget,
                  screen: QScreen = None) -> None:

    dst = screen if screen is not None else QApplication.primaryScreen()
    geo = window.frameGeometry()
    geo.moveCenter(QScreen.availableGeometry(dst).center())
    return window.move(geo.center())


def mixColor(c1: QColor, c2: QColor, weight: float) -> QColor:
    """ mix two color

    Parameters
    ----------
    c1, c2: QColor
        the color to be mixed

    weight: float
        the weight of first color
    """
    return QColor(
        *map(
            lambda color: int(getattr(c1, color)() * weight 
                              + getattr(c2, color)() * (1 - weight)),
            ("red", "green", "blue")
        )
    )

def mixLight(color: QColor, weight: float) -> QColor:
    """ mix color with white

    Parameters
    ----------
    color: QColor
        the color to be mixed

    weight: float
        the weight of `color`
    """
    return mixColor(color, QColor(255, 255, 255), weight)

def mixDark(color: QColor, weight: float) -> QColor:
    """ mix color with black

    Parameters
    ----------
    color: QColor
        the color to be mixed

    weight: float
        the weight of `color`
    """
    return mixColor(color, QColor(0, 0, 0), weight)


def randomColor(alpha: float = 1.0) -> QColor:
    '''Returns a random color (4 tuple).

    :Parameters:
        `alpha`: float, defaults to 1.0
            If alpha == -1, a random alpha value is generated.
    '''
    return QColor(*(random() * 255 for _ in range(3)), 
                  random() * 255 if alpha == -1 else alpha)

def colorToHex(color: Union[tuple[int, int, int], QColor]) -> str:
    '''Transform a rgb(0, 0, 0) color to hex value::
        >>> colorToHex((0, 1, 0))
        '#00ff00'
        >>> colorToHex((25, 77, 90, 5))
        '#3fc4e57f'
        >>> colorToHex(QColor(255, 255, 255))
        '#ffffff'
    '''
    if isinstance(color, QColor):
        return color.name(QColor.NameFormat.HexRgb)
    return '#' + ''.join('{0:02x}'.format(int(x)) for x in color)


def parse_css_linear_gradient(
        css_gradient: str, 
        qt_gradient: QLinearGradient = None,
        *,
        width: int = None,
        apply_deg: bool = False,
        reverse: bool = False) -> QLinearGradient:

    if not qt_gradient:
        if width is not None and apply_deg:
            _deg = int(re.findall(r"(\d+)deg", css_gradient, re.IGNORECASE)[0])
            qt_gradient = QLinearGradient(*deg_to_coordinates(_deg, width))
        qt_gradient = QLinearGradient(0, 0, width if width is not None else 100, 0)

    parts = re.findall(r"[rgb|rgba]\((\d+),\s*(\d+),\s*(\d+),\s*([\d.]+)\) (\d+)%", css_gradient, re.IGNORECASE)
    for index, (*colors, step) in enumerate(parts[::-1] if reverse else parts):
        if reverse:
            step = parts[-index][-1]

        color = QColor(*map(int, colors[:-1] if len(colors) > 3 else colors))
        qt_gradient.setColorAt(float(step) / 100, color)

    return qt_gradient


def parse_css_radial_gradient():
    ...

def parse_css_conic_gradient():
    ...