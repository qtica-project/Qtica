#!/usr/bin/python3

import os
from PySide6.QtCore import QThread, Signal, QUrl
from PySide6.QtWidgets import QProgressBar, QWidget
from ..core import BehaviorDeclarative, QObjectBase


class CopyProgress(BehaviorDeclarative):
    def __init__(self,
                 *,
                 child: QProgressBar | QWidget,
                 src: str | QUrl,
                 dst: str | QUrl,
                 filename: str = None,
                 running: bool = False,
                 chunk_size: int = 1024 * (1024 // 2),
                 overwrite: bool = False,
                 **kwargs) -> QWidget:

        for method in (
            "maximum",
            "setValue"
        ):
            if not hasattr(child, method):
                raise ValueError("invalid progress bar widget!")

        self.child = child
        self.copy_thread = CopyThread(self.child, 
                                      src, 
                                      dst,
                                      filename, 
                                      chunk_size,
                                      overwrite,
                                      **kwargs)

        self.copy_thread.copy_progress.connect(self.update_progress)

        if running:
            self.copy_thread.start()

        return self.child
    
    def set_src(self, path: str | QUrl):
        self.copy_thread.set_src(path)
    
    def set_dst(self, path: str | QUrl):
        self.copy_thread.set_dst(path)

    def start(self):
        self.copy_thread.start()

    def pause(self):
        self.copy_thread.pause()

    def resum(self):
        self.copy_thread.resum()

    def update_progress(self, progress: int):
        self.child.setValue(progress)

    def build(self):
        return self.copy_thread


class CopyThread(QObjectBase, QThread):
    copy_done = Signal()
    copy_paused = Signal()
    copy_progress = Signal(int)

    def __init__(self, 
                 parent, 
                 src, 
                 dst, 
                 filename, 
                 chunk_size,
                 overwrite,
                 **kwargs):

        QThread.__init__(self, parent)
        super().__init__(**kwargs)

        self.set_src(src)
        self.set_dst(dst)

        self.filename = filename
        self.chunk_size = chunk_size
        self.overwrite = overwrite
        self._is_paused: bool = False

    def set_src(self, path: str | QUrl):
        self.src = (path.toLocalFile() 
                    if isinstance(path, QUrl) 
                    else path)

    def set_dst(self, path: str | QUrl):
        self.dst = (path.toLocalFile() 
                    if isinstance(path, QUrl) 
                    else path)

    def get_filename(self):
        if self.filename is not None:
            return self.filename

        return os.path.basename(self.src)

    @property
    def file_destination(self):
        return os.path.join(self.dst, self.get_filename())

    def run(self):
        self.copy()

    def pause(self):
        self._is_paused = True
        self.copy_paused.emit()

    def resum(self):
        self._is_paused = False

        if not os.path.exists(self.src):
            raise FileNotFoundError(f"'{self.src}' does not exist!")

        if not os.path.exists(self.file_destination):
            raise FileNotFoundError(f"'{self.file_destination}' does not exist!")

        source_size = os.path.getsize(self.src)
        dest_size = os.path.getsize(self.file_destination)
        copied = dest_size

        with (open(self.src, "rb") as source, 
              open(self.file_destination, "ab") as target):

            source.seek(dest_size, 1)

            while True:
                chunk = source.read(self.chunk_size)
                if not chunk:
                    break

                target.write(chunk)
                copied += len(chunk)
                progress = copied * (self.parent().maximum() 
                                        if self.parent() is not None 
                                        else 100) / source_size

                self.copy_progress.emit(progress)

                if progress >= 100:
                    self.copy_done.emit()

    def copy(self):
        if os.path.exists(self.file_destination) and not self.overwrite:
            raise FileExistsError(self.file_destination)

        source_size = os.path.getsize(self.src)
        copied = 0

        with (open(self.src, "rb") as source,
              open(self.file_destination, "wb") as target):

            while True:
                if self._is_paused:
                    break

                chunk = source.read(self.chunk_size)
                if not chunk:
                    self.copy_done.emit()
                    break

                target.write(chunk)
                copied += len(chunk)
                progress = copied * (self.parent().maximum() 
                                     if self.parent() is not None 
                                     else 100) / source_size

                self.copy_progress.emit(progress)

                # if progress >= 100:
                #     self.copy_done.emit()