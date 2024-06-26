from PySide6 import QtCore
from enum import Enum, auto


class Signals(Enum):
    about_to_activate: QtCore.Signal = auto()
    about_to_hide: QtCore.Signal = auto()
    about_to_quit: QtCore.Signal = auto()
    about_to_show: QtCore.Signal = auto()
    accepted: QtCore.Signal = auto()
    action_triggered: QtCore.Signal = auto()
    activated: QtCore.Signal = auto()
    allowed_areas_changed: QtCore.Signal = auto()
    anchor_clicked: QtCore.Signal = auto()
    angle_changed: QtCore.Signal = auto()
    application_display_name_changed: QtCore.Signal = auto()
    application_name_changed: QtCore.Signal = auto()
    application_state_changed: QtCore.Signal = auto()
    application_version_changed: QtCore.Signal = auto()
    axis_changed: QtCore.Signal = auto()
    backward_available: QtCore.Signal = auto()
    block_count_changed: QtCore.Signal = auto()
    blur_hints_changed: QtCore.Signal = auto()
    blur_radius_changed: QtCore.Signal = auto()
    button_clicked: QtCore.Signal = auto()
    button_pressed: QtCore.Signal = auto()
    button_released: QtCore.Signal = auto()
    button_toggled: QtCore.Signal = auto()
    canceled: QtCore.Signal = auto()
    cell_activated: QtCore.Signal = auto()
    cell_changed: QtCore.Signal = auto()
    cell_clicked: QtCore.Signal = auto()
    cell_double_clicked: QtCore.Signal = auto()
    cell_entered: QtCore.Signal = auto()
    cell_pressed: QtCore.Signal = auto()
    changed: QtCore.Signal = auto()
    checkable_changed: QtCore.Signal = auto()
    children_changed: QtCore.Signal = auto()
    clicked: QtCore.Signal = auto()
    close_editor: QtCore.Signal = auto()
    collapsed: QtCore.Signal = auto()
    color_changed: QtCore.Signal = auto()
    color_selected: QtCore.Signal = auto()
    columns_about_to_be_inserted: QtCore.Signal = auto()
    columns_about_to_be_moved: QtCore.Signal = auto()
    columns_about_to_be_removed: QtCore.Signal = auto()
    columns_inserted: QtCore.Signal = auto()
    columns_moved: QtCore.Signal = auto()
    columns_removed: QtCore.Signal = auto()
    commit_data: QtCore.Signal = auto()
    commit_data_request: QtCore.Signal = auto()
    complete_changed: QtCore.Signal = auto()
    copy_available: QtCore.Signal = auto()
    current_cell_changed: QtCore.Signal = auto()
    current_changed: QtCore.Signal = auto()
    current_char_format_changed: QtCore.Signal = auto()
    current_color_changed: QtCore.Signal = auto()
    current_font_changed: QtCore.Signal = auto()
    current_id_changed: QtCore.Signal = auto()
    current_index_changed: QtCore.Signal = auto()
    current_item_changed: QtCore.Signal = auto()
    current_page_changed: QtCore.Signal = auto()
    current_row_changed: QtCore.Signal = auto()
    current_text_changed: QtCore.Signal = auto()
    current_url_changed: QtCore.Signal = auto()
    cursor_position_changed: QtCore.Signal = auto()
    custom_button_clicked: QtCore.Signal = auto()
    custom_context_menu_requested: QtCore.Signal = auto()
    data_changed: QtCore.Signal = auto()
    date_changed: QtCore.Signal = auto()
    date_time_changed: QtCore.Signal = auto()
    destroyed: QtCore.Signal = auto()
    directory_entered: QtCore.Signal = auto()
    directory_loaded: QtCore.Signal = auto()
    directory_url_entered: QtCore.Signal = auto()
    dock_location_changed: QtCore.Signal = auto()
    document_size_changed: QtCore.Signal = auto()
    double_clicked: QtCore.Signal = auto()
    double_value_changed: QtCore.Signal = auto()
    double_value_selected: QtCore.Signal = auto()
    edit_text_changed: QtCore.Signal = auto()
    editing_finished: QtCore.Signal = auto()
    enabled_changed: QtCore.Signal = auto()
    entered: QtCore.Signal = auto()
    expanded: QtCore.Signal = auto()
    features_changed: QtCore.Signal = auto()
    file_renamed: QtCore.Signal = auto()
    file_selected: QtCore.Signal = auto()
    files_selected: QtCore.Signal = auto()
    filter_selected: QtCore.Signal = auto()
    finished: QtCore.Signal = auto()
    focus_changed: QtCore.Signal = auto()
    focus_item_changed: QtCore.Signal = auto()
    focus_object_changed: QtCore.Signal = auto()
    focus_window_changed: QtCore.Signal = auto()
    font_changed: QtCore.Signal = auto()
    font_database_changed: QtCore.Signal = auto()
    font_selected: QtCore.Signal = auto()
    forward_available: QtCore.Signal = auto()
    geometries_changed: QtCore.Signal = auto()
    geometry_changed: QtCore.Signal = auto()
    header_data_changed: QtCore.Signal = auto()
    height_changed: QtCore.Signal = auto()
    help_requested: QtCore.Signal = auto()
    highlighted: QtCore.Signal = auto()
    history_changed: QtCore.Signal = auto()
    hovered: QtCore.Signal = auto()
    icon_size_changed: QtCore.Signal = auto()
    id_clicked: QtCore.Signal = auto()
    id_pressed: QtCore.Signal = auto()
    id_released: QtCore.Signal = auto()
    id_toggled: QtCore.Signal = auto()
    indexes_moved: QtCore.Signal = auto()
    input_rejected: QtCore.Signal = auto()
    int_value_changed: QtCore.Signal = auto()
    int_value_selected: QtCore.Signal = auto()
    item_activated: QtCore.Signal = auto()
    item_changed: QtCore.Signal = auto()
    item_clicked: QtCore.Signal = auto()
    item_collapsed: QtCore.Signal = auto()
    item_double_clicked: QtCore.Signal = auto()
    item_entered: QtCore.Signal = auto()
    item_expanded: QtCore.Signal = auto()
    item_pressed: QtCore.Signal = auto()
    item_selection_changed: QtCore.Signal = auto()
    key_sequence_changed: QtCore.Signal = auto()
    last_window_closed: QtCore.Signal = auto()
    layout_about_to_be_changed: QtCore.Signal = auto()
    layout_changed: QtCore.Signal = auto()
    layout_direction_changed: QtCore.Signal = auto()
    link_activated: QtCore.Signal = auto()
    link_hovered: QtCore.Signal = auto()
    message_changed: QtCore.Signal = auto()
    message_clicked: QtCore.Signal = auto()
    model_about_to_be_reset: QtCore.Signal = auto()
    model_reset: QtCore.Signal = auto()
    modification_changed: QtCore.Signal = auto()
    movable_changed: QtCore.Signal = auto()
    object_name_changed: QtCore.Signal = auto()
    offset_changed: QtCore.Signal = auto()
    opacity_changed: QtCore.Signal = auto()
    opacity_mask_changed: QtCore.Signal = auto()
    organization_domain_changed: QtCore.Signal = auto()
    organization_name_changed: QtCore.Signal = auto()
    orientation_changed: QtCore.Signal = auto()
    origin_changed: QtCore.Signal = auto()
    overflow: QtCore.Signal = auto()
    page_added: QtCore.Signal = auto()
    page_count_changed: QtCore.Signal = auto()
    page_removed: QtCore.Signal = auto()
    palette_changed: QtCore.Signal = auto()
    parent_changed: QtCore.Signal = auto()
    pressed: QtCore.Signal = auto()
    primary_screen_changed: QtCore.Signal = auto()
    range_changed: QtCore.Signal = auto()
    redo_available: QtCore.Signal = auto()
    rejected: QtCore.Signal = auto()
    released: QtCore.Signal = auto()
    return_pressed: QtCore.Signal = auto()
    root_path_changed: QtCore.Signal = auto()
    rotation_changed: QtCore.Signal = auto()
    rows_about_to_be_inserted: QtCore.Signal = auto()
    rows_about_to_be_moved: QtCore.Signal = auto()
    rows_about_to_be_removed: QtCore.Signal = auto()
    rows_inserted: QtCore.Signal = auto()
    rows_moved: QtCore.Signal = auto()
    rows_removed: QtCore.Signal = auto()
    rubber_band_changed: QtCore.Signal = auto()
    save_state_request: QtCore.Signal = auto()
    scale_changed: QtCore.Signal = auto()
    scene_rect_changed: QtCore.Signal = auto()
    screen_added: QtCore.Signal = auto()
    screen_removed: QtCore.Signal = auto()
    scroller_properties_changed: QtCore.Signal = auto()
    section_clicked: QtCore.Signal = auto()
    section_count_changed: QtCore.Signal = auto()
    section_double_clicked: QtCore.Signal = auto()
    section_entered: QtCore.Signal = auto()
    section_handle_double_clicked: QtCore.Signal = auto()
    section_moved: QtCore.Signal = auto()
    section_pressed: QtCore.Signal = auto()
    section_resized: QtCore.Signal = auto()
    selection_changed: QtCore.Signal = auto()
    size_hint_changed: QtCore.Signal = auto()
    slider_moved: QtCore.Signal = auto()
    slider_pressed: QtCore.Signal = auto()
    slider_released: QtCore.Signal = auto()
    sort_indicator_changed: QtCore.Signal = auto()
    sort_indicator_clearable_changed: QtCore.Signal = auto()
    source_changed: QtCore.Signal = auto()
    splitter_moved: QtCore.Signal = auto()
    state_changed: QtCore.Signal = auto()
    strength_changed: QtCore.Signal = auto()
    sub_window_activated: QtCore.Signal = auto()
    tab_bar_clicked: QtCore.Signal = auto()
    tab_bar_double_clicked: QtCore.Signal = auto()
    tab_close_requested: QtCore.Signal = auto()
    tab_moved: QtCore.Signal = auto()
    tabified_dock_widget_activated: QtCore.Signal = auto()
    text_activated: QtCore.Signal = auto()
    text_changed: QtCore.Signal = auto()
    text_edited: QtCore.Signal = auto()
    text_highlighted: QtCore.Signal = auto()
    text_value_changed: QtCore.Signal = auto()
    text_value_selected: QtCore.Signal = auto()
    time_changed: QtCore.Signal = auto()
    toggled: QtCore.Signal = auto()
    tool_button_style_changed: QtCore.Signal = auto()
    top_level_changed: QtCore.Signal = auto()
    triggered: QtCore.Signal = auto()
    undo_available: QtCore.Signal = auto()
    update: QtCore.Signal = auto()
    update_block: QtCore.Signal = auto()
    update_preview_widget: QtCore.Signal = auto()
    update_request: QtCore.Signal = auto()
    url_selected: QtCore.Signal = auto()
    urls_selected: QtCore.Signal = auto()
    user_date_changed: QtCore.Signal = auto()
    user_time_changed: QtCore.Signal = auto()
    value_changed: QtCore.Signal = auto()
    viewport_entered: QtCore.Signal = auto()
    visibility_changed: QtCore.Signal = auto()
    visible_changed: QtCore.Signal = auto()
    widget_removed: QtCore.Signal = auto()
    width_changed: QtCore.Signal = auto()
    window_icon_changed: QtCore.Signal = auto()
    window_icon_text_changed: QtCore.Signal = auto()
    window_state_changed: QtCore.Signal = auto()
    window_title_changed: QtCore.Signal = auto()
    x_changed: QtCore.Signal = auto()
    x_scale_changed: QtCore.Signal = auto()
    y_changed: QtCore.Signal = auto()
    y_scale_changed: QtCore.Signal = auto()
    z_changed: QtCore.Signal = auto()
    z_scale_changed: QtCore.Signal = auto()
