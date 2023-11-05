#!/usr/bin/python3

class WindowsInit:
    def __init__(self) -> None:
        ...

    def set_app_id(self, 
                   company: str, 
                   product: str, 
                   subproduct: str, 
                   version: str) -> str:
        try:
            from ctypes import windll  # Only exists on Windows.
            windll.shell32.SetCurrentProcessExplicitAppUserModelID(f"{company}.{product}.{subproduct}.{version}")
        except ImportError:
            pass