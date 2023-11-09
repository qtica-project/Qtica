# coding:utf-8
from PySide6.QtGui import QColor
from random import random
from re import split


# def imageAverageColor(image: str):
#     ...


def mixColor(c1: QColor, c2: QColor, weight: float) -> QColor:
    """ mix two color

    Parameters
    ----------
    c1, c2: QColor
        the color to be mixed

    weight: float
        the weight of first color
    """
    r = int(c1.red()*weight + c2.red()*(1-weight))
    g = int(c1.green()*weight + c2.green()*(1-weight))
    b = int(c1.blue()*weight + c2.blue()*(1-weight))
    return QColor(r, g, b)


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


def translucent(color: QColor, alpha: int) -> QColor:
    return QColor(color.red(), color.green(), color.blue(), alpha)


def get_color_from_hex(s):
    '''Transform a hex string color to a kivy
    :class:`~kivy.graphics.Color`.
    '''
    if s.startswith('#'):
        return get_color_from_hex(s[1:])

    value = [int(x, 16) / 255.
             for x in split('([0-9a-f]{2})', s.lower()) if x != '']
    if len(value) == 3:
        value.append(1.0)
    return value


def get_hex_from_color(*rgb: list[int]):
    '''Transform a rgb(0, 0, 0) color to hex value::
        >>> get_hex_from_color((0, 1, 0))
        '#00ff00'
        >>> get_hex_from_color((25, 77, 90, 5))
        '#3fc4e57f'

    '''
    return '#' + ''.join(['{0:02x}'.format(int(x)) for x in rgb])


def get_random_color(alpha=1.0):
    '''Returns a random color (4 tuple).

    :Parameters:
        `alpha`: float, defaults to 1.0
            If alpha == 'random', a random alpha value is generated.
    '''
    return [random(), random(), random(), random() if alpha == 'random' else alpha]


def is_color_transparent(c):
    '''Return True if the alpha channel is 0.'''
    if len(c) < 4:
        return False

    if float(c[3]) == 0.:
        return True

    return False