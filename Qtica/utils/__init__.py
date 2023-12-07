from .overload import singledispatchmethod
from .exception_handler import exceptionHandler
from .auto_wrap import TextWrap
from ._ensure_thread import CallCallable, ensure_object_thread, ensure_main_thread
from ._message_handler import MessageHandler

import uuid

def UniqueIdentifier() -> str:
    return uuid.uuid4().hex