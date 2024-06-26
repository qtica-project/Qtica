from PySide6 import QtCore, QtGui
from ...core import AbstractTool


class BackingStore(AbstractTool, QtGui.QBackingStore):
    def __init__(self, *args, **kwargs):
        QtGui.QBackingStore.__init__(self, *args)
        super().__init__(**kwargs)


class Bitmap(AbstractTool, QtGui.QBitmap):
    def __init__(self, *args, **kwargs):
        QtGui.QBitmap.__init__(self, *args)
        super().__init__(**kwargs)


class Brush(AbstractTool, QtGui.QBrush):
    def __init__(self, *args, **kwargs):
        QtGui.QBrush.__init__(self, *args)
        super().__init__(**kwargs)


class ColorSpace(AbstractTool, QtGui.QColorSpace):
    def __init__(self, *args, **kwargs):
        QtGui.QColorSpace.__init__(self, *args)
        super().__init__(**kwargs)


class ConicalGradient(AbstractTool, QtGui.QConicalGradient):
    def __init__(self, *args, **kwargs):
        QtGui.QConicalGradient.__init__(self, *args)
        super().__init__(**kwargs)

    def to_qss(self) -> str:
        """qconicalgradient(cx: float, cy: float, angle: float, stop: float QColor, ...)"""
        qss = self.__class__.__base__.__name__.lower()
        qss += "("
        qss += f"cx:{str(self._point_value(self.center().x()))}, "
        qss += f"cy:{str(self._point_value(self.center().y()))}, "
        qss += f"angle:{str(self.angle())}, "
        qss += ", ".join(f"stop:{self._point_value(stop)} {self._color_to_rgba(color)}" 
                         for stop, color in self.stops())
        qss += ")"
        return qss

    def _color_to_rgba(self, color) -> str:
        return f"rgba({','.join(map(str, color.toTuple()))})"

    def _point_value(self, value) -> int:
        return 100 / value if value > 1 else value


class Cursor(AbstractTool, QtGui.QCursor):
    def __init__(self, *args, **kwargs):
        QtGui.QCursor.__init__(self, *args)
        super().__init__(**kwargs)


class DesktopServices(AbstractTool, QtGui.QDesktopServices):
    def __init__(self, *args, **kwargs):
        QtGui.QDesktopServices.__init__(self, *args)
        super().__init__(**kwargs)


class Font(AbstractTool, QtGui.QFont):
    def __init__(self, *args, **kwargs):
        QtGui.QFont.__init__(self, *args)
        super().__init__(**kwargs)


class GlyphRun(AbstractTool, QtGui.QGlyphRun):
    def __init__(self, *args, **kwargs):
        QtGui.QGlyphRun.__init__(self, *args)
        super().__init__(**kwargs)


class Gradient(AbstractTool, QtGui.QGradient):
    def __init__(self, *args, **kwargs):
        QtGui.QGradient.__init__(self, *args)
        super().__init__(**kwargs)

    def to_qss(self) -> str: ...


class Image(AbstractTool, QtGui.QImage):
    def __init__(self, *args, **kwargs):
        QtGui.QImage.__init__(self, *args)
        super().__init__(**kwargs)


class ImageIOHandler(AbstractTool, QtGui.QImageIOHandler):
    def __init__(self, *args, **kwargs):
        QtGui.QImageIOHandler.__init__(self, *args)
        super().__init__(**kwargs)


class ImageReader(AbstractTool, QtGui.QImageReader):
    def __init__(self, *args, **kwargs):
        QtGui.QImageReader.__init__(self, *args)
        super().__init__(**kwargs)


class ImageWriter(AbstractTool, QtGui.QImageWriter):
    def __init__(self, *args, **kwargs):
        QtGui.QImageWriter.__init__(self, *args)
        super().__init__(**kwargs)


class LinearGradient(AbstractTool, QtGui.QLinearGradient):
    def __init__(self, *args, **kwargs):
        QtGui.QLinearGradient.__init__(self, *args)
        super().__init__(**kwargs)

    def to_qss(self) -> str:
        """qlineargradient(x1: float, y1: float, x2: float, y2: float, stop: float QColor, ...)"""
        qss = self.__class__.__base__.__name__.lower()
        qss += "("
        qss += f"x1:{str(self._point_value(self.start().x()))}, "
        qss += f"y1:{str(self._point_value(self.start().y()))}, "
        qss += f"x2:{str(self._point_value(self.finalStop().x()))}, "
        qss += f"y2:{str(self._point_value(self.finalStop().y()))}, "
        qss += ", ".join(f"stop:{self._point_value(stop)} {self._color_to_rgba(color)}" 
                         for stop, color in self.stops())
        qss += ")"
        return qss

    def _color_to_rgba(self, color) -> str:
        return f"rgba({','.join(map(str, color.toTuple()))})"

    def _point_value(self, value) -> int:
        return 100 / value if value > 1 else value


class PageLayout(AbstractTool, QtGui.QPageLayout):
    def __init__(self, *args, **kwargs):
        QtGui.QPageLayout.__init__(self, *args)
        super().__init__(**kwargs)


class PagedPaintDevice(AbstractTool, QtGui.QPagedPaintDevice):
    def __init__(self, *args, **kwargs):
        QtGui.QPagedPaintDevice.__init__(self, *args)
        super().__init__(**kwargs)


class PaintEngine(AbstractTool, QtGui.QPaintEngine):
    def __init__(self, *args, **kwargs):
        QtGui.QPaintEngine.__init__(self, *args)
        super().__init__(**kwargs)


class Painter(AbstractTool, QtGui.QPainter):
    def __init__(self, *args, **kwargs):
        QtGui.QPainter.__init__(self, *args)
        super().__init__(**kwargs)


class PainterPathStroker(AbstractTool, QtGui.QPainterPathStroker):
    def __init__(self, *args, **kwargs):
        QtGui.QPainterPathStroker.__init__(self, *args)
        super().__init__(**kwargs)


class Palette(AbstractTool, QtGui.QPalette):
    def __init__(self, *args, **kwargs):
        QtGui.QPalette.__init__(self, *args)
        super().__init__(**kwargs)


class Pen(AbstractTool, QtGui.QPen):
    def __init__(self, *args, **kwargs):
        QtGui.QPen.__init__(self, *args)
        super().__init__(**kwargs)


class Picture(AbstractTool, QtGui.QPicture):
    def __init__(self, *args, **kwargs):
        QtGui.QPicture.__init__(self, *args)
        super().__init__(**kwargs)


class Pixmap(AbstractTool, QtGui.QPixmap):
    def __init__(self, *args, **kwargs):
        QtGui.QPixmap.__init__(self, *args)
        super().__init__(**kwargs)


class Quaternion(AbstractTool, QtGui.QQuaternion):
    def __init__(self, *args, **kwargs):
        QtGui.QQuaternion.__init__(self, *args)
        super().__init__(**kwargs)


class RadialGradient(AbstractTool, QtGui.QRadialGradient):
    def __init__(self, *args, **kwargs):
        QtGui.QRadialGradient.__init__(self, *args)
        super().__init__(**kwargs)

    def to_qss(self) -> str:
        """qradialgradient(cx: float, cy: float, radius: float, fx: float, fy: float, stop: float QColor, ...)"""
        qss = self.__class__.__base__.__name__.lower()

        qss += "("
        qss += f"cx:{str(self._point_value(self.center().x()))}, "
        qss += f"cy:{str(self._point_value(self.center().y()))}, "
        qss += f"fx:{str(self._point_value(self.focalPoint().x()))}, "
        qss += f"fy:{str(self._point_value(self.focalPoint().y()))}, "
        qss += f"radius:{str(self.radius())}, "
        qss += ", ".join(f"stop:{self._point_value(stop)} {self._color_to_rgba(color)}" 
                         for stop, color in self.stops())
        qss += ")"
        return qss

    def _color_to_rgba(self, color) -> str:
        return f"rgba({','.join(map(str, color.toTuple()))})"

    def _point_value(self, value) -> int:
        return 100 / value if value > 1 else value


class Rgba64(AbstractTool, QtGui.QRgba64):
    def __init__(self, *args, **kwargs):
        QtGui.QRgba64.__init__(self, *args)
        super().__init__(**kwargs)

if QtCore.QSysInfo.buildCpuArchitecture() != "arm64":
    class RhiBuffer(AbstractTool, QtGui.QRhiBuffer):
        def __init__(self, *args, **kwargs):
            QtGui.QRhiBuffer.__init__(self, *args)
            super().__init__(**kwargs)


    class RhiColorAttachment(AbstractTool, QtGui.QRhiColorAttachment):
        def __init__(self, *args, **kwargs):
            QtGui.QRhiColorAttachment.__init__(self, *args)
            super().__init__(**kwargs)


    class RhiCommandBuffer(AbstractTool, QtGui.QRhiCommandBuffer):
        def __init__(self, *args, **kwargs):
            QtGui.QRhiCommandBuffer.__init__(self, *args)
            super().__init__(**kwargs)


    class RhiComputePipeline(AbstractTool, QtGui.QRhiComputePipeline):
        def __init__(self, *args, **kwargs):
            QtGui.QRhiComputePipeline.__init__(self, *args)
            super().__init__(**kwargs)


    class RhiDepthStencilClearValue(AbstractTool, QtGui.QRhiDepthStencilClearValue):
        def __init__(self, *args, **kwargs):
            QtGui.QRhiDepthStencilClearValue.__init__(self, *args)
            super().__init__(**kwargs)


    class RhiGraphicsPipeline(AbstractTool, QtGui.QRhiGraphicsPipeline):
        def __init__(self, *args, **kwargs):
            QtGui.QRhiGraphicsPipeline.__init__(self, *args)
            super().__init__(**kwargs)


    class RhiReadbackDescription(AbstractTool, QtGui.QRhiReadbackDescription):
        def __init__(self, *args, **kwargs):
            QtGui.QRhiReadbackDescription.__init__(self, *args)
            super().__init__(**kwargs)


    class RhiRenderBuffer(AbstractTool, QtGui.QRhiRenderBuffer):
        def __init__(self, *args, **kwargs):
            QtGui.QRhiRenderBuffer.__init__(self, *args)
            super().__init__(**kwargs)


    class RhiRenderTarget(AbstractTool, QtGui.QRhiRenderTarget):
        def __init__(self, *args, **kwargs):
            QtGui.QRhiRenderTarget.__init__(self, *args)
            super().__init__(**kwargs)


    class RhiSampler(AbstractTool, QtGui.QRhiSampler):
        def __init__(self, *args, **kwargs):
            QtGui.QRhiSampler.__init__(self, *args)
            super().__init__(**kwargs)


    class RhiScissor(AbstractTool, QtGui.QRhiScissor):
        def __init__(self, *args, **kwargs):
            QtGui.QRhiScissor.__init__(self, *args)
            super().__init__(**kwargs)


    class RhiShaderResourceBindings(AbstractTool, QtGui.QRhiShaderResourceBindings):
        def __init__(self, *args, **kwargs):
            QtGui.QRhiShaderResourceBindings.__init__(self, *args)
            super().__init__(**kwargs)


    class RhiShaderStage(AbstractTool, QtGui.QRhiShaderStage):
        def __init__(self, *args, **kwargs):
            QtGui.QRhiShaderStage.__init__(self, *args)
            super().__init__(**kwargs)


    class RhiSwapChain(AbstractTool, QtGui.QRhiSwapChain):
        def __init__(self, *args, **kwargs):
            QtGui.QRhiSwapChain.__init__(self, *args)
            super().__init__(**kwargs)


    class RhiSwapChainRenderTarget(AbstractTool, QtGui.QRhiSwapChainRenderTarget):
        def __init__(self, *args, **kwargs):
            QtGui.QRhiSwapChainRenderTarget.__init__(self, *args)
            super().__init__(**kwargs)


    class RhiTexture(AbstractTool, QtGui.QRhiTexture):
        def __init__(self, *args, **kwargs):
            QtGui.QRhiTexture.__init__(self, *args)
            super().__init__(**kwargs)


    class RhiTextureCopyDescription(AbstractTool, QtGui.QRhiTextureCopyDescription):
        def __init__(self, *args, **kwargs):
            QtGui.QRhiTextureCopyDescription.__init__(self, *args)
            super().__init__(**kwargs)


    class RhiTextureRenderTarget(AbstractTool, QtGui.QRhiTextureRenderTarget):
        def __init__(self, *args, **kwargs):
            QtGui.QRhiTextureRenderTarget.__init__(self, *args)
            super().__init__(**kwargs)


    class RhiTextureRenderTargetDescription(AbstractTool, QtGui.QRhiTextureRenderTargetDescription):
        def __init__(self, *args, **kwargs):
            QtGui.QRhiTextureRenderTargetDescription.__init__(self, *args)
            super().__init__(**kwargs)


    class RhiTextureSubresourceUploadDescription(AbstractTool, QtGui.QRhiTextureSubresourceUploadDescription):
        def __init__(self, *args, **kwargs):
            QtGui.QRhiTextureSubresourceUploadDescription.__init__(self, *args)
            super().__init__(**kwargs)


    class RhiTextureUploadDescription(AbstractTool, QtGui.QRhiTextureUploadDescription):
        def __init__(self, *args, **kwargs):
            QtGui.QRhiTextureUploadDescription.__init__(self, *args)
            super().__init__(**kwargs)


    class RhiTextureUploadEntry(AbstractTool, QtGui.QRhiTextureUploadEntry):
        def __init__(self, *args, **kwargs):
            QtGui.QRhiTextureUploadEntry.__init__(self, *args)
            super().__init__(**kwargs)


    class RhiVertexInputAttribute(AbstractTool, QtGui.QRhiVertexInputAttribute):
        def __init__(self, *args, **kwargs):
            QtGui.QRhiVertexInputAttribute.__init__(self, *args)
            super().__init__(**kwargs)


    class RhiVertexInputBinding(AbstractTool, QtGui.QRhiVertexInputBinding):
        def __init__(self, *args, **kwargs):
            QtGui.QRhiVertexInputBinding.__init__(self, *args)
            super().__init__(**kwargs)


    class RhiVertexInputLayout(AbstractTool, QtGui.QRhiVertexInputLayout):
        def __init__(self, *args, **kwargs):
            QtGui.QRhiVertexInputLayout.__init__(self, *args)
            super().__init__(**kwargs)


    class RhiViewport(AbstractTool, QtGui.QRhiViewport):
        def __init__(self, *args, **kwargs):
            QtGui.QRhiViewport.__init__(self, *args)
            super().__init__(**kwargs)


    class Shader(AbstractTool, QtGui.QShader):
        def __init__(self, *args, **kwargs):
            QtGui.QShader.__init__(self, *args)
            super().__init__(**kwargs)


    class ShaderCode(AbstractTool, QtGui.QShaderCode):
        def __init__(self, *args, **kwargs):
            QtGui.QShaderCode.__init__(self, *args)
            super().__init__(**kwargs)


    class ShaderKey(AbstractTool, QtGui.QShaderKey):
        def __init__(self, *args, **kwargs):
            QtGui.QShaderKey.__init__(self, *args)
            super().__init__(**kwargs)


    class ShaderVersion(AbstractTool, QtGui.QShaderVersion):
        def __init__(self, *args, **kwargs):
            QtGui.QShaderVersion.__init__(self, *args)
            super().__init__(**kwargs)


class StandardItem(AbstractTool, QtGui.QStandardItem):
    def __init__(self, *args, **kwargs):
        QtGui.QStandardItem.__init__(self, *args)
        super().__init__(**kwargs)


class StaticText(AbstractTool, QtGui.QStaticText):
    def __init__(self, *args, **kwargs):
        QtGui.QStaticText.__init__(self, *args)
        super().__init__(**kwargs)


class SurfaceFormat(AbstractTool, QtGui.QSurfaceFormat):
    def __init__(self, *args, **kwargs):
        QtGui.QSurfaceFormat.__init__(self, *args)
        super().__init__(**kwargs)


class TextBlock(AbstractTool, QtGui.QTextBlock):
    def __init__(self, *args, **kwargs):
        QtGui.QTextBlock.__init__(self, *args)
        super().__init__(**kwargs)


class TextBlockFormat(AbstractTool, QtGui.QTextBlockFormat):
    def __init__(self, *args, **kwargs):
        QtGui.QTextBlockFormat.__init__(self, *args)
        super().__init__(**kwargs)


class TextCharFormat(AbstractTool, QtGui.QTextCharFormat):
    def __init__(self, *args, **kwargs):
        QtGui.QTextCharFormat.__init__(self, *args)
        super().__init__(**kwargs)


class TextCursor(AbstractTool, QtGui.QTextCursor):
    def __init__(self, *args, **kwargs):
        QtGui.QTextCursor.__init__(self, *args)
        super().__init__(**kwargs)


class TextDocumentWriter(AbstractTool, QtGui.QTextDocumentWriter):
    def __init__(self, *args, **kwargs):
        QtGui.QTextDocumentWriter.__init__(self, *args)
        super().__init__(**kwargs)


class TextFormat(AbstractTool, QtGui.QTextFormat):
    def __init__(self, *args, **kwargs):
        QtGui.QTextFormat.__init__(self, *args)
        super().__init__(**kwargs)


class TextFrameFormat(AbstractTool, QtGui.QTextFrameFormat):
    def __init__(self, *args, **kwargs):
        QtGui.QTextFrameFormat.__init__(self, *args)
        super().__init__(**kwargs)


class TextImageFormat(AbstractTool, QtGui.QTextImageFormat):
    def __init__(self, *args, **kwargs):
        QtGui.QTextImageFormat.__init__(self, *args)
        super().__init__(**kwargs)


class TextInlineObject(AbstractTool, QtGui.QTextInlineObject):
    def __init__(self, *args, **kwargs):
        QtGui.QTextInlineObject.__init__(self, *args)
        super().__init__(**kwargs)


class TextLayout(AbstractTool, QtGui.QTextLayout):
    def __init__(self, *args, **kwargs):
        QtGui.QTextLayout.__init__(self, *args)
        super().__init__(**kwargs)


class TextLine(AbstractTool, QtGui.QTextLine):
    def __init__(self, *args, **kwargs):
        QtGui.QTextLine.__init__(self, *args)
        super().__init__(**kwargs)


class TextListFormat(AbstractTool, QtGui.QTextListFormat):
    def __init__(self, *args, **kwargs):
        QtGui.QTextListFormat.__init__(self, *args)
        super().__init__(**kwargs)


class TextOption(AbstractTool, QtGui.QTextOption):
    def __init__(self, *args, **kwargs):
        QtGui.QTextOption.__init__(self, *args)
        super().__init__(**kwargs)


class TextTableCell(AbstractTool, QtGui.QTextTableCell):
    def __init__(self, *args, **kwargs):
        QtGui.QTextTableCell.__init__(self, *args)
        super().__init__(**kwargs)


class TextTableCellFormat(AbstractTool, QtGui.QTextTableCellFormat):
    def __init__(self, *args, **kwargs):
        QtGui.QTextTableCellFormat.__init__(self, *args)
        super().__init__(**kwargs)


class TextTableFormat(AbstractTool, QtGui.QTextTableFormat):
    def __init__(self, *args, **kwargs):
        QtGui.QTextTableFormat.__init__(self, *args)
        super().__init__(**kwargs)


class UndoCommand(AbstractTool, QtGui.QUndoCommand):
    def __init__(self, *args, **kwargs):
        QtGui.QUndoCommand.__init__(self, *args)
        super().__init__(**kwargs)


class Vector2D(AbstractTool, QtGui.QVector2D):
    def __init__(self, *args, **kwargs):
        QtGui.QVector2D.__init__(self, *args)
        super().__init__(**kwargs)


class Vector3D(AbstractTool, QtGui.QVector3D):
    def __init__(self, *args, **kwargs):
        QtGui.QVector3D.__init__(self, *args)
        super().__init__(**kwargs)


class Vector4D(AbstractTool, QtGui.QVector4D):
    def __init__(self, *args, **kwargs):
        QtGui.QVector4D.__init__(self, *args)
        super().__init__(**kwargs)
