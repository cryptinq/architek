from typing import Optional, List

from core.exceptions.KernelException import KernelException


class KeySet:

    def __init__(self, configuration: dict):
        self._keys = configuration.keys()
        self._configuration = configuration

    def get(self, key: str):
        if key not in self.keys(): KernelException("KeyNotFoundException", key)
        return KeySet(self._configuration[key]) \
            if isinstance(self._configuration[key], dict) \
            else self._configuration[key]

    def set(self, key: str, value): self._configuration[key] = value

    def is_empty(self): return len(self.keys()) == 0

    def keys(self): return self._keys
    def has_key(self, key): return key in self.keys()

    def has_keys(self, keys: list): return all(key in self.keys() for key in keys)
    def missing_keys(self, keys: list) -> Optional[List]: return [key for key in keys if key not in self.keys()]


