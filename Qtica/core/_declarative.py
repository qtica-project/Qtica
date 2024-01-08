#!/usr/bin/python3

from typing import Any


class DuplicateKeyError(Exception):
    def __init__(self, uid: str):
        super().__init__(uid)
        print(f"'{uid}' was registered in this dictionary!")


class _TrackingDec:
    def __init__(self):
        self._instances_dict = dict()

    def _register(self, uid: str, obj: Any) -> None:
        if not isinstance(uid, str):
            raise ValueError("invalid uid, must be str type.")

        if uid in self._instances_dict:
            raise DuplicateKeyError(uid)
        self._instances_dict[uid] = obj

    def _deregister(self, uid: str) -> Any:
        """ deregister widget from manager """
        if not isinstance(uid, str):
            raise ValueError("invalid uid, must be str type.")

        if uid not in self._instances_dict:
            return

        return self._instances_dict.pop(uid)

    def pop(self, uid: str) -> Any:
       self._deregister(uid)

    def get(self, uid: str) -> Any:
        return self._instances_dict.get(uid)

    def items(self) -> Any:
        return self._instances_dict.items()

TrackingDec = _TrackingDec()


class AbstractDec:
    """
    `__init__` method can now return a value

    ### usage example
    ```python
    class Object(AbstractDec):
        def __init__(self, *args, **kwargs) -> object:
            return ...
    ```
    
    #### NOTE: use `uid` parameter to store this class in `TrackingDec`, \
        and call it with Api.fetch
    """

    def __new__(cls, *args, **kwargs) -> Any:
        instance = super().__new__(cls)

        if not hasattr(cls, "objectName"):
            _uid = (kwargs.pop
                    if 'uid' not in
                    instance.__init__.__code__.co_varnames
                    else kwargs.get)("uid", None)

            if _uid is not None:
                TrackingDec._register(_uid, instance)

        return instance.__init__(*args, **kwargs)


class BehaviorDec(AbstractDec):
    pass
