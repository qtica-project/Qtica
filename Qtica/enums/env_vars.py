from enum import Enum


class EnvVars(Enum):
    enable_highdpi_scaling: str = "QT_ENABLE_HIGHDPI_SCALING"
    scale_factor: str = "QT_SCALE_FACTOR"
    quick_controls_style: str = "QT_QUICK_CONTROLS_STYLE"
    quick_controls_fallback_style: str = "QT_QUICK_CONTROLS_FALLBACK_STYLE"
    quick_controls_conf: str = "QT_QUICK_CONTROLS_CONF"
    quick_controls_hover_enabled: str = "QT_QUICK_CONTROLS_HOVER_ENABLED"
    quick_controls_imagine_path: str = "QT_QUICK_CONTROLS_IMAGINE_PATH"
    quick_controls_imagine_smooth: str = "QT_QUICK_CONTROLS_IMAGINE_SMOOTH"
    quick_controls_material_theme: str = "QT_QUICK_CONTROLS_MATERIAL_THEME"
    quick_controls_material_variant: str = "QT_QUICK_CONTROLS_MATERIAL_VARIANT"
    quick_controls_material_accent: str = "QT_QUICK_CONTROLS_MATERIAL_ACCENT"
    quick_controls_material_primary: str = "QT_QUICK_CONTROLS_MATERIAL_PRIMARY"
    quick_controls_material_foreground: str = "QT_QUICK_CONTROLS_MATERIAL_FOREGROUND"
    quick_controls_material_background: str = "QT_QUICK_CONTROLS_MATERIAL_BACKGROUND"
    quick_controls_universal_theme: str = "QT_QUICK_CONTROLS_UNIVERSAL_THEME"
    quick_controls_universal_accent: str = "QT_QUICK_CONTROLS_UNIVERSAL_ACCENT"
    quick_controls_universal_foreground: str = "QT_QUICK_CONTROLS_UNIVERSAL_FOREGROUND"
    quick_controls_universal_background: str = "QT_QUICK_CONTROLS_UNIVERSAL_BACKGROUND"
    qpa_platform: str = "QT_QPA_PLATFORM"
    im_module: str = "QT_IM_MODULE"