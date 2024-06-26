from PySide6.QtCore import QObject
from PySide6 import QtWidgets
from enum import Enum


class Widgets(Enum):
    any: QObject = QObject
    abstract_button: QObject = QtWidgets.QAbstractButton
    abstract_graphics_shape_item: QObject = QtWidgets.QAbstractGraphicsShapeItem
    abstract_item_delegate: QObject = QtWidgets.QAbstractItemDelegate
    abstract_item_view: QObject = QtWidgets.QAbstractItemView
    abstract_scroll_area: QObject = QtWidgets.QAbstractScrollArea
    abstract_slider: QObject = QtWidgets.QAbstractSlider
    abstract_spin_box: QObject = QtWidgets.QAbstractSpinBox
    accessible_widget: QObject = QtWidgets.QAccessibleWidget
    application: QObject = QtWidgets.QApplication
    box_layout: QObject = QtWidgets.QBoxLayout
    button_group: QObject = QtWidgets.QButtonGroup
    calendar_widget: QObject = QtWidgets.QCalendarWidget
    check_box: QObject = QtWidgets.QCheckBox
    color_dialog: QObject = QtWidgets.QColorDialog
    colormap: QObject = QtWidgets.QColormap
    column_view: QObject = QtWidgets.QColumnView
    combo_box: QObject = QtWidgets.QComboBox
    command_link_button: QObject = QtWidgets.QCommandLinkButton
    common_style: QObject = QtWidgets.QCommonStyle
    completer: QObject = QtWidgets.QCompleter
    data_widget_mapper: QObject = QtWidgets.QDataWidgetMapper
    date_edit: QObject = QtWidgets.QDateEdit
    date_time_edit: QObject = QtWidgets.QDateTimeEdit
    dial: QObject = QtWidgets.QDial
    dialog: QObject = QtWidgets.QDialog
    dialog_button_box: QObject = QtWidgets.QDialogButtonBox
    dock_widget: QObject = QtWidgets.QDockWidget
    double_spin_box: QObject = QtWidgets.QDoubleSpinBox
    error_message: QObject = QtWidgets.QErrorMessage
    file_dialog: QObject = QtWidgets.QFileDialog
    file_icon_provider: QObject = QtWidgets.QFileIconProvider
    file_system_model: QObject = QtWidgets.QFileSystemModel
    focus_frame: QObject = QtWidgets.QFocusFrame
    font_combo_box: QObject = QtWidgets.QFontComboBox
    font_dialog: QObject = QtWidgets.QFontDialog
    form_layout: QObject = QtWidgets.QFormLayout
    frame: QObject = QtWidgets.QFrame
    gesture: QObject = QtWidgets.QGesture
    gesture_event: QObject = QtWidgets.QGestureEvent
    gesture_recognizer: QObject = QtWidgets.QGestureRecognizer
    graphics_anchor: QObject = QtWidgets.QGraphicsAnchor
    graphics_anchor_layout: QObject = QtWidgets.QGraphicsAnchorLayout
    graphics_blur_effect: QObject = QtWidgets.QGraphicsBlurEffect
    graphics_colorize_effect: QObject = QtWidgets.QGraphicsColorizeEffect
    graphics_drop_shadow_effect: QObject = QtWidgets.QGraphicsDropShadowEffect
    graphics_effect: QObject = QtWidgets.QGraphicsEffect
    graphics_ellipse_item: QObject = QtWidgets.QGraphicsEllipseItem
    graphics_grid_layout: QObject = QtWidgets.QGraphicsGridLayout
    graphics_item: QObject = QtWidgets.QGraphicsItem
    graphics_item_animation: QObject = QtWidgets.QGraphicsItemAnimation
    graphics_item_group: QObject = QtWidgets.QGraphicsItemGroup
    graphics_layout: QObject = QtWidgets.QGraphicsLayout
    graphics_layout_item: QObject = QtWidgets.QGraphicsLayoutItem
    graphics_line_item: QObject = QtWidgets.QGraphicsLineItem
    graphics_linear_layout: QObject = QtWidgets.QGraphicsLinearLayout
    graphics_object: QObject = QtWidgets.QGraphicsObject
    graphics_opacity_effect: QObject = QtWidgets.QGraphicsOpacityEffect
    graphics_path_item: QObject = QtWidgets.QGraphicsPathItem
    graphics_pixmap_item: QObject = QtWidgets.QGraphicsPixmapItem
    graphics_polygon_item: QObject = QtWidgets.QGraphicsPolygonItem
    graphics_proxy_widget: QObject = QtWidgets.QGraphicsProxyWidget
    graphics_rect_item: QObject = QtWidgets.QGraphicsRectItem
    graphics_rotation: QObject = QtWidgets.QGraphicsRotation
    graphics_scale: QObject = QtWidgets.QGraphicsScale
    graphics_scene: QObject = QtWidgets.QGraphicsScene
    graphics_scene_context_menu_event: QObject = QtWidgets.QGraphicsSceneContextMenuEvent
    graphics_scene_drag_drop_event: QObject = QtWidgets.QGraphicsSceneDragDropEvent
    graphics_scene_event: QObject = QtWidgets.QGraphicsSceneEvent
    graphics_scene_help_event: QObject = QtWidgets.QGraphicsSceneHelpEvent
    graphics_scene_hover_event: QObject = QtWidgets.QGraphicsSceneHoverEvent
    graphics_scene_mouse_event: QObject = QtWidgets.QGraphicsSceneMouseEvent
    graphics_scene_move_event: QObject = QtWidgets.QGraphicsSceneMoveEvent
    graphics_scene_resize_event: QObject = QtWidgets.QGraphicsSceneResizeEvent
    graphics_scene_wheel_event: QObject = QtWidgets.QGraphicsSceneWheelEvent
    graphics_simple_text_item: QObject = QtWidgets.QGraphicsSimpleTextItem
    graphics_text_item: QObject = QtWidgets.QGraphicsTextItem
    graphics_transform: QObject = QtWidgets.QGraphicsTransform
    graphics_view: QObject = QtWidgets.QGraphicsView
    graphics_widget: QObject = QtWidgets.QGraphicsWidget
    grid_layout: QObject = QtWidgets.QGridLayout
    group_box: QObject = QtWidgets.QGroupBox
    hbox_layout: QObject = QtWidgets.QHBoxLayout
    header_view: QObject = QtWidgets.QHeaderView
    input_dialog: QObject = QtWidgets.QInputDialog
    int_list: QObject = QtWidgets.QIntList
    item_delegate: QObject = QtWidgets.QItemDelegate
    item_editor_creator_base: QObject = QtWidgets.QItemEditorCreatorBase
    item_editor_factory: QObject = QtWidgets.QItemEditorFactory
    key_sequence_edit: QObject = QtWidgets.QKeySequenceEdit
    lcdnumber: QObject = QtWidgets.QLCDNumber
    label: QObject = QtWidgets.QLabel
    layout: QObject = QtWidgets.QLayout
    layout_item: QObject = QtWidgets.QLayoutItem
    line_edit: QObject = QtWidgets.QLineEdit
    list_view: QObject = QtWidgets.QListView
    list_widget: QObject = QtWidgets.QListWidget
    list_widget_item: QObject = QtWidgets.QListWidgetItem
    main_window: QObject = QtWidgets.QMainWindow
    mdi_area: QObject = QtWidgets.QMdiArea
    mdi_sub_window: QObject = QtWidgets.QMdiSubWindow
    menu: QObject = QtWidgets.QMenu
    menu_bar: QObject = QtWidgets.QMenuBar
    message_box: QObject = QtWidgets.QMessageBox
    pan_gesture: QObject = QtWidgets.QPanGesture
    pinch_gesture: QObject = QtWidgets.QPinchGesture
    plain_text_document_layout: QObject = QtWidgets.QPlainTextDocumentLayout
    plain_text_edit: QObject = QtWidgets.QPlainTextEdit
    point_flist: QObject = QtWidgets.QPointFList
    point_list: QObject = QtWidgets.QPointList
    progress_bar: QObject = QtWidgets.QProgressBar
    progress_dialog: QObject = QtWidgets.QProgressDialog
    proxy_style: QObject = QtWidgets.QProxyStyle
    push_button: QObject = QtWidgets.QPushButton
    radio_button: QObject = QtWidgets.QRadioButton
    rubber_band: QObject = QtWidgets.QRubberBand
    scroll_area: QObject = QtWidgets.QScrollArea
    scroll_bar: QObject = QtWidgets.QScrollBar
    scroller: QObject = QtWidgets.QScroller
    scroller_properties: QObject = QtWidgets.QScrollerProperties
    size_grip: QObject = QtWidgets.QSizeGrip
    size_policy: QObject = QtWidgets.QSizePolicy
    slider: QObject = QtWidgets.QSlider
    spacer_item: QObject = QtWidgets.QSpacerItem
    spin_box: QObject = QtWidgets.QSpinBox
    splash_screen: QObject = QtWidgets.QSplashScreen
    splitter: QObject = QtWidgets.QSplitter
    splitter_handle: QObject = QtWidgets.QSplitterHandle
    stacked_layout: QObject = QtWidgets.QStackedLayout
    stacked_widget: QObject = QtWidgets.QStackedWidget
    status_bar: QObject = QtWidgets.QStatusBar
    style: QObject = QtWidgets.QStyle
    style_factory: QObject = QtWidgets.QStyleFactory
    style_hint_return: QObject = QtWidgets.QStyleHintReturn
    style_hint_return_mask: QObject = QtWidgets.QStyleHintReturnMask
    style_hint_return_variant: QObject = QtWidgets.QStyleHintReturnVariant
    style_option: QObject = QtWidgets.QStyleOption
    style_option_button: QObject = QtWidgets.QStyleOptionButton
    style_option_combo_box: QObject = QtWidgets.QStyleOptionComboBox
    style_option_complex: QObject = QtWidgets.QStyleOptionComplex
    style_option_dock_widget: QObject = QtWidgets.QStyleOptionDockWidget
    style_option_focus_rect: QObject = QtWidgets.QStyleOptionFocusRect
    style_option_frame: QObject = QtWidgets.QStyleOptionFrame
    style_option_graphics_item: QObject = QtWidgets.QStyleOptionGraphicsItem
    style_option_group_box: QObject = QtWidgets.QStyleOptionGroupBox
    style_option_header: QObject = QtWidgets.QStyleOptionHeader
    style_option_header_v2: QObject = QtWidgets.QStyleOptionHeaderV2
    style_option_menu_item: QObject = QtWidgets.QStyleOptionMenuItem
    style_option_progress_bar: QObject = QtWidgets.QStyleOptionProgressBar
    style_option_rubber_band: QObject = QtWidgets.QStyleOptionRubberBand
    style_option_size_grip: QObject = QtWidgets.QStyleOptionSizeGrip
    style_option_slider: QObject = QtWidgets.QStyleOptionSlider
    style_option_spin_box: QObject = QtWidgets.QStyleOptionSpinBox
    style_option_tab: QObject = QtWidgets.QStyleOptionTab
    style_option_tab_bar_base: QObject = QtWidgets.QStyleOptionTabBarBase
    style_option_tab_widget_frame: QObject = QtWidgets.QStyleOptionTabWidgetFrame
    style_option_title_bar: QObject = QtWidgets.QStyleOptionTitleBar
    style_option_tool_bar: QObject = QtWidgets.QStyleOptionToolBar
    style_option_tool_box: QObject = QtWidgets.QStyleOptionToolBox
    style_option_tool_button: QObject = QtWidgets.QStyleOptionToolButton
    style_option_view_item: QObject = QtWidgets.QStyleOptionViewItem
    style_painter: QObject = QtWidgets.QStylePainter
    styled_item_delegate: QObject = QtWidgets.QStyledItemDelegate
    swipe_gesture: QObject = QtWidgets.QSwipeGesture
    system_tray_icon: QObject = QtWidgets.QSystemTrayIcon
    tab_bar: QObject = QtWidgets.QTabBar
    tab_widget: QObject = QtWidgets.QTabWidget
    table_view: QObject = QtWidgets.QTableView
    table_widget: QObject = QtWidgets.QTableWidget
    table_widget_item: QObject = QtWidgets.QTableWidgetItem
    table_widget_selection_range: QObject = QtWidgets.QTableWidgetSelectionRange
    tap_and_hold_gesture: QObject = QtWidgets.QTapAndHoldGesture
    tap_gesture: QObject = QtWidgets.QTapGesture
    text_browser: QObject = QtWidgets.QTextBrowser
    text_edit: QObject = QtWidgets.QTextEdit
    tile_rules: QObject = QtWidgets.QTileRules
    time_edit: QObject = QtWidgets.QTimeEdit
    tool_bar: QObject = QtWidgets.QToolBar
    tool_box: QObject = QtWidgets.QToolBox
    tool_button: QObject = QtWidgets.QToolButton
    tool_tip: QObject = QtWidgets.QToolTip
    tree_view: QObject = QtWidgets.QTreeView
    tree_widget: QObject = QtWidgets.QTreeWidget
    tree_widget_item: QObject = QtWidgets.QTreeWidgetItem
    tree_widget_item_iterator: QObject = QtWidgets.QTreeWidgetItemIterator
    undo_view: QObject = QtWidgets.QUndoView
    vbox_layout: QObject = QtWidgets.QVBoxLayout
    whats_this: QObject = QtWidgets.QWhatsThis
    widget: QObject = QtWidgets.QWidget
    widget_action: QObject = QtWidgets.QWidgetAction
    widget_item: QObject = QtWidgets.QWidgetItem
    wizard: QObject = QtWidgets.QWizard
    wizard_page: QObject = QtWidgets.QWizardPage
