#!/usr/bin/python3

import math

from .geometry import circumcircle, minimum_bounding_circle, Vector
from .vector import Vector, Vector2D


def boundary(value, minvalue, maxvalue):
    '''Limit a value between a minvalue and maxvalue.'''
    return min(max(value, minvalue), maxvalue)


def intersection(set1, set2):
    '''Return the intersection of 2 lists.'''
    return [s for s in set1 if s in set2]


def difference(set1, set2):
    '''Return the difference between 2 lists.'''
    return [s for s in set1 if s not in set2]


def interpolate(value_from, value_to, step=10):
    '''Interpolate between two values. This can be useful for smoothing some
    transitions. For example::

        # instead of setting directly
        self.pos = pos

        # use interpolate, and you'll have a nicer transition
        self.pos = interpolate(self.pos, new_pos)

    .. warning::
        These interpolations work only on lists/tuples/doubles with the same
        dimensions. No test is done to check the dimensions are the same.
    '''
    if type(value_from) in (list, tuple):
        out = []
        for x, y in zip(value_from, value_to):
            out.append(interpolate(x, y, step))
        return out
    else:
        return value_from + (value_to - value_from) / float(step)

def format_bytes_to_human(size: int, precision: int = 2) -> str:
    '''Format a byte value to a human readable representation (B, KB, MB...).

    .. versionadded:: 1.0.8

    :Parameters:
        `size`: int
            Number that represents the bytes value
        `precision`: int, defaults to 2
            Precision after the comma

    Examples::

        >>> format_bytes_to_human(6463)
        '6.31 KB'
        >>> format_bytes_to_human(646368746541)
        '601.98 GB'
    '''
    size = int(size)
    fmt = '%%1.%df %%s' % precision
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return fmt % (size, unit)
        size /= 1024.0


def deg_to_coordinates(degrees: int, width: int) -> tuple[int, int, int, int]:
    # Convert degrees to radians
    radians = math.radians(degrees)

    # Calculate x and y components based on angle
    x_component = math.cos(radians)
    y_component = math.sin(radians)

    # Calculate half-width components
    half_width_x = (width / 2) * y_component
    half_width_y = (width / 2) * x_component

    # Define start and end points for a linear gradient
    xStart, yStart = (0.5 - half_width_x, 0.5 + half_width_y)
    xFinalStop, yFinalStop = (0.5 + half_width_x, 0.5 - half_width_y)

    return xStart, yStart, xFinalStop, yFinalStop