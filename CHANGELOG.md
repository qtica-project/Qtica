# Changelog

## Unreleased - (Soon!)

### Added

- parent_child_widgets.py example

## 0.1.1 - (2023-11-05)

### Added

- #### PySide6 Built-in Widgets

  - QApplication
  - QPushButton
  - QLabel
  - QFrame
  - QMainWindow
  - QSystemTrayIcon
  - QGraphicsView
  - QWidget
  - QQuickWidget
  - QQuickView
  - QGraphicsOpacityEffect
  - QGraphicsDropShadowEffect
  - QGraphicsColorizeEffect
  - QGraphicsBlurEffect
  - QFormLayout
  - QGridLayout
  - QHBoxLayout
  - QStackedLayout
  - QVBoxLayout

- #### PySide6 Additional Widgets

  - WigglyWidget
  - WaterRippleProgressBar
  - WaterProgressBar
  - ProgressIndicator
  - MovieView
  - MetroCircleProgress
  - ElidingLabel
  - FramelessWindow
  - RoutingWindow
  - TeachingTip
  - SlidingStackedWidget
  - SideBarWidget
  - TerminalWidget
  - NavBarWidget
  - SilentTextDialog
  - LargTextDialog
  - ColourfulProgressBar
  - OutsideNeumorphismEffect
  - InsideNeumorphismEffect
  - FlowLayout
  - ExpandLayout

- #### PySide6 Built-in Core

  - QPropertyAnimation

- #### PySide6 Additional Core
  - StyleAnimation
  - ProgressStyleAnimation
  - Animation

## 0.1.2 - (2023-11-07)

### Added

- Qtica `logo.png`
- version_generator.py example
- status_edge.py example
- resources, and fonts into the `Application` class.
- `tools.Painter class`
- `tools.PaintStatusEdge`
- `widgets.FramelessWindowSizeGrip`

### Changed

- `enums.Sizes.size_hint` -> `enums.Sizes.hint`

### Fixed

- `core.BehaviorDeclarative`, no uid in `__init__` parameters

## 0.1.3 - (2023-11-12)

### Added

- `widgets.ThemeSwitchButton`
- `enums.AbstractIcons` to make enum icons that work with Qtica tools
- `tools.Icon`
- `utils.color.DetectImageColors`, using to get an image colors map.
- `utils.color.get_image_average_color`, get an image rgb color
- `widgets.LineEdit`
- `core.WidgetBase` effect argument.
- `core.AbstractBase` \*\*kwargs, can now accept set value for method.
- `widgets.ScrollArea`
- get_start.py example

### Changed

- `Theme.system_theme` to static method type.
- `effects.*` from ObjectDeclarative class type to `ObjectBase`
- `utils.color.get_hex_from_color` color arg to \*rgb arg

### Fixed

- pixmap error when you try to add `QIcon` to `tools.Icon` with color value.

## 0.1.4 (2023-11-24)

### Added

- extras `icons` modules `elusive` `feather` `fluent` `fontawesome` `material`
- `widgets.FramelessWindowSizeGrip` edge option.
- `utils.methods.qt_corner_to_edge` convert Qt.Corner inputs to Qt.Edge values.
- `widgets.StackedWidget` QStackedWidget built-in PySide6 class
- `widgets.IconWidget`
- `widgets.MaskDialog`

### Fixed

- `widgets.FramelessWindow` window geometry changed when move window.
- `widgets.FramelessWindowSizeGrip` cursor shape for SizeGrip hover.
- `tools.Icon` list index out of range, when used colored icon

### Updated

- `widgets.NavBarButton` it's now subclass from `core.WidgetBase`

## 0.2.0 (2023-12-08)

### Added

- `widgets.HLine`, Horizontal Frame widget.
- `widgets.VLine`, Vertical Frame widget.
- `widgets.ToolButton` PySide6 Built-in QToolButton
- `core.QStyleSheet` restore_qss method to restore last Qss value after update_qss call with save=False.
- `tools.StatusEdgePaint` corner option.
- `widgets.MainWindow`, `widgets.FramelessWindow`, `widgets.RoutingWindow` sys_tray parameter.
- `widgets.Menu`, fork for PySide6.QtWidgets.QMenu.
- `tools.Action` fork for PySide6.QtGui.QAction.
- `utils.colors`
- `core.AbstractBase` `methods` parameter.
- `core.AbstractTool`, `core.ToolBase`
- `core.AbstractIcon`, `core.IconBase`
- `core.AbstractPainter`, `core.PainterBase`

### Removed

- `tools.Painter` `__init__` return parent widget, you can now return from subclasses.
- `core.Return`, we dont't need it any more!

### Updated

- `layouts.HLayout`, and `layouts.VLayout` now you can add `QSpacerItem`, and `QLayoutItem` widget types to children
- `core.QStyleSheet` improve Qss Parser.
- `core.QStyleSheet` qss now accepting json files.
- `widgets.LineEdit` password_mode parameter, add password echo mode support
- `widgets.SlidingStackedWidget` now children parameter support Route

### Fixed

- `tools.Icon` default color value -1, when color is None
- `core.Api.fetch` method NoneType error when fetching `PySide6.QtWidgets.QApplication` class type.

### Changed

- `tools.PaintStatusEdge` to `tools.StatusEdgePaint`
- `tools.ObjectBase` to `tools.QObjectBase`
- `widgets.QuickWidget` parameter `file` to `qml`
- `widgets.QuickView` parameter `file` to `qml`

## 0.2.1 (2023-12-09)

### Added

- `utils.caseconverter`, forking `caseconverter` module to be as built-in

### Changed

- moving pynput from dependencies to extras dependence.

### Removed

- `requirements.txt`, we don't need it anymore, you can use poetry to install requirements.

## 0.3.0 (2024-01-03)

### Changed

- `core.Api.fetch` \type argument has been renamed to qtype
- `widgets.MovieView` has been moved and renamed to `tools.Movie`
- `tools.EnvVar` has been moved to `utils.EnvVar`
- `widgets.Application` list_styles has been renamed to style_list
- `core.WidgetBase` has been renamed to `AbstractWidget`
- `core.ObjectBase` has been renamed to `AbstractQObject`
- `core.BehavioDeclarative` has been renamed to `BehavioDec`
- `core.QStyleSheet` has been moved to `utils.QStyleSheet`
- `core.WidgetDeclarative` has been renamed to `WidgetDec`
- `core.ObjectDeclarative` has been renamed to `QObjectDec`
- `core.TrackingDeclarative` has been renamed to TrackingDec`
- `utils.colors.get_image_average_color` has been renamed to `imageAverageColor`
- `utils.colors.imageAverageColor` return `QColor` type insted `list[int]`
- `utils.colors.get_color_from_hex` has been renamed to `hexToColor`
- `utils.colors.get_hex_from_color` has been renamed to `colorToHex`
- `utils.colors.get_random_color` has been renamed to `randomColor`
- `enums.TeachingTipTailPositions` has been renamed to `TeachingTipTailPos`
- `widgets.ScrollArea` child can know accepted `QLayout` Objects
- `core.AbstractBase.get` has been renamed to `fetch`
- `utils.colors.Contrast.color_type` has been renamed to `color_mode`
- `core.AbstractPainter._repaint` has been renamed to `repaint`
- `core.AbstractPainter._paint` has been renamed to `_paint` 
- `core.AbstractPainter._super_paintEvent` has been renamed to `super_paintEvent` 

### Updated

- `core.AbstractBase` events keyword, now can accept methods without 'Event' suffix
- `enums.EnvVars`, some variables added
- `core.AbstractWidget` - `core.AbstractWidget` Now you can add an event method without writing the 'Event' suffix, and the class will auto-detect the method.
- `utils.Routes` add support for QStackedLayout

### Fixed

- `core.Api.fetch` Improve QObject Finder
- `utils.colors.ImageColors.most_common` change from property to method
- `core.AbstractDec` saving uid for objects how was have `objectName` method.

### Added

- supporting for PySide6.{5,6}.x versions
- `widgets.IconWidget` support `QMovie` animation image.
- `core.AbstractWidget` long_press Signal
- `core.AbstractBase.enable_event_stack`, know you can stack a widget event.
- `sys_tray.py` to examples folder.
- `stack.py` to examples folder.
- `core.AbstractIcons`
- `core.AbstractTool`
- `core.AbstractPainter`
- `core.AbstractDec`
- `utils.theme_detect` forked to be Qtica built-in module
- `layouts.ColumnLayout`
- `layouts.ColumnLayoutItemWrapper`
- `layouts.RowLayout`
- `layouts.RowLayoutItemWrapper`
- `layouts.BorderLayout`
- `layouts.BorderLayoutItemWrapper`
- `core.Api.dec_fetch`
- `enums.Theme`
- `services.showDialog`
- `services.TakeScreenShot`
- `services.UrlOpen`
- `tools.SystemTray`
- `tools.Action`
- `widgets.Stack`
- `tools.Pen`
- `painters.CircularProgressPaint`
- `core.AbstractDialog`
- `widgets.dialogs.TeachingTipDialog`
- `tools.action.LinePasswordAction`


## 0.3.1 (2024-01-09)

### Added

- `animations.ParallelAnimationGroup`
- `animations.SequentialAnimationGroup`
- `tools.Brush`

### Changed

- `Qtica.animation` has been renamed to `Qtica.animations`
- `tools.painters` has been moved to the main directory of Qtica `Qtica.painters`
- `layouts.GridLayoutItemWrapper` has been moved to `tools.wrappers.GridLayoutWrapper`
- `layouts.VLayoutItemWrapper` has been moved to `tools.wrappers.VLayoutWrapper`
- `layouts.HLayoutItemWrapper` has been moved to `tools.wrappers.HLayoutWrapper`
- `layouts.RowLayoutItemWrapper` has been moved to `tools.wrappers.RowLayoutWrapper`
- `layouts.ColumnLayoutItemWrapper` has been moved to `tools.wrappers.ColumnLayoutWrapper`
- `layouts.FormLayoutItemWrapper` has been moved to `tools.wrappers.FormLayoutWrapper`
- `layouts.BorderLayoutItemWrapper` has been moved to `tools.wrappers.BorderLayoutWrapper`
- `tools.AbstractConfig` has been moved to `core.AbstractConfig`
- `widgets.container` has been renamed to `widgets.frame`

### Removed

- `utils.colors`
- `enums.teaching_tip_tails`
- `enums.animation`
- `enums.clipboard`
- `enums.smooth_scroll`


## 0.3.2 (2024-01-13)

### Added

- `widgets.dialogs.MaskDialog` close button title bar.
- `widgets.SpinBox`
- `widgets.DoubleSpinBox`
- `services.parse_css_linear_gradient`
- `utils.maths.deg_to_coordinates`
- `core.AbstractBase` handle add Methods in **kwargs
- #### `tools.qtgui`
  - ActionGroup
  - Clipboard
  - DoubleValidator
  - Drag
  - GuiApplication
  - InputDevice
  - InputMethod
  - IntValidator
  - OffscreenSurface
  - OpenGLContext
  - OpenGLContextGroup
  - PaintDeviceWindow
  - PdfWriter
  - PointingDevice
  - PyTextObject
  - RasterWindow
  - RegularExpressionValidator
  - Screen
  - SessionManager
  - Shortcut
  - StandardItemModel
  - StyleHints
  - SyntaxHighlighter
  - TextBlockGroup
  - TextDocument
  - TextFrame
  - TextList
  - TextObject
  - TextTable
  - UndoGroup
  - UndoStack
  - Validator
  - Window
  - BackingStore
  - Bitmap
  - ColorSpace
  - ConicalGradient
  - Cursor
  - DesktopServices
  - Font
  - GlyphRun
  - Gradient
  - Image
  - ImageIOHandler
  - ImageReader
  - ImageWriter
  - LinearGradient
  - PageLayout
  - PagedPaintDevice
  - PaintEngine
  - Painter
  - PainterPathStroker
  - Palette
  - Pen
  - Picture
  - Pixmap
  - Quaternion
  - RadialGradient
  - Rgba64
  - RhiBuffer
  - RhiColorAttachment
  - RhiCommandBuffer
  - RhiComputePipeline
  - RhiDepthStencilClearValue
  - RhiGraphicsPipeline
  - RhiReadbackDescription
  - RhiRenderBuffer
  - RhiRenderTarget
  - RhiSampler
  - RhiScissor
  - RhiShaderResourceBindings
  - RhiShaderStage
  - RhiSwapChain
  - RhiSwapChainRenderTarget
  - RhiTexture
  - RhiTextureCopyDescription
  - RhiTextureRenderTarget
  - RhiTextureRenderTargetDescription
  - RhiTextureSubresourceUploadDescription
  - RhiTextureUploadDescription
  - RhiTextureUploadEntry
  - RhiVertexInputAttribute
  - RhiVertexInputBinding
  - RhiVertexInputLayout
  - RhiViewport
  - Shader
  - ShaderCode
  - ShaderKey
  - ShaderVersion
  - StandardItem
  - StaticText
  - SurfaceFormat
  - TextBlock
  - TextBlockFormat
  - TextCharFormat
  - TextCursor
  - TextDocumentWriter
  - TextFormat
  - TextFrameFormat
  - TextImageFormat
  - TextInlineObject
  - TextLayout
  - TextLine
  - TextListFormat
  - TextOption
  - TextTableCell
  - TextTableCellFormat
  - TextTableFormat
  - UndoCommand
  - Vector2D
  - Vector3D
  - Vector4D

  #### `tools.qtcore`
  - QAnimationGroup
  - QBuffer
  - QConcatenateTablesProxyModel
  - QCoreApplication
  - QEventLoop
  - QFileDevice
  - QFileSelector
  - QFileSystemWatcher
  - QIODevice
  - QIdentityProxyModel
  - QItemSelectionModel
  - QLibrary
  - QMimeData
  - QPauseAnimation
  - QPluginLoader
  - QProcess
  - QSaveFile
  - QSharedMemory
  - QSignalMapper
  - QSocketNotifier
  - QSortFilterProxyModel
  - QStringListModel
  - QTemporaryFile
  - QThread
  - QThreadPool
  - QTimeLine
  - QTimer
  - QTranslator
  - QTransposeProxyModel
  - QVariantAnimation

- #### `widgets`
  - AbstractButton
  - AbstractItemView
  - AbstractScrollArea
  - AbstractSlider
  - AbstractSpinBox
  - CalendarWidget
  - CheckBox
  - ColorDialog
  - ColumnView
  - ComboBox
  - CommandLinkButton
  - DateEdit
  - DateTimeEdit
  - Dial
  - Dialog
  - DialogButtonBox
  - DockWidget
  - DoubleSpinBox
  - ErrorMessage
  - FileDialog
  - FocusFrame
  - FontComboBox
  - FontDialog
  - GraphicsProxyWidget
  - GraphicsView
  - GraphicsWidget
  - GroupBox
  - HeaderView
  - InputDialog
  - KeySequenceEdit
  - LCDNumber
  - ListView
  - ListWidget
  - MdiArea
  - MdiSubWindow
  - MenuBar
  - MessageBox
  - PlainTextEdit
  - ProgressBar
  - ProgressDialog
  - RadioButton
  - RubberBand
  - ScrollBar
  - Slider
  - SpinBox
  - SplashScreen
  - Splitter
  - SplitterHandle
  - StatusBar
  - TabBar
  - TabWidget
  - TableView
  - TableWidget
  - TextBrowser
  - TextEdit
  - TimeEdit
  - ToolBar
  - ToolBox
  - TreeView
  - TreeWidget
  - UndoView
  - Wizard
  - WizardPage

### Updated

- `widgets.dialogs.TeachingTipDialog` improved
- `core.AbstractDialog` improved
- `tools.Settings` improved system detecting
- `tools.CopyProgress` improved
- `core.AbstractBase` improved

### Changed

- `tools.Alignment` has been moved to `utils.Alignment`
- `tools.Modifiers` has been moved to `utils.Modifiers`
- `core.AbstractWidget` 'long_press' signal has been renamed to long_pressed

### Fixed

- `tools.Settings` **_set_default_path**, when system equal to windows


## 0.3.3 (2024-01-14)

### Added

- `widgets.window.BaseWindow`

### Fixed

- `widgets.ToolButton` requires a 'PySide6.QtWidgets.QPushButton' object but received a 'ToolButton'
- `widgets.FramelessWindow` '__init__' method of object's base class (FramelessWindow) not called.


## 0.4.0 ()

### Added

- `widgets.icon_widget` setIcon method.
- `core.MArgs`
- `widgets.GroupBox` child keyword argument
- #### `tools.qtcore.tools`
  - QBitArray
  - QByteArray
  - QByteArrayMatcher
  - QCollator
  - QDataStream
  - QDate
  - QDateTime
  - QDeadlineTimer
  - QDir
  - QEasingCurve
  - QFileInfo
  - QFutureInterfaceBase
  - QJsonDocument
  - QLine
  - QLineF
  - QLocale
  - QLockFile
  - QLoggingCategory
  - QMargins
  - QMarginsF
  - QNativeIpcKey
  - QPoint
  - QPointF
  - QRect
  - QRectF
  - QRegularExpression
  - QSize
  - QSizeF
  - QSystemSemaphore
  - QTextStream
  - QTime
  - QUrl
  - QUrlQuery
  - QXmlStreamReader
  - QXmlStreamWriter

### Fixed

- `core.AbstractBase` repeating call of [add]Method when inserting to it Iterable value.

### Changed

- `utils.Args` has been moved to `core.Args`
- `utils.Func` has been moved to `core.Func`
- `utils.Routes` has been moved to `core.Routes`
- `utils.QStyleSheet` has been moved to `core.QStyleSheet`
- `utils.exceptionHandler` has been renamed and moved to `core.TryExc`