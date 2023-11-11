#!/usr/bin/python3
# coding:utf-8

from PySide6.QtGui import QColor
from collections import Counter
from random import random
from PIL import Image
from re import split
from typing import Any


class DetectImageColors:
    def __init__(self, image: str):

        self._image_path = image
        self._image = Image.open(image)

        # Resize the image to improve performance
        self._image = self._image.resize((100, 100))
        self._image = self._image.convert('RGB')

        # Count the occurrences of each color
        self._color_counter = Counter(self._image.getdata())

    @property
    def image_path(self) -> str:
        return self._image_path

    @property
    def total(self):
        return self._color_counter.total()

    @property
    def count(self):
        return self._color_counter.__len__()

    @property
    def colors(self) -> Any:
        return self._image.getdata()

    @property
    def most_common(self, count: int = None) -> list[tuple[tuple[int], int]]:
        '''
        count: int
            count == None, default = cls.total
        '''
        return self._color_counter.most_common(count
                                               if count is not None
                                               else self._color_counter.total())


def get_image_average_color(image: str, 
                            size: tuple = (100, 100)) -> list[int]:
    img = Image.open(image)
    img = img.convert("RGB")
    img = img.resize(size)
    return img.getpixel(tuple(map(lambda x: x  // 2, size)))


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


def get_color_from_hex(color: str):
    '''Transform a hex string color to a kivy
    :class:`~kivy.graphics.Color`.
    '''

    if color.startswith('#'):
        return get_color_from_hex(color[1:])

    value = [int(x, 16) / 255.
             for x in split('([0-9a-f]{2})', color.lower()) 
             if x != '']

    if len(value) == 3:
        value.append(1.0)

    return value


def get_hex_from_color(*rgb: list[int]) -> str:
    '''Transform a rgb(0, 0, 0) color to hex value::
        >>> get_hex_from_color((0, 1, 0))
        '#00ff00'
        >>> get_hex_from_color((25, 77, 90, 5))
        '#3fc4e57f'

    '''
    return '#' + ''.join(['{0:02x}'.format(int(x)) for x in rgb])


def get_random_color(alpha: float = 1.0) -> list[int]:
    '''Returns a random color (4 tuple).

    :Parameters:
        `alpha`: float, defaults to 1.0
            If alpha == 'random', a random alpha value is generated.
    '''
    return [random() * 255,
            random() * 255, 
            random() * 255, 
            random() * 255 if alpha == 'random' else alpha]


def is_color_transparent(*rgb: list[int]):
    '''Return True if the alpha channel is 0.'''
    if len(rgb) < 4:
        return False

    if float(rgb[3]) == 0.:
        return True

    return False


def print_hex_color(*rgb):
    '''
    arg: list[int]
        - (int, int, int, int)
        - (int, int, int)

    Return colored text.
    '''
    print('\033[38;2;{};{};{}m{}\033[0m'.format(rgb[0], rgb[1], rgb[2], rgb))