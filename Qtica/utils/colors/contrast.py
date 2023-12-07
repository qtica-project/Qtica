#!/usr/bin/python3

from __future__ import division


__all__ = ["Contrast"]


class Contrast:
    def __init__(self):
        ...

    def rgb(self, 
            rgb1: tuple[int, int, int], 
            rgb2: tuple[int, int, int]) -> float:

        for r, g, b in (rgb1, rgb2):
            if not 0.0 <= r <= 1.0:
                raise ValueError("r is out of valid range (0.0 - 1.0)")
            if not 0.0 <= g <= 1.0:
                raise ValueError("g is out of valid range (0.0 - 1.0)")
            if not 0.0 <= b <= 1.0:
                raise ValueError("b is out of valid range (0.0 - 1.0)")

        l1 = self._relative_luminance(*rgb1)
        l2 = self._relative_luminance(*rgb2)

        if l1 > l2:
            return (l1 + 0.05) / (l2 + 0.05)
        else:
            return (l2 + 0.05) / (l1 + 0.05)

    def _relative_luminance(self, r, g, b) -> float:
        r = self._linearize(r)
        g = self._linearize(g)
        b = self._linearize(b)

        return 0.2126 * r + 0.7152 * g + 0.0722 * b

    def _linearize(self, v) -> float:
        if v <= 0.03928:
            return v / 12.92
        else:
            return ((v + 0.055) / 1.055) ** 2.4

    def passes_AA(self, contrast: float, large=False) -> bool:
        if large:
            return contrast >= 3.0
        else:
            return contrast >= 4.5

    def passes_AAA(self, contrast: float, large=False) -> bool:
        if large:
            return contrast >= 4.5
        else:
            return contrast >= 7.0


class ContrastFont:
    @classmethod
    def color(cls, rgb: tuple[int, int, int]) -> tuple[int, int, int]:
        '''
        Calculate the perceptive luminance (aka luma) - human eye favors green color... 
        '''
        r, g, b, *_ = rgb
        luma = ((0.299 * r) + (0.587 * g) + (0.114 * b)) / 255
        return (0,) * 3 if luma > 0.5 else (255,) * 3