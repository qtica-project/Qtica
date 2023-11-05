from PySide6 import QtWidgets, QtCore, QtGui


class _OutsideNeumorphismEffect(QtWidgets.QGraphicsEffect):
    _cornerShift = (
        QtCore.Qt.TopLeftCorner, 
        QtCore.Qt.TopLeftCorner, 
        QtCore.Qt.BottomRightCorner, 
        QtCore.Qt.BottomLeftCorner
    )

    def __init__(self,
                 parent: object = None,
                 distance: int = 4, 
                 lightColor: QtGui.QColor = QtGui.QColor("#FFFFFF"),
                 darkColor: QtGui.QColor = QtGui.QColor("#7d7d7d"), 
                 clipRadius: int = 4,
                 origin: QtCore.Qt.Corner = QtCore.Qt.Corner.TopLeftCorner):
        super().__init__(parent)

        self._leftGradient = QtGui.QLinearGradient(1, 0, 0, 0)
        self._leftGradient.setCoordinateMode(QtGui.QGradient.CoordinateMode.ObjectBoundingMode)

        self._topGradient = QtGui.QLinearGradient(0, 1, 0, 0)
        self._topGradient.setCoordinateMode(QtGui.QGradient.CoordinateMode.ObjectBoundingMode)

        self._rightGradient = QtGui.QLinearGradient(0, 0, 1, 0)
        self._rightGradient.setCoordinateMode(QtGui.QGradient.CoordinateMode.ObjectBoundingMode)

        self._bottomGradient = QtGui.QLinearGradient(0, 0, 0, 1)
        self._bottomGradient.setCoordinateMode(QtGui.QGradient.CoordinateMode.ObjectBoundingMode)

        self._radial = QtGui.QRadialGradient(.5, .5, .5)
        self._radial.setCoordinateMode(QtGui.QGradient.CoordinateMode.ObjectBoundingMode)

        self._conical = QtGui.QConicalGradient(.5, .5, 0)
        self._conical.setCoordinateMode(QtGui.QGradient.CoordinateMode.ObjectBoundingMode)


        self._origin = origin

        distance = max(0, distance)
        self._clipRadius = min(distance, max(0, clipRadius))

        self._setColors(lightColor, darkColor)
        self._setDistance(distance)

    def setColors(self, 
                  color1 = QtGui.QColor("#FFFFFF"), 
                  color2 = QtGui.QColor("#7d7d7d")):
        # if (isinstance(color1, QtCore.Qt.GlobalColor) 
        #     and isinstance(color2, QtCore.Qt.GlobalColor)):

            # color1 = QtGui.QColor(color1)
            # color2 = QtGui.QColor(color2)

            self._setColors(color1, color2)
            self._setDistance(self._distance)

            self.update()

    def _setColors(self, color1, color2):
        self._baseStart = color1
        self._baseStop = QtGui.QColor(color1)
        self._baseStop.setAlpha(0)

        self._shadowStart = color2
        self._shadowStop = QtGui.QColor(color2)
        self._shadowStop.setAlpha(0)

        self.lightSideStops = [(0, self._baseStart), (1, self._baseStop)]
        self.shadowSideStops = [(0, self._shadowStart), (1, self._shadowStop)]
        self.cornerStops = [(0, self._shadowStart), (.25, self._shadowStop),
                            (.75, self._shadowStop), (1, self._shadowStart)]

        self._setOrigin(self._origin)

    def distance(self):
        return self._distance

    def setDistance(self, distance):
        if distance == self._distance:
            return

        self._setDistance(distance)
        self.updateBoundingRect()

    def _getCornerPixmap(self, rect, grad1, grad2=None):
        pm = QtGui.QPixmap(self._distance + self._clipRadius, 
                           self._distance + self._clipRadius)
        pm.fill(QtCore.Qt.GlobalColor.transparent)

        qp = QtGui.QPainter(pm)

        if self._clipRadius > 1:
            path = QtGui.QPainterPath()
            path.addRect(rect)
            size = self._clipRadius * 2 - 1
            mask = QtCore.QRectF(0, 0, size, size)
            mask.moveCenter(rect.center())
            path.addEllipse(mask)
            qp.setClipPath(path)
        qp.fillRect(rect, grad1)
        if grad2:
            qp.setCompositionMode(qp.CompositionMode.CompositionMode_SourceAtop)
            qp.fillRect(rect, grad2)
        qp.end()
        return pm

    def _setDistance(self, distance):
        distance = max(1, distance)
        self._distance = distance
        if self._clipRadius > distance:
            self._clipRadius = distance
        distance += self._clipRadius
        r = QtCore.QRectF(0, 0, distance * 2, distance * 2)

        lightSideStops = self.lightSideStops[:]
        shadowSideStops = self.shadowSideStops[:]

        if self._clipRadius:
            gradStart = self._clipRadius / (self._distance + self._clipRadius)
            lightSideStops[0] = (gradStart, lightSideStops[0][1])
            shadowSideStops[0] = (gradStart, shadowSideStops[0][1])

        # create the 4 corners as if the light source was top-left
        self._radial.setStops(lightSideStops)
        topLeft = self._getCornerPixmap(r, self._radial)

        self._conical.setAngle(359.9)
        self._conical.setStops(self.cornerStops)

        topRight = self._getCornerPixmap(r.translated(-distance, 0), 
                                         self._radial, self._conical)

        self._conical.setAngle(270)
        self._conical.setStops(self.cornerStops)
        bottomLeft = self._getCornerPixmap(r.translated(0, -distance), 
                                           self._radial, self._conical)

        self._radial.setStops(shadowSideStops)
        bottomRight = self._getCornerPixmap(r.translated(-distance, -distance), 
                                            self._radial)

        # rotate the images according to the actual light source
        images = topLeft, topRight, bottomRight, bottomLeft
        shift = self._cornerShift.index(self._origin)
        if shift:
            transform = QtGui.QTransform().rotate(shift * 90)
            for img in images:
                img.swap(img.transformed(transform, QtCore.Qt.SmoothTransformation))

        # and reorder them if required
        self.topLeft, self.topRight, self.bottomRight, self.bottomLeft = images[-shift:] + images[:-shift]

    def origin(self):
        return self._origin

    def setOrigin(self, origin):
        origin = QtCore.Qt.Corner(origin)
        if origin == self._origin:
            return

        self._setOrigin(origin)
        self._setDistance(self._distance)

        self.update()

    def _setOrigin(self, origin):
        self._origin = origin

        gradients = self._leftGradient, self._topGradient, self._rightGradient, self._bottomGradient
        stops = self.lightSideStops, self.lightSideStops, self.shadowSideStops, self.shadowSideStops

        # assign color stops to gradients based on the light source position
        shift = self._cornerShift.index(self._origin)
        for grad, stops in zip(gradients, stops[-shift:] + stops[:-shift]):
            grad.setStops(stops)

    def clipRadius(self):
        return self._clipRadius

    def setClipRadius(self, radius):
        if radius == self._clipRadius:
            return
        self._setClipRadius(radius)
        self.update()

    def _setClipRadius(self, radius):
        radius = min(self._distance, max(0, int(radius)))
        self._clipRadius = radius
        self._setDistance(self._distance)

    def boundingRectFor(self, rect):
        d = self._distance
        return rect.adjusted(-d, -d, d, d)

    def draw(self, qp):
        restoreTransform = qp.worldTransform()

        qp.setPen(QtCore.Qt.NoPen)
        x, y, width, height = self.sourceBoundingRect(QtCore.Qt.DeviceCoordinates).getRect()
        right = x + width
        bottom = y + height
        clip = self._clipRadius
        doubleClip = clip * 2

        if self._clipRadius:
            path = QtGui.QPainterPath()
            source = self.sourcePixmap(QtCore.Qt.DeviceCoordinates)
            sourceBoundingRect = self.sourceBoundingRect(QtCore.Qt.DeviceCoordinates)
            qp.save()

            qp.setTransform(QtGui.QTransform())
            path.addRoundedRect(sourceBoundingRect.x(), sourceBoundingRect.y(), sourceBoundingRect.width(),
                                sourceBoundingRect.height(), self._clipRadius, self._clipRadius)
            qp.setClipPath(path)
            qp.drawPixmap(sourceBoundingRect.x() - self._distance, sourceBoundingRect.y() - self._distance, source)
            qp.restore()
        else:
            path = QtGui.QPainterPath()
            source = self.sourcePixmap(QtCore.Qt.DeviceCoordinates)
            sourceBoundingRect = self.sourceBoundingRect(QtCore.Qt.DeviceCoordinates)
            qp.save()
            qp.setTransform(QtGui.QTransform())
            path.addRect(sourceBoundingRect.x(), sourceBoundingRect.y(), sourceBoundingRect.width(),
                         sourceBoundingRect.height())
            qp.setClipPath(path)
            qp.drawPixmap(sourceBoundingRect.x() - self._distance, sourceBoundingRect.y() - self._distance, source)
            qp.restore()

        qp.setWorldTransform(QtGui.QTransform())
        leftRect = QtCore.QRectF(x - self._distance, y + clip, self._distance, height - doubleClip)
        qp.setBrush(self._leftGradient)
        qp.drawRect(leftRect)

        topRect = QtCore.QRectF(x + clip, y - self._distance, width - doubleClip, self._distance)
        qp.setBrush(self._topGradient)
        qp.drawRect(topRect)

        rightRect = QtCore.QRectF(right, y + clip, self._distance, height - doubleClip)
        qp.setBrush(self._rightGradient)
        qp.drawRect(rightRect)

        bottomRect = QtCore.QRectF(x + clip, bottom, width - doubleClip, self._distance)
        qp.setBrush(self._bottomGradient)
        qp.drawRect(bottomRect)

        qp.drawPixmap(x - self._distance, y - self._distance, self.topLeft)
        qp.drawPixmap(right - clip, y - self._distance, self.topRight)
        qp.drawPixmap(right - clip, bottom - clip, self.bottomRight)
        qp.drawPixmap(x - self._distance, bottom - clip, self.bottomLeft)

        qp.setWorldTransform(restoreTransform)


class _InsideNeumorphismEffect(QtWidgets.QGraphicsEffect):
    _cornerShift = (
        QtCore.Qt.TopLeftCorner, 
        QtCore.Qt.TopRightCorner,
        QtCore.Qt.BottomRightCorner, 
        QtCore.Qt.BottomLeftCorner
    )

    def __init__(self, 
                 parent: object = None,
                 distance: int = 4, 
                 lightColor: QtGui.QColor = QtGui.QColor("#FFFFFF"),
                 darkColor: QtGui.QColor = QtGui.QColor("#7d7d7d"), 
                 clipRadius: int = 4,
                 origin: QtCore.Qt.Corner = QtCore.Qt.Corner.BottomRightCorner):
        super().__init__(parent)

        self._leftGradient = QtGui.QLinearGradient(0, 0, 1, 0)
        self._leftGradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)

        self._topGradient = QtGui.QLinearGradient(0, 0, 0, 1)
        self._topGradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)

        self._rightGradient = QtGui.QLinearGradient(1, 0, 0, 0)
        self._rightGradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)

        self._bottomGradient = QtGui.QLinearGradient(0, 1, 0, 0)
        self._bottomGradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)

        self._radial = QtGui.QRadialGradient(.5, .5, .5)
        self._radial.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)

        self._conical = QtGui.QConicalGradient(.5, .5, 0)
        self._conical.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)

        self._origin = origin
        distance = max(0, distance)
        self._clipRadius = min(distance, max(0, clipRadius))

        self._setColors(lightColor, darkColor)
        self._setDistance(distance)

    def setColors(self, color1, color2):
        # if (isinstance(color1, QtCore.Qt.GlobalColor) 
        #     and isinstance(color2, QtCore.Qt.GlobalColor)):
        #     color1 = QtGui.QColor(color1)
        #     color2 = QtGui.QColor(color2)

            self._setColors(color1, color2)
            self._setDistance(self._distance)

            self.update()

    def _setColors(self, color1, color2):
        self._baseStart = color1
        self._baseStop = QtGui.QColor(color1)
        self._baseStop.setAlpha(0)

        self._shadowStart = color2
        self._shadowStop = QtGui.QColor(color2)
        self._shadowStop.setAlpha(0)

        self.lightSideStops = [(0, self._baseStart), (1, self._baseStop)]
        self.shadowSideStops = [(0, self._shadowStart), (1, self._shadowStop)]
        self.cornerStops = [(0, self._shadowStart), (.25, self._shadowStop),
                            (.75, self._shadowStop), (1, self._shadowStart)]

        self._setOrigin(self._origin)

    def distance(self):
        return self._distance

    def setDistance(self, distance):
        if distance == self._distance:
            return

        self._setDistance(distance)
        self.updateBoundingRect()

    def _getCornerPixmap(self, rect, grad1, grad2=None):
        pm = QtGui.QPixmap(self._distance + self._clipRadius, 
                           self._distance + self._clipRadius)
        pm.fill(QtCore.Qt.GlobalColor.transparent)

        qp = QtGui.QPainter(pm)
        if self._clipRadius > 1:
            path = QtGui.QPainterPath()
            size = self._clipRadius * 2 - 1
            el = QtCore.QRectF(0, 0, size, size)
            path.addEllipse(rect)
            qp.setClipPath(path)
        qp.fillRect(rect, grad1)
        if grad2:
            qp.setCompositionMode(qp.CompositionMode.CompositionMode_SourceAtop)
            qp.fillRect(rect, grad2)
        qp.end()
        return pm

    def _setDistance(self, distance):
        distance = max(1, distance)
        self._distance = distance
        if self._clipRadius > distance:
            self._clipRadius = distance
        distance += self._clipRadius
        r = QtCore.QRectF(0, 0, distance * 2, distance * 2)
        lightSideStops = self.lightSideStops[:]
        shadowSideStops = self.shadowSideStops[:]
        if self._clipRadius:
            gradStart = self._clipRadius / (self._distance + self._clipRadius)
            lightSideStops[0] = (1, lightSideStops[0][1])
            lightSideStops[1] = (gradStart, lightSideStops[1][1])
            shadowSideStops[1] = (gradStart, shadowSideStops[1][1])
            shadowSideStops[0] = (1, shadowSideStops[0][1])
        else:
            lightSideStops[0] = (1, lightSideStops[0][1])
            lightSideStops[1] = (0, lightSideStops[1][1])
            shadowSideStops[1] = (0, shadowSideStops[1][1])
            shadowSideStops[0] = (1, shadowSideStops[0][1])

        # create the 4 corners as if the light source was top-left
        self._radial.setStops(lightSideStops)
        topLeft = self._getCornerPixmap(r, self._radial)

        self._conical.setAngle(359.9)
        self._conical.setStops(self.cornerStops)
        topRight = self._getCornerPixmap(r.translated(-distance, 0), 
                                         self._radial, self._conical)

        self._conical.setAngle(270)
        self._conical.setStops(self.cornerStops)
        bottomLeft = self._getCornerPixmap(r.translated(0, -distance), 
                                           self._radial, self._conical)

        self._radial.setStops(shadowSideStops)
        bottomRight = self._getCornerPixmap(r.translated(-distance, -distance), 
                                            self._radial)

        # rotate the images according to the actual light source
        images = topLeft, topRight, bottomRight, bottomLeft

        shift = self._cornerShift.index(self._origin)
        if shift:
            transform = QtGui.QTransform().rotate(shift * 90)
            for img in images:
                img.swap(img.transformed(transform, QtCore.Qt.SmoothTransformation))

        # and reorder them if required
        self.topLeft, self.topRight, self.bottomRight, self.bottomLeft = images[-shift:] + images[:-shift]

    def origin(self):
        return self._origin

    def setOrigin(self, origin):
        origin = QtCore.Qt.Corner(origin)
        if origin == self._origin:
            return

        self._setOrigin(origin)
        self._setDistance(self._distance)
        self.update()

    def _setOrigin(self, origin):
        self._origin = origin

        gradients = self._leftGradient, self._topGradient, self._rightGradient, self._bottomGradient
        stops = self.lightSideStops, self.lightSideStops, self.shadowSideStops, self.shadowSideStops

        # assign color stops to gradients based on the light source position
        shift = self._cornerShift.index(self._origin)
        for grad, stops in zip(gradients, stops[-shift:] + stops[:-shift]):
            grad.setStops(stops)

    def clipRadius(self):
        return self._clipRadius

    def setClipRadius(self, radius):
        if radius == self._clipRadius:
            return

        self._setClipRadius(radius)
        self.update()

    def _setClipRadius(self, radius):
        radius = min(self._distance, max(0, int(radius)))
        self._clipRadius = radius
        self._setDistance(self._distance)

    def boundingRectFor(self, rect):
        d = self._distance
        return rect.adjusted(-d, -d, d, d)

    def draw(self, qp):

        restoreTransform = qp.worldTransform()

        qp.setPen(QtCore.Qt.NoPen)
        x, y, width, height = self.sourceBoundingRect(QtCore.Qt.DeviceCoordinates).getRect()
        right = x + width
        bottom = y + height
        clip = self._clipRadius
        doubleClip = clip * 2

        if self._clipRadius:
            path = QtGui.QPainterPath()
            source = self.sourcePixmap(QtCore.Qt.DeviceCoordinates)
            sourceBoundingRect = self.sourceBoundingRect(QtCore.Qt.DeviceCoordinates)
            qp.save()
            qp.setTransform(QtGui.QTransform())
            path.addRoundedRect(sourceBoundingRect, self._clipRadius, self._clipRadius)
            qp.setClipPath(path)
            qp.drawPixmap(sourceBoundingRect.x() - self._distance, sourceBoundingRect.y() - self._distance, source)
            qp.restore()
        else:
            path = QtGui.QPainterPath()
            source = self.sourcePixmap(QtCore.Qt.DeviceCoordinates)
            sourceBoundingRect = self.sourceBoundingRect(QtCore.Qt.DeviceCoordinates)
            qp.save()
            qp.setTransform(QtGui.QTransform())
            path.addRect(sourceBoundingRect.x(), sourceBoundingRect.y(), sourceBoundingRect.width(),
                         sourceBoundingRect.height())
            qp.setClipPath(path)
            qp.drawPixmap(sourceBoundingRect.x() - self._distance, sourceBoundingRect.y() - self._distance, source)
            qp.restore()

        qp.setWorldTransform(QtGui.QTransform())
        leftRect = QtCore.QRectF(x, y + clip + self._distance, self._distance,
                                 height - doubleClip - self._distance * 2)
        qp.setBrush(self._leftGradient)
        qp.drawRect(leftRect)

        topRect = QtCore.QRectF(x + clip + self._distance, y, width - doubleClip - self._distance * 2,
                                self._distance)
        qp.setBrush(self._topGradient)
        qp.drawRect(topRect)

        rightRect = QtCore.QRectF(right - self._distance, y + clip + self._distance, self._distance,
                                  height - doubleClip - self._distance * 2)
        qp.setBrush(self._rightGradient)
        qp.drawRect(rightRect)

        bottomRect = QtCore.QRectF(x + clip + self._distance, bottom - self._distance,
                                   width - doubleClip - self._distance * 2, self._distance)
        qp.setBrush(self._bottomGradient)
        qp.drawRect(bottomRect)

        qp.drawPixmap(x, y, self.topLeft)
        qp.drawPixmap(right - clip - self._distance, y, self.topRight)
        qp.drawPixmap(right - clip - self._distance, bottom - clip - self._distance, self.bottomRight)
        qp.drawPixmap(x, bottom - clip - self._distance, self.bottomLeft)

        qp.setWorldTransform(restoreTransform)



from ..core import ObjectDeclarative

class OutsideNeumorphismEffect(ObjectDeclarative, _OutsideNeumorphismEffect):
    def __init__(self, 
                 child: QtWidgets.QWidget,
                 light_color: QtGui.QColor = QtGui.QColor("#FFFFFF"),
                 dark_color: QtGui.QColor = QtGui.QColor("#7d7d7d"),
                 clip_radius: int = 4,
                 distance: int = 4,
                 origin: QtCore.Qt.Corner = QtCore.Qt.Corner.TopLeftCorner,
                 **kwargs) -> QtWidgets.QWidget:
        _OutsideNeumorphismEffect.__init__(self)
        super().__init__(**kwargs)

        self.setParent(child)
        self._set_child(child)

        if clip_radius is not None:
            self.setClipRadius(clip_radius)

        if light_color is not None and dark_color is not None:
            self.setColors(light_color,
                           dark_color)

        if distance is not None:
            self.setDistance(distance)

        if origin is not None:
            self.setOrigin(origin)

        return child

    def _set_child(self, child):
        child.setGraphicsEffect(self)

    def build(self):
        return self


class InsideNeumorphismEffect(ObjectDeclarative, _InsideNeumorphismEffect):
    def __init__(self, 
                 child: QtWidgets.QWidget,
                 light_color: QtGui.QColor = QtGui.QColor("#FFFFFF"),
                 dark_color: QtGui.QColor = QtGui.QColor("#7d7d7d"),
                 clip_radius: int = 4,
                 distance: int = 4,
                 origin: QtCore.Qt.Corner = QtCore.Qt.Corner.BottomRightCorner,
                 **kwargs):
        _InsideNeumorphismEffect.__init__(self)
        super().__init__(**kwargs)

        self.setParent(child)
        self._set_child(child)

        if clip_radius is not None:
            self.setClipRadius(clip_radius)

        if light_color is not None and dark_color is not None:
            self.setColors(light_color,
                           dark_color)

        if distance is not None:
            self.setDistance(distance)

        if origin is not None:
            self.setOrigin(origin)

        return child

    def _set_child(self, child):
        child.setGraphicsEffect(self)