'''Vector
======

The :class:`Vector` represents a 2D vector (x, y).
Our implementation is built on top of a Python list.

 An example of constructing a Vector::

    >>> # Construct a point at 82,34
    >>> v = Vector(82, 34)
    >>> v[0]
    82
    >>> v.x
    82
    >>> v[1]
    34
    >>> v.y
    34

    >>> # Construct by giving a list of 2 values
    >>> pos = (93, 45)
    >>> v = Vector(pos)
    >>> v[0]
    93
    >>> v.x
    93
    >>> v[1]
    45
    >>> v.y
    45


Optimized usage
---------------

Most of the time, you can use a list for arguments instead of using a
Vector. For example, if you want to calculate the distance between 2
points::

    a = (10, 10)
    b = (87, 34)

    # optimized method
    print('distance between a and b:', Vector(a).distance(b))

    # non-optimized method
    va = Vector(a)
    vb = Vector(b)
    print('distance between a and b:', va.distance(vb))


Vector operators
----------------

The :class:`Vector` supports some numeric operators such as +, -, /::

    >>> Vector(1, 1) + Vector(9, 5)
    [10, 6]

    >>> Vector(9, 5) - Vector(5, 5)
    [4, 0]

    >>> Vector(10, 10) / Vector(2., 4.)
    [5.0, 2.5]

    >>> Vector(10, 10) / 5.
    [2.0, 2.0]


You can also use in-place operators::

    >>> v = Vector(1, 1)
    >>> v += 2
    >>> v
    [3, 3]
    >>> v *= 5
    [15, 15]
    >>> v /= 2.
    [7.5, 7.5]

'''

__all__ = ('Vector', 'Vector2D')

import math


class Vector(list):
    '''Vector class. See module documentation for more information.
    '''

    def __init__(self, *largs):
        if len(largs) == 1:
            super(Vector, self).__init__(largs[0])
        elif len(largs) == 2:
            super(Vector, self).__init__(largs)
        else:
            raise Exception('Invalid vector')

    def _get_x(self):
        return self[0]

    def _set_x(self, x):
        self[0] = x

    x = property(_get_x, _set_x)
    ''':attr:`x` represents the first element in the list.

    >>> v = Vector(12, 23)
    >>> v[0]
    12
    >>> v.x
    12
    '''

    def _get_y(self):
        return self[1]

    def _set_y(self, y):
        self[1] = y

    y = property(_get_y, _set_y)
    ''':attr:`y` represents the second element in the list.

    >>> v = Vector(12, 23)
    >>> v[1]
    23
    >>> v.y
    23

    '''

    def __getslice__(self, i, j):
        try:
            # use the list __getslice__ method and convert
            # result to vector
            return Vector(super(Vector, self).__getslice__(i, j))
        except Exception:
            raise TypeError('vector::FAILURE in __getslice__')

    def __add__(self, val):
        return Vector(list(map(lambda x, y: x + y, self, val)))

    def __iadd__(self, val):
        if type(val) in (int, float):
            self.x += val
            self.y += val
        else:
            self.x += val.x
            self.y += val.y
        return self

    def __neg__(self):
        return Vector([-x for x in self])

    def __sub__(self, val):
        return Vector(list(map(lambda x, y: x - y, self, val)))

    def __isub__(self, val):
        if type(val) in (int, float):
            self.x -= val
            self.y -= val
        else:
            self.x -= val.x
            self.y -= val.y
        return self

    def __mul__(self, val):
        try:
            return Vector(list(map(lambda x, y: x * y, self, val)))
        except Exception:
            return Vector([x * val for x in self])

    def __imul__(self, val):
        if type(val) in (int, float):
            self.x *= val
            self.y *= val
        else:
            self.x *= val.x
            self.y *= val.y
        return self

    def __rmul__(self, val):
        return (self * val)

    def __truediv__(self, val):
        try:
            return Vector(list(map(lambda x, y: x / y, self, val)))
        except Exception:
            return Vector([x / val for x in self])

    def __div__(self, val):
        try:
            return Vector(list(map(lambda x, y: x / y, self, val)))
        except Exception:
            return Vector([x / val for x in self])

    def __rtruediv__(self, val):
        try:
            return Vector(*val) / self
        except Exception:
            return Vector(val, val) / self

    def __rdiv__(self, val):
        try:
            return Vector(*val) / self
        except Exception:
            return Vector(val, val) / self

    def __idiv__(self, val):
        if type(val) in (int, float):
            self.x /= val
            self.y /= val
        else:
            self.x /= val.x
            self.y /= val.y
        return self

    def length(self):
        '''Returns the length of a vector.

        >>> Vector(10, 10).length()
        14.142135623730951
        >>> pos = (10, 10)
        >>> Vector(pos).length()
        14.142135623730951

        '''
        return math.sqrt(self[0] ** 2 + self[1] ** 2)

    def length2(self):
        '''Returns the length of a vector squared.

        >>> Vector(10, 10).length2()
        200
        >>> pos = (10, 10)
        >>> Vector(pos).length2()
        200

        '''
        return self[0] ** 2 + self[1] ** 2

    def distance(self, to):
        '''Returns the distance between two points.

        >>> Vector(10, 10).distance((5, 10))
        5.
        >>> a = (90, 33)
        >>> b = (76, 34)
        >>> Vector(a).distance(b)
        14.035668847618199

        '''
        return math.sqrt((self[0] - to[0]) ** 2 + (self[1] - to[1]) ** 2)

    def distance2(self, to):
        '''Returns the distance between two points squared.

        >>> Vector(10, 10).distance2((5, 10))
        25

        '''
        return (self[0] - to[0]) ** 2 + (self[1] - to[1]) ** 2

    def normalize(self):
        '''Returns a new vector that has the same direction as vec,
        but has a length of one.

        >>> v = Vector(88, 33).normalize()
        >>> v
        [0.93632917756904444, 0.3511234415883917]
        >>> v.length()
        1.0

        '''
        if self[0] == 0. and self[1] == 0.:
            return Vector(0., 0.)
        return self / self.length()

    def dot(self, a):
        '''Computes the dot product of a and b.

        >>> Vector(2, 4).dot((2, 2))
        12

        '''
        return self[0] * a[0] + self[1] * a[1]

    def angle(self, a):
        '''Computes the angle between a and b, and returns the angle in
        degrees.

        >>> Vector(100, 0).angle((0, 100))
        -90.0
        >>> Vector(87, 23).angle((-77, 10))
        -157.7920283010705

        '''
        angle = -(180 / math.pi) * math.atan2(
            self[0] * a[1] - self[1] * a[0],
            self[0] * a[0] + self[1] * a[1])
        return angle

    def rotate(self, angle):
        '''Rotate the vector with an angle in degrees.

        >>> v = Vector(100, 0)
        >>> v.rotate(45)
        [70.71067811865476, 70.71067811865474]

        '''
        angle = math.radians(angle)
        return Vector(
            (self[0] * math.cos(angle)) - (self[1] * math.sin(angle)),
            (self[1] * math.cos(angle)) + (self[0] * math.sin(angle)))

    @staticmethod
    def line_intersection(v1, v2, v3, v4):
        '''
        Finds the intersection point between the lines (1)v1->v2 and (2)v3->v4
        and returns it as a vector object.

        >>> a = (98, 28)
        >>> b = (72, 33)
        >>> c = (10, -5)
        >>> d = (20, 88)
        >>> Vector.line_intersection(a, b, c, d)
        [15.25931928687196, 43.911669367909241]

        .. warning::

            This is a line intersection method, not a segment intersection.

        For math see: http://en.wikipedia.org/wiki/Line-line_intersection
        '''
        # linear algebar sucks...seriously!!
        x1, x2, x3, x4 = float(v1[0]), float(v2[0]), float(v3[0]), float(v4[0])
        y1, y2, y3, y4 = float(v1[1]), float(v2[1]), float(v3[1]), float(v4[1])

        u = (x1 * y2 - y1 * x2)
        v = (x3 * y4 - y3 * x4)
        denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if denom == 0:
            return None

        px = (u * (x3 - x4) - (x1 - x2) * v) / denom
        py = (u * (y3 - y4) - (y1 - y2) * v) / denom

        return Vector(px, py)

    @staticmethod
    def segment_intersection(v1, v2, v3, v4):
        '''
        Finds the intersection point between segments (1)v1->v2 and (2)v3->v4
        and returns it as a vector object.

        >>> a = (98, 28)
        >>> b = (72, 33)
        >>> c = (10, -5)
        >>> d = (20, 88)
        >>> Vector.segment_intersection(a, b, c, d)
        None

        >>> a = (0, 0)
        >>> b = (10, 10)
        >>> c = (0, 10)
        >>> d = (10, 0)
        >>> Vector.segment_intersection(a, b, c, d)
        [5, 5]
        '''

        # Yaaay! I love linear algebra applied within the realms of geometry.
        x1, x2, x3, x4 = float(v1[0]), float(v2[0]), float(v3[0]), float(v4[0])
        y1, y2, y3, y4 = float(v1[1]), float(v2[1]), float(v3[1]), float(v4[1])

        # This is mostly the same as the line_intersection
        u = (x1 * y2 - y1 * x2)
        v = (x3 * y4 - y3 * x4)
        denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if denom == 0:
            return None

        px = (u * (x3 - x4) - (x1 - x2) * v) / denom
        py = (u * (y3 - y4) - (y1 - y2) * v) / denom
        # Here are the new bits
        c1 = (x1 <= px <= x2) or (x2 <= px <= x1) or (x1 == x2)
        c2 = (y1 <= py <= y2) or (y2 <= py <= y1) or (y1 == y2)
        c3 = (x3 <= px <= x4) or (x4 <= px <= x3) or (x3 == x4)
        c4 = (y3 <= py <= y4) or (y4 <= py <= y3) or (y3 == y4)

        if (c1 and c2) and (c3 and c4):
            return Vector(px, py)
        else:
            return None

    @staticmethod
    def in_bbox(point, a, b):
        '''Return True if `point` is in the bounding box defined by `a`
        and `b`.

        >>> bmin = (0, 0)
        >>> bmax = (100, 100)
        >>> Vector.in_bbox((50, 50), bmin, bmax)
        True
        >>> Vector.in_bbox((647, -10), bmin, bmax)
        False

        '''
        return ((point[0] <= a[0] and point[0] >= b[0] or
                 point[0] <= b[0] and point[0] >= a[0]) and
                (point[1] <= a[1] and point[1] >= b[1] or
                 point[1] <= b[1] and point[1] >= a[1]))



class Vector2D(complex):
    """
    Simple immutable 2D vector class based on the Python complex number type

    Create and access - coordinates

    >>> v = Vector(1, 2)
    >>> v.x, v.y
    (1.0, 2.0)

    Create and access - angle and magnitude (length)

    >>> v = Vector.polar(math.pi, 2)
    >>> v
    Vector(-2.0, 0.0)
    >>> v.magnitude  # Length of the vector, alias for abs(v)
    2.0
    >>> v.radians
    3.141592653589793
    >>> v.degrees
    180.0

    Arithmetic operations

    >>> Vector(1, 1) + 2
    Vector(3.0, 1.0)
    >>> Vector(0.1, 0.1) + Vector(0.2, 0.2)  == Vector(0.3, 0.3)  # Float tolerance 10 decimals
    True
    >>> Vector(2, 3) - Vector(1, 1)
    Vector(1.0, 2.0)
    >>> Vector(1, 1) * 2
    Vector(2.0, 2.0)
    >>> round(Vector.polar(math.pi / 4, 1), 1)
    Vector(0.7, 0.7)

    Get a new vector by adjusting one of the coordinates
    >>> v = Vector()
    >>> v.with_x(1)
    Vector(1.0, 0.0)
    >>> v.with_y(2)
    Vector(0.0, 2.0)

    Get a new vector by adjusting angle or magnitude

    >>> v = Vector(1, 2)
    >>> v = v.with_magnitude(4.47213595499958)  # Twice as long
    >>> v.x, v.y
    (2.0, 4.0)

    >>> v = Vector.polar(math.pi, 2)
    >>> v
    Vector(-2.0, 0.0)
    >>> v.with_radians(0)
    Vector(2.0, 0.0)
    >>> v.with_degrees(90)
    Vector(0.0, 2.0)
    """

    abs_tol = 1e-10

    x = complex.real
    y = complex.imag

    def __add__(self, other):
        return type(self)(complex.__add__(self, other))

    def __sub__(self, other):
        return type(self)(complex.__sub__(self, other))

    def __mul__(self, other):
        return type(self)(complex.__mul__(self, other))

    def __truediv__(self, other):
        return type(self)(complex.__truediv__(self, other))

    def __len__(self):
        return 2

    def __round__(self, ndigits=None):
        return type(self)(round(self.x, ndigits), round(self.y, ndigits))

    def __eq__(self, other):
        return math.isclose(self.x, other.x, abs_tol=self.abs_tol) and math.isclose(
            self.y, other.y, abs_tol=self.abs_tol
        )

    def __ne__(self, other):
        return not self.__eq__(other)

    def __iter__(self):
        return iter([self.x, self.y])

    def __str__(self):
        return str(tuple(self))

    def __repr__(self):
        return f"{type(self).__name__}{str(self)}"

    @classmethod
    def polar(cls, radians, magnitude):
        return cls(
            round(math.cos(radians) * magnitude, 10),
            round(math.sin(radians) * magnitude, 10),
        )

    @property
    def magnitude(self):
        return abs(self)

    @property
    def degrees(self):
        return math.degrees(self.radians)

    @property
    def radians(self):
        return math.atan2(self.y, self.x)

    def with_x(self, value):
        return type(self)(value, self.y)

    def with_y(self, value):
        return type(self)(self.x, value)

    def with_magnitude(self, value):
        return self * value / abs(self)

    def with_radians(self, value):
        magnitude = abs(self)
        return type(self).polar(value, magnitude)

    def with_degrees(self, value):
        radians = math.radians(value)
        magnitude = abs(self)
        return type(self).polar(radians, magnitude)
